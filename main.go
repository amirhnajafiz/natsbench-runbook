package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/amirhnajafiz/natsbench-runbook/internal/config"
	"github.com/amirhnajafiz/natsbench-runbook/internal/handler"
	"github.com/amirhnajafiz/natsbench-runbook/internal/nats"

	"github.com/gorilla/mux"
)

func main() {
	// load configs
	cfg := config.Load()

	// create a new mux router
	router := mux.NewRouter()

	// create a new handler
	h := handler.Handler{
		NatsCli: nats.New(),
	}

	// register exporter endpoints
	router.HandleFunc("/healthz", h.Health).Methods(http.MethodGet)
	router.HandleFunc("/context", h.ListContext).Methods(http.MethodGet)
	router.HandleFunc("/context/{context}", h.GetContext).Methods(http.MethodGet)
	router.HandleFunc("/context/{context}", h.SelectContext).Methods(http.MethodPost)
	router.HandleFunc("/", h.Runbook).Methods(http.MethodPost)

	// create a new server
	srv := &http.Server{
		Handler: router,
		Addr:    fmt.Sprintf("127.0.0.1:%d", cfg["port"].(int)),
	}

	log.Printf("server started on %d ...\n", cfg["port"].(int))

	// start the http server
	if err := srv.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}
