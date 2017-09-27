package main

/*

#include "stdlib.h"

extern void go_callback_int(void * data, char * foo, int p1);

// normally you will have to define function or variables
// in another separate C file to avoid the multiple definition
// errors, however, using "static inline" is a nice workaround
// for simple functions like this one.
static inline void CallMyFunction(void * data, char * foo) {
	go_callback_int(data, foo, 5);
}
*/
import "C"
import (
	"fmt"
	"sync"
	"time"
	"unsafe"

	context "golang.org/x/net/context"

	"github.com/fatih/color"
	"github.com/k0kubun/pp"
	homedir "github.com/mitchellh/go-homedir"
	"github.com/rai-project/config"
	"github.com/rai-project/logger"
	tr "github.com/rai-project/tracer"
	_ "github.com/rai-project/tracer/jaeger"
	_ "github.com/rai-project/tracer/noop"
	_ "github.com/rai-project/tracer/zipkin"
	"github.com/sirupsen/logrus"
)

var (
	IsDebug   bool
	IsVerbose bool
	AppSecret string
	CfgFile   string
	tracer    tr.Tracer
	log       *logrus.Entry = logrus.New().WithField("pkg", "scratch/tracepp-go")
)

//export go_callback_int
func go_callback_int(data unsafe.Pointer, foo *C.char, p1 C.int) {
	ctx := (*context.Context)(data)
	callback(*ctx, foo, p1)
}

func callback(ctx context.Context, foo *C.char, p1 C.int) {

	span, ctx := tracer.StartSpanFromContext(ctx, C.GoString(foo))
	defer span.Finish()

	time.Sleep(time.Second)

	fn := lookup(C.GoString(foo))

	s, ctx := tracer.StartSpanFromContext(ctx, "calling fn")
	defer s.Finish()
	fn(p1)
}

func MyCallback(x C.int) {
	time.Sleep(time.Duration(x) * time.Second)
	fmt.Println("callback with", x)
}

func Example() {
	name := register("MyCallback", MyCallback)
	cstr := C.CString(name)
	defer C.free(unsafe.Pointer(cstr))

	ctx := context.Background()

	span, ctx := tracer.StartSpanFromContext(ctx, "top level")
	defer span.Finish()

	C.CallMyFunction(unsafe.Pointer(&ctx), cstr)
	unregister(name)
}

var mu sync.Mutex
var index int
var fns = make(map[string]func(C.int))

func register(name string, fn func(C.int)) string {
	mu.Lock()
	defer mu.Unlock()
	fns[name] = fn
	return name
}

func lookup(name string) func(C.int) {
	mu.Lock()
	defer mu.Unlock()
	return fns[name]
}

func unregister(name string) {
	mu.Lock()
	defer mu.Unlock()
	delete(fns, name)
}

// Init reads in config file and ENV variables if set.
func Init() {

	log.Level = logrus.DebugLevel
	config.AfterInit(func() {
		log = logger.New().WithField("pkg", "scratch/tracepp-go")
		tracer = tr.MustNew("tracepp")
		pp.Println(tracer.Endpoints())
	})

	color.NoColor = false
	opts := []config.Option{
		config.AppName("carml"),
		config.ColorMode(true),
		config.DebugMode(IsDebug),
		config.VerboseMode(IsVerbose),
	}
	if c, err := homedir.Expand(CfgFile); err == nil {
		CfgFile = c
	}
	config.Init(opts...)
}

func main() {
	Init()
	defer tr.Close()
	Example()
}
