package nats

type cli struct{}

func (c cli) List() []string {
	return nil
}

func (c cli) Get(name string) string {
	return ""
}

func (c cli) Select(name string) {

}
