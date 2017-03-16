package main

import (
	"os"

	"github.com/Sirupsen/logrus"
	"github.com/docker/docker/cli/command"
	"github.com/docker/docker/pkg/signal"
	"github.com/docker/docker/pkg/term"
	"github.com/rai-project/config"
	"github.com/rai-project/docker"
	"github.com/rai-project/logger"
)

var (
	log       *logrus.Entry
	ImageName = "ubuntu:16.10"
)

func main() {
	config.Init(
		config.VerboseMode(true),
		config.DebugMode(true),
	)

	term.SetRawTerminal(os.Stdin.Fd())
	term.SetRawTerminal(os.Stdout.Fd())
	term.SetRawTerminal(os.Stderr.Fd())

	sstdin, sstdout, sstderr := term.StdStreams()

	// p, tty, err := pty.Open()
	// pp.Println(err)
	// if err == nil {
	// 	sstdout = tty
	// 	sstderr = tty
	// 	sstdin = tty
	// 	defer tty.Close()
	// 	defer p.Close()
	// }

	stdout := command.NewOutStream(sstdout)
	stderr := command.NewOutStream(sstderr)
	stdin := command.NewInStream(sstdin)

	dockerClient, err := docker.NewClient(
		docker.Stdout(stdout),
		docker.Stderr(stderr),
		docker.Stdin(stdin),
	)
	if err != nil {
		log.WithError(err).Fatal("cannot create docker client")
	}
	defer dockerClient.Close()

	if !dockerClient.HasImage(ImageName) {
		if err := dockerClient.PullImage(ImageName); err != nil {
			log.WithError(err).WithField("image", ImageName).Fatal("unable to pull image")
		}
	}

	containerOpts := []docker.ContainerOption{
		docker.AddVolume("/src"),
		docker.AddVolume("/build"),
		docker.WorkingDirectory("/"),
	}

	container, err := docker.NewContainer(dockerClient, containerOpts...)
	if err != nil {
		log.WithError(err).WithField("image", ImageName).Fatal("unable to create container")
	}
	defer container.Stop()

	sigc := container.ForwardAllSignals()
	defer signal.StopCatch(sigc)

	if err := container.Start(); err != nil {
		log.WithError(err).WithField("image", ImageName).Fatal("unable to start container")
	}
	container.MonitorTtySize()

	// cmd := "/bin/sh"
	// exec, err := docker.NewExecutionFromString(container, cmd)
	// if err != nil {
	// 	log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	// }

	// exec.Stdin = os.Stdin
	// exec.Stderr = stderr
	// exec.Stdout = stdout

	// exec.MonitorTtySize()

	// if err := exec.Run(); err != nil {
	// 	log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	// }

	container.Attach()

	// death := death.NewDeath(syscall.SIGINT, syscall.SIGTERM)

	// death.WaitForDeath()
}

func init() {
	config.AfterInit(func() {
		log = logger.New().WithField("pkg", "docker-stdin-test")
	})
}
