package cache

import "time"

type item struct {
	CreatedAt  time.Time `json:"created_at"`
	FinishedAt time.Time `json:"finished_at"`
	Done       bool      `json:"is_done"`
	Command    string    `json:"command"`
	Output     []string  `json:"output"`
}
