// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: google/monitoring/v3/group_service.proto

#include "google/monitoring/v3/group_service.pb.h"
#include "google/monitoring/v3/group_service.grpc.pb.h"

#include <grpc++/impl/codegen/async_stream.h>
#include <grpc++/impl/codegen/async_unary_call.h>
#include <grpc++/impl/codegen/channel_interface.h>
#include <grpc++/impl/codegen/client_unary_call.h>
#include <grpc++/impl/codegen/method_handler_impl.h>
#include <grpc++/impl/codegen/rpc_service_method.h>
#include <grpc++/impl/codegen/service_type.h>
#include <grpc++/impl/codegen/sync_stream.h>
namespace google {
namespace monitoring {
namespace v3 {

static const char* GroupService_method_names[] = {
  "/google.monitoring.v3.GroupService/ListGroups",
  "/google.monitoring.v3.GroupService/GetGroup",
  "/google.monitoring.v3.GroupService/CreateGroup",
  "/google.monitoring.v3.GroupService/UpdateGroup",
  "/google.monitoring.v3.GroupService/DeleteGroup",
  "/google.monitoring.v3.GroupService/ListGroupMembers",
};

std::unique_ptr< GroupService::Stub> GroupService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  std::unique_ptr< GroupService::Stub> stub(new GroupService::Stub(channel));
  return stub;
}

GroupService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_ListGroups_(GroupService_method_names[0], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetGroup_(GroupService_method_names[1], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_CreateGroup_(GroupService_method_names[2], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_UpdateGroup_(GroupService_method_names[3], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_DeleteGroup_(GroupService_method_names[4], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_ListGroupMembers_(GroupService_method_names[5], ::grpc::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status GroupService::Stub::ListGroups(::grpc::ClientContext* context, const ::google::monitoring::v3::ListGroupsRequest& request, ::google::monitoring::v3::ListGroupsResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_ListGroups_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::ListGroupsResponse>* GroupService::Stub::AsyncListGroupsRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::ListGroupsRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::ListGroupsResponse>::Create(channel_.get(), cq, rpcmethod_ListGroups_, context, request);
}

::grpc::Status GroupService::Stub::GetGroup(::grpc::ClientContext* context, const ::google::monitoring::v3::GetGroupRequest& request, ::google::monitoring::v3::Group* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_GetGroup_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>* GroupService::Stub::AsyncGetGroupRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::GetGroupRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>::Create(channel_.get(), cq, rpcmethod_GetGroup_, context, request);
}

::grpc::Status GroupService::Stub::CreateGroup(::grpc::ClientContext* context, const ::google::monitoring::v3::CreateGroupRequest& request, ::google::monitoring::v3::Group* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_CreateGroup_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>* GroupService::Stub::AsyncCreateGroupRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::CreateGroupRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>::Create(channel_.get(), cq, rpcmethod_CreateGroup_, context, request);
}

::grpc::Status GroupService::Stub::UpdateGroup(::grpc::ClientContext* context, const ::google::monitoring::v3::UpdateGroupRequest& request, ::google::monitoring::v3::Group* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_UpdateGroup_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>* GroupService::Stub::AsyncUpdateGroupRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::UpdateGroupRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::Group>::Create(channel_.get(), cq, rpcmethod_UpdateGroup_, context, request);
}

::grpc::Status GroupService::Stub::DeleteGroup(::grpc::ClientContext* context, const ::google::monitoring::v3::DeleteGroupRequest& request, ::google::protobuf::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_DeleteGroup_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>* GroupService::Stub::AsyncDeleteGroupRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::DeleteGroupRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::protobuf::Empty>::Create(channel_.get(), cq, rpcmethod_DeleteGroup_, context, request);
}

::grpc::Status GroupService::Stub::ListGroupMembers(::grpc::ClientContext* context, const ::google::monitoring::v3::ListGroupMembersRequest& request, ::google::monitoring::v3::ListGroupMembersResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_ListGroupMembers_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::ListGroupMembersResponse>* GroupService::Stub::AsyncListGroupMembersRaw(::grpc::ClientContext* context, const ::google::monitoring::v3::ListGroupMembersRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::ClientAsyncResponseReader< ::google::monitoring::v3::ListGroupMembersResponse>::Create(channel_.get(), cq, rpcmethod_ListGroupMembers_, context, request);
}

GroupService::Service::Service() {
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[0],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::ListGroupsRequest, ::google::monitoring::v3::ListGroupsResponse>(
          std::mem_fn(&GroupService::Service::ListGroups), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[1],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::GetGroupRequest, ::google::monitoring::v3::Group>(
          std::mem_fn(&GroupService::Service::GetGroup), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[2],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::CreateGroupRequest, ::google::monitoring::v3::Group>(
          std::mem_fn(&GroupService::Service::CreateGroup), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[3],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::UpdateGroupRequest, ::google::monitoring::v3::Group>(
          std::mem_fn(&GroupService::Service::UpdateGroup), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[4],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::DeleteGroupRequest, ::google::protobuf::Empty>(
          std::mem_fn(&GroupService::Service::DeleteGroup), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      GroupService_method_names[5],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< GroupService::Service, ::google::monitoring::v3::ListGroupMembersRequest, ::google::monitoring::v3::ListGroupMembersResponse>(
          std::mem_fn(&GroupService::Service::ListGroupMembers), this)));
}

GroupService::Service::~Service() {
}

::grpc::Status GroupService::Service::ListGroups(::grpc::ServerContext* context, const ::google::monitoring::v3::ListGroupsRequest* request, ::google::monitoring::v3::ListGroupsResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GroupService::Service::GetGroup(::grpc::ServerContext* context, const ::google::monitoring::v3::GetGroupRequest* request, ::google::monitoring::v3::Group* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GroupService::Service::CreateGroup(::grpc::ServerContext* context, const ::google::monitoring::v3::CreateGroupRequest* request, ::google::monitoring::v3::Group* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GroupService::Service::UpdateGroup(::grpc::ServerContext* context, const ::google::monitoring::v3::UpdateGroupRequest* request, ::google::monitoring::v3::Group* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GroupService::Service::DeleteGroup(::grpc::ServerContext* context, const ::google::monitoring::v3::DeleteGroupRequest* request, ::google::protobuf::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GroupService::Service::ListGroupMembers(::grpc::ServerContext* context, const ::google::monitoring::v3::ListGroupMembersRequest* request, ::google::monitoring::v3::ListGroupMembersResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace google
}  // namespace monitoring
}  // namespace v3

