# -*- coding: utf-8 -*-

"""Console script for python_predictor."""

import click
import python_predictor
import predictor_pb2_grpc


@click.command()
def main(args=None):
    """Console script for python_predictor."""
    click.echo("Replace this message by putting your code into "
               "python_predictor.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predictor_pb2_grpc.add_GreeterServicer_to_server(
        python_predictor.Predictor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
