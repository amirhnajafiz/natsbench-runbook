package handler

import (
	"log"
	"net/http"
)

func (h Handler) Runbook(w http.ResponseWriter, r *http.Request) {
	bytes := make([]byte, 0)

	if _, err := r.Body.Read(bytes); err != nil {
		log.Println(err)

		w.WriteHeader(http.StatusBadRequest)

		return
	}

	go h.work(string(bytes))

	w.WriteHeader(http.StatusOK)
}
