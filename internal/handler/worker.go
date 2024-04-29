package handler

import (
	"log"
	"os"
	"os/exec"
	"strings"

	"github.com/google/uuid"
)

func (h Handler) work(object string) {
	id := uuid.NewString()

	h.Cache.Put(id, object)
	defer func() {
		h.Cache.Del(id)
	}()

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

	out, err := cmd.Output()
	if err != nil {
		log.Println(err)

		return
	}

	parts := strings.Split(string(out), "\n")
	for _, part := range parts {
		if len(part) > 0 {
			h.Cache.Add(id, strings.Trim(part, "\t"))
		}
	}
}
