package handler

import (
	"log"
	"os"
	"os/exec"

	"github.com/google/uuid"
)

func (h Handler) work(object string) {
	id := uuid.NewString()

	h.Cache.Put(id, object)
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

	h.Cache.Del(id)
}
