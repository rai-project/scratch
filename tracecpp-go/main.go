package main

/*

#include "stdlib.h"

extern void go_callback_int(char * foo, int p1);

// normally you will have to define function or variables
// in another separate C file to avoid the multiple definition
// errors, however, using "static inline" is a nice workaround
// for simple functions like this one.
static inline void CallMyFunction(char * foo) {
	go_callback_int(foo, 5);
}
*/
import "C"
import (
	"fmt"
	"sync"
	"unsafe"
)

//export go_callback_int
func go_callback_int(foo *C.char, p1 C.int) {
	fn := lookup(C.GoString(foo))
	fn(p1)
}

func MyCallback(x C.int) {
	fmt.Println("callback with", x)
}

func Example() {
	name := register("MyCallback", MyCallback)
	cstr := C.CString(name)
	defer C.free(unsafe.Pointer(cstr))
	C.CallMyFunction(cstr)
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

func main() {
	Example()
}
