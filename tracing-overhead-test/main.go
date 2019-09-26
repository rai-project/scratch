package main

import (
	"context"
	"time"

	opentracing "github.com/opentracing/opentracing-go"
	"github.com/rai-project/config"
	"github.com/rai-project/tracer"
	_ "github.com/rai-project/tracer/jaeger"
)

func main() {
	var span opentracing.Span
	ctx := context.Background()

	span, ctx = tracer.StartSpanFromContext(ctx, tracer.FULL_TRACE, "test_run")
	time.Sleep(time.Second)
	span.Finish()

	tracer.Close()
}

func init() {
	config.Init(
		config.AppName("carml"),
		config.DebugMode(true),
		config.VerboseMode(true),
	)
}
