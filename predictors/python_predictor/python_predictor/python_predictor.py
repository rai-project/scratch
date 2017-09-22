# -*- coding: utf-8 -*-

"""Main module."""

import uuid
import predictor_pb2
import predictor_pb2_grpc


class Predictor(predictor_pb2_grpc.PredictServicer):
    def Open(self, request, context):
        """Opens a predictor and returns an id where the predictor
        is accessible. The id can be used to perform inference
        requests.
        """
        return predictor_pb2.Predictor(id=uuid.uuid4())

    def Close(self, request, context):
        """rpc Information(Predictor) returns (PredictorInformation) {
        option (google.api.http) = {
        post : "/v1/predict/information",
        body : "*"
        };
        }

        Close a predictor clear it's memory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def URLs(self, request, context):
        """Image method receives a stream of urls and runs
        the predictor on all the urls. The

        The result is a prediction feature stream for each url.
        """
        return predictor_pb2.FeaturesResponse()

    def URLsStream(self, request, context):
        """Image method receives a stream of urls and runs
        the predictor on all the urls. The

        The result is a prediction feature stream for each url.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Images(self, request, context):
        """Image method receives a list base64 encoded images and runs
        the predictor on all the images.

        The result is a prediction feature list for each image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImagesStream(self, request, context):
        """Image method receives a list base64 encoded images and runs
        the predictor on all the images.

        The result is a prediction feature stream for each image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Dataset(self, request, context):
        """Dataset method receives a single dataset and runs
        the predictor on all elements of the dataset.

        The result is a prediction feature list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DatasetStream(self, request, context):
        """Dataset method receives a single dataset and runs
        the predictor on all elements of the dataset.

        The result is a prediction feature stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Clear method clears the internal cache of the predictors
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
