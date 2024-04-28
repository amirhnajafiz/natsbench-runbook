package nats

import "os/exec"

// executeCommand is used to run shell commands.
// args[0] = command name
// args[1:] = command arguments
func executeCommand(args []string) (string, error) {
	cmd := exec.Command(args[0], args[1:]...)

	stdout, err := cmd.Output()
	if err != nil {
		return "", err
	}

	return string(stdout), nil
}
