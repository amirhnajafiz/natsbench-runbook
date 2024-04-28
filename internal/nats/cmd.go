package nats

import "strings"

type cli struct{}

func (c cli) List() []string {
	args := []string{
		"nats",
		"context",
		"ls",
		"--names",
	}

	list := make([]string, 0)

	out, err := executeCommand(args)
	if err != nil {
		return list
	}

	parts := strings.Split(out, "\n")
	for _, part := range parts {
		if len(part) > 0 {
			list = append(list, part)
		}
	}

	return list
}

func (c cli) Get(name string) string {
	args := []string{
		"nats",
		"context",
		"info",
		name,
		"--json",
	}

	out, err := executeCommand(args)
	if err != nil {
		return ""
	}

	return out
}

func (c cli) Select(name string) {
	args := []string{
		"nats",
		"context",
		"select",
		name,
	}

	_, _ = executeCommand(args)
}
