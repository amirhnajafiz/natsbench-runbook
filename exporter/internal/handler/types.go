package handler

import (
	"encoding/json"
	"strings"
	"time"
)

type customDate time.Time

func (j *customDate) UnmarshalJSON(b []byte) error {
	s := strings.Trim(string(b), "\"")

	t, err := time.Parse("2006-01-02 15:04:05.000000", s)
	if err != nil {
		return err
	}

	*j = customDate(t)

	return nil
}

func (j customDate) MarshalJSON() ([]byte, error) {
	return json.Marshal(time.Time(j))
}

type fileMeta struct {
	Date     customDate  `json:"date"`
	Name     string      `json:"name"`
	Location string      `json:"location"`
	Command  interface{} `json:"run-command"`
}
