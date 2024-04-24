package config

import (
	"os"
	"strconv"
)

// Config struct is used for exporter config values
type Config struct {
	HTTPPort int
	Volume   string
}

// Load env variables into config struct
func Load() Config {
	port, _ := strconv.Atoi(os.Getenv("HTTP_PORT"))
	volume := os.Getenv("VOLUME_PATH")

	return Config{
		HTTPPort: port,
		Volume:   volume,
	}
}
