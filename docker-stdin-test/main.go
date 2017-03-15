package main

import (
	"os"
	"syscall"

	"github.com/Sirupsen/logrus"
	"github.com/rai-project/config"
	"github.com/rai-project/docker"
	"github.com/rai-project/logger"
	"github.com/vrecan/death"
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

	dockerClient, err := docker.NewClient(
		docker.Stdout(os.Stdout),
		docker.Stderr(os.Stderr),
		docker.Stdin(os.Stdin),
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

	if err := container.Start(); err != nil {
		log.WithError(err).WithField("image", ImageName).Fatal("unable to start container")
	}

	cmd := "/bin/bash"
	exec, err := docker.NewExecutionFromString(container, cmd)
	if err != nil {
		log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	}

	exec.Stdin = os.Stdin
	exec.Stderr = os.Stderr
	exec.Stdout = os.Stdout

	if err := exec.Run(); err != nil {
		log.WithError(err).WithField("cmd", cmd).Fatal("unable to create docker execution")
	}

	death := death.NewDeath(syscall.SIGINT, syscall.SIGTERM)

	death.WaitForDeath()
}

func init() {
	config.AfterInit(func() {
		log = logger.New().WithField("pkg", "docker-stdin-test")
	})
}
