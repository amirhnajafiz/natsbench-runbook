package handler

import "time"

type inputFileMeta struct {
	Date     string      `json:"date"`
	Location string      `json:"location"`
	Command  interface{} `json:"run-command"`
}

type outputFileMeta struct {
	Date    time.Time   `json:"created_at"`
	Name    string      `json:"name"`
	Command interface{} `json:"command"`
}
