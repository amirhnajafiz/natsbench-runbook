package handler

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"sort"
	"strings"
	"time"

	"github.com/gorilla/mux"
)

// ServeCSV loads the csv file of the given project.
func (h Handler) ServeCSV(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	location := vars["benchmark"]
	path := fmt.Sprintf("%s/%s/dataset.csv", h.Volume, location)

	http.ServeFile(w, r, path)
}

// ListDirectories returns the list of benchmarks in details
func (h Handler) ListDirectories(w http.ResponseWriter, _ *http.Request) {
	// create a list of fileMeta type
	items := make([]fileMeta, 0)

	// get directory entries
	entries, err := os.ReadDir(fmt.Sprintf("%s/", h.Volume))
	if err != nil {
		log.Println(err)

		return
	}

	// read info files into fileMeta struct
	for _, e := range entries {
		data, err := os.ReadFile(fmt.Sprintf("%s/%s/info.json", h.Volume, e.Name()))
		if err != nil {
			log.Println(err)

			continue
		}

		instance := fileMeta{}
		if err := json.Unmarshal(data, &instance); err != nil {
			log.Println(err)

			continue
		}

		instance.Name = strings.Split(instance.Location, "/")[1]

		items = append(items, instance)
	}

	// sort based on created date
	sort.Slice(items, func(i, j int) bool {
		A := time.Time(items[i].Date)
		B := time.Time(items[j].Date)

		return A.Before(B)
	})

	// create json output
	bytes, err := json.Marshal(items)
	if err != nil {
		log.Println(err)

		return
	}

	w.Write(bytes)
}

// Health handler is used to check exporter status
func (h Handler) Health(w http.ResponseWriter, _ *http.Request) {
	w.WriteHeader(http.StatusOK)
}
