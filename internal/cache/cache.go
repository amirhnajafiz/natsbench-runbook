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
	}
}

func (c Cache) Del(name, output string) {
	c.storage[name].FinishedAt = time.Now()
	c.storage[name].Output = output
}

func (c Cache) List() []byte {
	bytes, err := json.Marshal(c.storage)
	if err != nil {
		return nil
	}

	return bytes
}
