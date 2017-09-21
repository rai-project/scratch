# Makefile for building the sample on Linux, with protoc and the gRPC plugins
# installed on the system following the instructions in gRPC's INSTALL file.
#
# Parts of are taken verbatim from examples/cpp/helloworld/Makefile, so if you
# want to be strict about these things - gRPC's (3-clause BSD) license applies
# to these parts.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# This code is in the public domain.

CXX = g++
TARGET_DIR = $(CURDIR)/src

CPPFLAGS += -I/usr/local/include -I $(TARGET_DIR) -I $(CURDIR)/gens -pthread
CXXFLAGS += -std=c++11

HOST_SYSTEM = $(shell uname | cut -f 1 -d_)
SYSTEM ?= $(HOST_SYSTEM)

ifeq ($(SYSTEM),Darwin)
LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++`\
					 -lgrpc++_reflection\
					 -ldl
else
LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++`\
					 -Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
					 -ldl
endif

PROTOC = protoc
GRPC_CPP_PLUGIN = grpc_cpp_plugin
GRPC_CPP_PLUGIN_PATH ?= `which $(GRPC_CPP_PLUGIN)`

EXECUTABLES = predictor_server
all: $(EXECUTABLES)

googleapis:
	mkdir -p $(CURDIR)/gens
	rm -fr $(CURDIR)/gens/google
	git clone --depth=1 https://github.com/googleapis/googleapis
	cd googleapis && \
	make && \
	mv gens $(CURDIR)/gens && \
	cd .. && \
	rm -fr googleapis

.PRECIOUS: $(TARGET_DIR)/%.grpc.pb.cc
$(TARGET_DIR)/%.grpc.pb.cc: ../predictor.proto
	$(PROTOC) --grpc_out=$(TARGET_DIR) --plugin=protoc-gen-grpc=$(GRPC_CPP_PLUGIN_PATH) $<

.PRECIOUS: $(TARGET_DIR)/%.pb.cc
$(TARGET_DIR)/%.pb.cc: ../predictor.proto
	mkdir -p $(TARGET_DIR)
	$(PROTOC) --cpp_out=$(TARGET_DIR) \
	-I../ \
	-I$(GOPATH)/src \
	-I$(GOPATH)/src/github.com/golang/protobuf/proto \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	$<

predictor_server: $(TARGET_DIR)/predictor.pb.o $(TARGET_DIR)/predictor.grpc.pb.o $(TARGET_DIR)/predictor_server.o
	$(CXX) $^ $(LDFLAGS) -o $@

clean:
	rm -f $(EXECUTABLES) $(TARGET_DIR)/*.pb.cc $(TARGET_DIR)/*.pb.h $(TARGET_DIR)/*.pb.o $(TARGET_DIR)/*.o



# The following is to test your system and ensure a smoother experience.
# They are by no means necessary to actually compile a grpc-enabled software.

PROTOC_CMD = which $(PROTOC)
PROTOC_CHECK_CMD = $(PROTOC) --version | grep -q libprotoc.3
PLUGIN_CHECK_CMD = which $(GRPC_CPP_PLUGIN)
HAS_PROTOC = $(shell $(PROTOC_CMD) > /dev/null && echo true || echo false)
ifeq ($(HAS_PROTOC),true)
HAS_VALID_PROTOC = $(shell $(PROTOC_CHECK_CMD) 2> /dev/null && echo true || echo false)
endif
HAS_PLUGIN = $(shell $(PLUGIN_CHECK_CMD) > /dev/null && echo true || echo false)

SYSTEM_OK = false
ifeq ($(HAS_VALID_PROTOC),true)
ifeq ($(HAS_PLUGIN),true)
SYSTEM_OK = true
endif
endif

system-check:
ifneq ($(HAS_VALID_PROTOC),true)
	@echo " DEPENDENCY ERROR"
	@echo
	@echo "You don't have protoc 3.0.0 installed in your path."
	@echo "Please install Google protocol buffers 3.0.0 and its compiler."
	@echo "You can find it here:"
	@echo
	@echo "   https://github.com/google/protobuf/releases/tag/v3.0.0"
	@echo
	@echo "Here is what I get when trying to evaluate your version of protoc:"
	@echo
	-$(PROTOC) --version
	@echo
	@echo
endif
ifneq ($(HAS_PLUGIN),true)
	@echo " DEPENDENCY ERROR"
	@echo
	@echo "You don't have the grpc c++ protobuf plugin installed in your path."
	@echo "Please install grpc. You can find it here:"
	@echo
	@echo "   https://github.com/grpc/grpc"
	@echo
	@echo "Here is what I get when trying to detect if you have the plugin:"
	@echo
	-which $(GRPC_CPP_PLUGIN)
	@echo
	@echo
endif
ifneq ($(SYSTEM_OK),true)
	@false
endif
