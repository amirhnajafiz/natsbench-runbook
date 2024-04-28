package cache

import "time"

type item struct {
	CreatedAt time.Time `json:"created_at"`
	Command   string    `json:"command"`
}
