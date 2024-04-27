package nats

type CLI interface {
	List() []string
	Get(name string) string
	Select(name string)
}

func New() CLI {
	return &cli{}
}
