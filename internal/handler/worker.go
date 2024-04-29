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
		"python3",
		"main.py",
		"-p",
		"true",
		"-j",
		object,
	}

	cmd := exec.Command(args[0], args[1:]...)

	out, err := cmd.Output()
	if err != nil {
		log.Println(err)
	}

	h.Cache.Del(id, string(out))
}
