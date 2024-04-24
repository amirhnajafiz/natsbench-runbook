package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
	"time"
)

const (
	baseDir = "tmp/"
)

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

// serverCSV loads the csv file of the given project.
func serveCSV(location string) {
	path := fmt.Sprintf("%s%s/dataset.csv", baseDir, location)

	log.Println(path)
}

// listDirectories returns the list of tests
func listDirectories() []outputFileMeta {
	items := make([]outputFileMeta, 0)

	entries, err := os.ReadDir(baseDir)
	if err != nil {
		log.Println(err)

		return items
	}

	for _, e := range entries {
		data, err := os.ReadFile(fmt.Sprintf("%s%s/info.json", baseDir, e.Name()))
		if err != nil {
			log.Println(err)

			continue
		}

		instance := inputFileMeta{}
		if err := json.Unmarshal(data, &instance); err != nil {
			log.Println(err)

			continue
		}

		output, er := time.Parse("2006-01-02 15:04:05.000000", instance.Date)
		if er != nil {
			log.Println(er)

			continue
		}

		out := outputFileMeta{
			Date:    output,
			Name:    strings.Split(instance.Location, "/")[1],
			Command: instance.Command,
		}

		items = append(items, out)
	}

	sort.Slice(items, func(i, j int) bool {
		return items[i].Date.Before(items[j].Date)
	})

	return items
}

func main() {
	list := listDirectories()

	bytes, err := json.Marshal(list)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(bytes))
}
