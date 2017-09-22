#include <iostream>
#include <map>
#include <memory>
#include <mutex>
#include <string>

#include <grpc++/grpc++.h>

#include "github.com/gogo/protobuf/gogoproto/gogo.pb.cc"
#include "google/api/annotations.pb.cc"
#include "google/api/http.pb.cc"

#include "predictor.grpc.pb.h"
#include "utils.hpp"

// Implementation of the Predictor service. We have to implement all of the
// service's methods - these will be invoked by the running gRPC server.

class PredictorImpl final : public ::carml::org::predictor::Predict::Service {
public:
  ::grpc::Status
  Open(::grpc::ServerContext *context,
       const ::carml::org::predictor::PredictorOpenRequest *request,
       ::carml::org::predictor::Predictor *response) {
    (void)context;
    (void)request;
    response->set_id(uuid4());
    return ::grpc::Status::OK;
  }

  ::grpc::Status
  Close(::grpc::ServerContext *context,
        const ::carml::org::predictor::Predictor *request,
        ::carml::org::predictor::PredictorCloseResponse *response) {
    (void)context;
    const auto id = request->id();
    (void)response;
    return ::grpc::Status::OK;
  }

  ::grpc::Status URLs(::grpc::ServerContext *context,
                      const ::carml::org::predictor::URLsRequest *request,
                      ::carml::org::predictor::FeaturesResponse *response) {
    (void)context;
    (void)request;
    (void)response;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status URLsStream(
      ::grpc::ServerContext *context,
      const ::carml::org::predictor::URLsRequest *request,
      ::grpc::ServerWriter<::carml::org::predictor::FeatureResponse> *writer) {
    (void)context;
    (void)request;
    (void)writer;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status Images(::grpc::ServerContext *context,
                        const ::carml::org::predictor::ImagesRequest *request,
                        ::carml::org::predictor::FeaturesResponse *response) {
    (void)context;
    (void)request;
    (void)response;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status ImagesStream(
      ::grpc::ServerContext *context,
      const ::carml::org::predictor::ImagesRequest *request,
      ::grpc::ServerWriter<::carml::org::predictor::FeatureResponse> *writer) {
    (void)context;
    (void)request;
    (void)writer;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status Dataset(::grpc::ServerContext *context,
                         const ::carml::org::predictor::DatasetRequest *request,
                         ::carml::org::predictor::FeaturesResponse *response) {
    (void)context;
    (void)request;
    (void)response;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status DatasetStream(
      ::grpc::ServerContext *context,
      const ::carml::org::predictor::DatasetRequest *request,
      ::grpc::ServerWriter<::carml::org::predictor::FeatureResponse> *writer) {
    (void)context;
    (void)request;
    (void)writer;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

  ::grpc::Status Reset(::grpc::ServerContext *context,
                       const ::carml::org::predictor::ResetRequest *request,
                       ::carml::org::predictor::ResetResponse *response) {
    (void)context;
    (void)request;
    (void)response;
    return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
  }

private:
  // Mutex serializing access to the map.
  std::mutex mutex;
};

void RunServer() {
  // This parts is taken from the "hello world" gRPC sample.
  std::string server_address("0.0.0.0:4050");
  PredictorImpl service;

  grpc::ServerBuilder builder;
  // Listen on the given address without any authentication mechanism.
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  // Register "service" as the instance through which we'll communicate with
  // clients. In this case it corresponds to an *synchronous* service.
  builder.RegisterService(server_address, &service);
  // Finally assemble the server.
  std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;

  // Wait for the server to shutdown. Note that some other thread must be
  // responsible for shutting down the server for this call to ever return.
  server->Wait();
}

int main(int argc, char **argv) {
  RunServer();

  return 0;
}
