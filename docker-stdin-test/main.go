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

	sstdin, sstdout, sstderr := term.StdStreams()

	stdout := command.NewOutStream(sstdout)
	stderr := command.NewOutStream(sstderr)

	dockerClient, err := docker.NewClient(
		docker.Stdout(stdout),
		docker.Stderr(stderr),
		docker.Stdin(sstdin),
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

	container.MonitorTtySize()

	if err := container.Start(); err != nil {
		log.WithError(err).WithField("image", ImageName).Fatal("unable to start container")
	}

	cmd := "/bin/bash"
	exec, err := docker.NewExecutionFromString(container, cmd)
	if err != nil {
		log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	}

	exec.Stdin = os.Stdin
	exec.Stderr = stderr
	exec.Stdout = stdout

	exec.MonitorTtySize()

	if err := exec.Run(); err != nil {
		log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	}

	// death := death.NewDeath(syscall.SIGINT, syscall.SIGTERM)

	// death.WaitForDeath()
}

func init() {
	config.AfterInit(func() {
		log = logger.New().WithField("pkg", "docker-stdin-test")
	})
}
