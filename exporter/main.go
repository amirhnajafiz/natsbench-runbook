package main

import (
	"fmt"
	"log"
	"os"
	"time"
)

const (
	baseDir = "tmp/"
)

type FileMeta struct {
	Date     time.Time `json:"date"`
	Location string    `json:"location"`
}

// serverCSV loads the csv file of the given project.
func serveCSV(location string) {
	path := fmt.Sprintf("%s%s/dataset.csv", baseDir, location)

	log.Println(path)
}

// listDirectories returns the list of tests
func listDirectories() []string {
	items := make([]string, 0)

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

		items = append(items, string(data))
	}

	return items
}

func main() {
	list := listDirectories()

	for _, item := range list {
		fmt.Println(item)
		fmt.Println()
	}
}
