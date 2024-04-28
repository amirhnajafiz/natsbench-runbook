package handler

import (
	"encoding/json"
	"log"
	"net/http"
)

func (h Handler) ListContext(w http.ResponseWriter, r *http.Request) {
	list := h.NatsCli.List()

	bytes, err := json.Marshal(list)
	if err != nil {
		log.Println(err)

		w.WriteHeader(http.StatusInternalServerError)

		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write(bytes)
}

func (h Handler) GetContext(w http.ResponseWriter, r *http.Request) {

}

func (h Handler) SelectContext(w http.ResponseWriter, r *http.Request) {

}
