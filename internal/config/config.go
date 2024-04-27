package config

import (
	"os"
	"strconv"
)

func Load() map[string]interface{} {
	instance := make(map[string]interface{})

	instance["port"], _ = strconv.Atoi(os.Getenv("HTTP_PORT"))

	return instance
}
