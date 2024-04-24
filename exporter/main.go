package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/amirhnajafiz/natsbench-runbook/exporter/internal/config"
	"github.com/amirhnajafiz/natsbench-runbook/exporter/internal/handler"

	"github.com/gorilla/mux"
)

func main() {
	// load config
	cfg := config.Load()

	// create a new mux router
	router := mux.NewRouter()

	// create a new handler
	h := handler.Handler{
		Volume: cfg.Volume,
	}

	// register exporter endpoints
	router.HandleFunc("/healthz", h.Health).Methods(http.MethodGet)
	router.HandleFunc("/benchmarks", h.ListDirectories).Methods(http.MethodGet)
	router.HandleFunc("/benchmarks/{benchmark}", h.ServeCSV).Methods(http.MethodGet)

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
