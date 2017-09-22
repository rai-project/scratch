# -*- coding: utf-8 -*-

"""Console script for python_predictor."""

import sys
import os.path

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "gens"))

import click
import grpc
import time
from concurrent import futures
import python_predictor
import predictor_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

addr = '[::]:50051'


@click.command()
def main(args=None):
    click.echo("Running GRPC server on " + addr)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predictor_pb2_grpc.add_PredictServicer_to_server(
        python_predictor.Predictor(), server)
    server.add_insecure_port(addr)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
