package handler

import (
	"bytes"
	"log"
	"net/http"
)

func (h Handler) List(w http.ResponseWriter, _ *http.Request) {
	bytes := h.Cache.List()
	if bytes == nil {
		w.WriteHeader(http.StatusInternalServerError)

		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write(bytes)
}

func (h Handler) Runbook(w http.ResponseWriter, r *http.Request) {
	buffer := bytes.Buffer{}

	if _, err := buffer.ReadFrom(r.Body); err != nil {
		log.Println(err)

		w.WriteHeader(http.StatusBadRequest)

		return
	}

	go h.work(buffer.String())

	w.WriteHeader(http.StatusOK)
}
