package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	// create a new mux router
	router := mux.NewRouter()

	// register exporter endpoints
	//router.HandleFunc("/healthz", h.Health).Methods(http.MethodGet)
	//router.HandleFunc("/benchmarks", h.ListDirectories).Methods(http.MethodGet)
	//router.HandleFunc("/benchmarks/{benchmark}", h.ServeCSV).Methods(http.MethodGet)

	// create a new server
	srv := &http.Server{
		Handler: router,
		Addr:    fmt.Sprintf("127.0.0.1:%d", 8080),
	}

	log.Printf("exporter started on %d ...\n", 8080)

	// start the http server
	if err := srv.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}
