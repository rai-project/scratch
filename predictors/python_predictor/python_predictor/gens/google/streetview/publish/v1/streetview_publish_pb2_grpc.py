# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.streetview.publish.v1 import resources_pb2 as google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2
from google.streetview.publish.v1 import rpcmessages_pb2 as google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2


class StreetViewPublishServiceStub(object):
  """Definition of the service that backs the Street View Publish API.

  Publishes and connects user-contributed photos on Street View.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartUpload = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/StartUpload',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.UploadRef.FromString,
        )
    self.CreatePhoto = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/CreatePhoto',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.CreatePhotoRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.FromString,
        )
    self.GetPhoto = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/GetPhoto',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.GetPhotoRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.FromString,
        )
    self.BatchGetPhotos = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/BatchGetPhotos',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchGetPhotosRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchGetPhotosResponse.FromString,
        )
    self.ListPhotos = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/ListPhotos',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.ListPhotosRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.ListPhotosResponse.FromString,
        )
    self.UpdatePhoto = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/UpdatePhoto',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.UpdatePhotoRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.FromString,
        )
    self.BatchUpdatePhotos = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/BatchUpdatePhotos',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchUpdatePhotosRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchUpdatePhotosResponse.FromString,
        )
    self.DeletePhoto = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/DeletePhoto',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.DeletePhotoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BatchDeletePhotos = channel.unary_unary(
        '/google.streetview.publish.v1.StreetViewPublishService/BatchDeletePhotos',
        request_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchDeletePhotosRequest.SerializeToString,
        response_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchDeletePhotosResponse.FromString,
        )


class StreetViewPublishServiceServicer(object):
  """Definition of the service that backs the Street View Publish API.

  Publishes and connects user-contributed photos on Street View.
  """

  def StartUpload(self, request, context):
    """Creates an upload session to start uploading photo data. The upload URL of
    the returned `UploadRef` is used to upload the data for the photo.

    After the upload is complete, the `UploadRef` is used with
    `StreetViewPublishService:CreatePhoto()` to create the `Photo` object
    entry.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePhoto(self, request, context):
    """After the client finishes uploading the photo with the returned
    `UploadRef`, `photo.create` publishes the uploaded photo to Street View on
    Google Maps.

    This method returns the following error codes:

    * `INVALID_ARGUMENT` if the request is malformed.
    * `NOT_FOUND` if the upload reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPhoto(self, request, context):
    """Gets the metadata of the specified `Photo`.

    This method returns the following error codes:

    * `PERMISSION_DENIED` if the requesting user did not create the requested
    photo.
    * `NOT_FOUND` if the requested photo does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchGetPhotos(self, request, context):
    """Gets the metadata of the specified `Photo` batch.

    Note that if `photos.batchGet` fails, either critical fields are
    missing or there was an authentication error.
    Even if `photos.batchGet` succeeds, there may have been failures
    for single photos in the batch. These failures will be specified in
    `BatchGetPhotosResponse.results.status`.
    See `photo.get` for specific failures that will occur per photo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPhotos(self, request, context):
    """Lists all the photos that belong to the user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePhoto(self, request, context):
    """Updates the metadata of a photo, such as pose, place association, etc.
    Changing the pixels of a photo is not supported.

    This method returns the following error codes:

    * `PERMISSION_DENIED` if the requesting user did not create the requested
    photo.
    * `INVALID_ARGUMENT` if the request is malformed.
    * `NOT_FOUND` if the photo ID does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchUpdatePhotos(self, request, context):
    """Updates the metadata of photos, such as pose, place association, etc.
    Changing the pixels of a photo is not supported.

    Note that if `photos.batchUpdate` fails, either critical fields
    are missing or there was an authentication error.
    Even if `photos.batchUpdate` succeeds, there may have been
    failures for single photos in the batch. These failures will be specified
    in `BatchUpdatePhotosResponse.results.status`.
    See `UpdatePhoto` for specific failures that will occur per photo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePhoto(self, request, context):
    """Deletes a photo and its metadata.

    This method returns the following error codes:

    * `PERMISSION_DENIED` if the requesting user did not create the requested
    photo.
    * `NOT_FOUND` if the photo ID does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchDeletePhotos(self, request, context):
    """Deletes a list of photos and their metadata.

    Note that if `photos.batchDelete` fails, either critical fields
    are missing or there was an authentication error.
    Even if `photos.batchDelete` succeeds, there may have been
    failures for single photos in the batch. These failures will be specified
    in `BatchDeletePhotosResponse.status`.
    See `photo.update` for specific failures that will occur per photo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StreetViewPublishServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartUpload': grpc.unary_unary_rpc_method_handler(
          servicer.StartUpload,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.UploadRef.SerializeToString,
      ),
      'CreatePhoto': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePhoto,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.CreatePhotoRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.SerializeToString,
      ),
      'GetPhoto': grpc.unary_unary_rpc_method_handler(
          servicer.GetPhoto,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.GetPhotoRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.SerializeToString,
      ),
      'BatchGetPhotos': grpc.unary_unary_rpc_method_handler(
          servicer.BatchGetPhotos,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchGetPhotosRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchGetPhotosResponse.SerializeToString,
      ),
      'ListPhotos': grpc.unary_unary_rpc_method_handler(
          servicer.ListPhotos,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.ListPhotosRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.ListPhotosResponse.SerializeToString,
      ),
      'UpdatePhoto': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePhoto,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.UpdatePhotoRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2.Photo.SerializeToString,
      ),
      'BatchUpdatePhotos': grpc.unary_unary_rpc_method_handler(
          servicer.BatchUpdatePhotos,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchUpdatePhotosRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchUpdatePhotosResponse.SerializeToString,
      ),
      'DeletePhoto': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePhoto,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.DeletePhotoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BatchDeletePhotos': grpc.unary_unary_rpc_method_handler(
          servicer.BatchDeletePhotos,
          request_deserializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchDeletePhotosRequest.FromString,
          response_serializer=google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2.BatchDeletePhotosResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.streetview.publish.v1.StreetViewPublishService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
