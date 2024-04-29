package cache

import (
	"encoding/json"
	"time"
)

type Cache struct {
	storage map[string]*item
}

func New() Cache {
	return Cache{
		storage: make(map[string]*item),
	}
}

func (c Cache) Put(name, command string) {
	c.storage[name] = &item{
		CreatedAt: time.Now(),
		Command:   command,
		Output:    make([]string, 0),
		Done:      false,
	}
}

func (c Cache) Add(name, content string) {
	c.storage[name].Output = append(c.storage[name].Output, content)
}

func (c Cache) Del(name string) {
	c.storage[name].FinishedAt = time.Now()
	c.storage[name].Done = true
}

func (c Cache) List() []byte {
	bytes, err := json.Marshal(c.storage)
	if err != nil {
		return nil
	}

	return bytes
}
