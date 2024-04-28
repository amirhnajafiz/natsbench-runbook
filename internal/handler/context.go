package handler

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
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
	vars := mux.Vars(r)
	ctx := vars["context"]

	out := h.NatsCli.Get(ctx)

	w.WriteHeader(http.StatusOK)
	w.Write([]byte(out))
}

func (h Handler) SelectContext(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	ctx := vars["context"]

	h.NatsCli.Select(ctx)

	w.WriteHeader(http.StatusOK)
}
