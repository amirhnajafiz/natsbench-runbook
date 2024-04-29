package cache

import "time"

type item struct {
	CreatedAt  time.Time `json:"created_at"`
	FinishedAt time.Time `json:"finished_at"`
	Command    string    `json:"command"`
}
