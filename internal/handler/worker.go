package handler

import (
	"log"
	"os"
	"os/exec"
)

func (h Handler) work(object string) {
	os.Chdir("runbook/")

	args := []string{
		"python",
		"main.py",
		"-p",
		"true",
		"-j",
		object,
	}

	cmd := exec.Command(args[0], args[1:]...)
	if out, err := cmd.Output(); err != nil {
		log.Println(err)
	} else {
		log.Println(out)
	}
}
