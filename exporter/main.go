package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"sort"
	"strings"
	"time"

	"github.com/amirhnajafiz/natsbench-runbook/exporter/internal/config"

	"github.com/gorilla/mux"
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
func serveCSV(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	location := vars["benchmark"]
	path := fmt.Sprintf("%s%s/dataset.csv", baseDir, location)

	http.ServeFile(w, r, path)
}

// listDirectories returns the list of benchmarks in details
func listDirectories(w http.ResponseWriter, _ *http.Request) {
	// create a list of outputFileMeta type
	items := make([]outputFileMeta, 0)

	// get directory entries
	entries, err := os.ReadDir(baseDir)
	if err != nil {
		log.Println(err)

		return
	}

	// read info file
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

	// sort based on created date
	sort.Slice(items, func(i, j int) bool {
		return items[i].Date.Before(items[j].Date)
	})

	// create json output
	bytes, err := json.Marshal(items)
	if err != nil {
		log.Println(err)

		return
	}

	w.Write(bytes)
}

// health handler is used to check exporter status
func health(w http.ResponseWriter, _ *http.Request) {
	w.WriteHeader(http.StatusOK)
}

func main() {
	// load config
	cfg := config.Load()

	// create a new mux router
	router := mux.NewRouter()

	// register exporter endpoints
	router.HandleFunc("/healthz", health).Methods(http.MethodGet)
	router.HandleFunc("/benchmarks", listDirectories).Methods(http.MethodGet)
	router.HandleFunc("/benchmarks/{benchmark}", serveCSV).Methods(http.MethodGet)

	// create a new server
	srv := &http.Server{
		Handler: router,
		Addr:    fmt.Sprintf("127.0.0.1:%d", cfg.HTTPPort),
	}

	log.Printf("exporter started on %d ...\n", cfg.HTTPPort)

	// start the http server
	if err := srv.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}
