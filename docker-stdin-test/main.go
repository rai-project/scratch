package main

import (
	"github.com/Sirupsen/logrus"
	"github.com/moby/moby/cli/command"
	"github.com/moby/moby/pkg/signal"
	"github.com/moby/moby/pkg/term"
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

	// _, err := term.SetRawTerminal(os.Stdin.Fd())
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// _, err := term.SetRawTerminal(os.Stdout.Fd())
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// _, err = term.SetRawTerminal(os.Stderr.Fd())
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// if term.IsTerminal(os.Stdin.Fd()) {
	// 	fmt.Println("stdin is a term")
	// 	state, err := term.SaveState(os.Stdin.Fd())
	// 	if err != nil {
	// 		log.Fatal(err)
	// 	}
	// 	term.DisableEcho(os.Stdin.Fd(), state)
	// 	defer term.RestoreTerminal(os.Stdin.Fd(), state)
	// }

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
	// defer func() {
	// 	fmt.Println("Restoring stdin")
	// 	stdin.RestoreTerminal()
	// 	stdin.Close()
	// }()
	// defer func() {
	// 	fmt.Println("Restoring stdout")
	// 	stdout.RestoreTerminal()
	// }()
	// defer func() {
	// 	fmt.Println("Restoring stderr")
	// 	stderr.RestoreTerminal()
	// }()

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
		docker.Tty(true /*default*/),
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

	// height, width := stdout.GetTtySize()
	// options := types.ResizeOptions{
	// 	Height: height + 1,
	// 	Width:  width + 1,
	// }
	// err = dockerClient.ContainerResize(context.Background(), container.ID, options)
	// container.MonitorTtySize()

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
