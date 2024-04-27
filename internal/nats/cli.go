package nats

type CLI interface {
	List() []string
	Get(name string) string
	Select(name string)
}

type cli struct{}

func New() CLI {
	return &cli{}
}

func (c cli) List() []string {
	return nil
}

func (c cli) Get(name string) string {
	return ""
}

func (c cli) Select(name string) {

}
