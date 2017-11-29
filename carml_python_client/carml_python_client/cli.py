# -*- coding: utf-8 -*-

"""Console script for carml_python_client."""

import click
import requests
import chalk
import json
import uuid


@click.command()
@click.option('--carml_url', default="impact2.csl.illinois.edu:9099", help='The URL to the CarML website.')
@click.option('--urls', default='example.txt', type=click.File('rb'), help="The file containing all the urls to perform inference on.")
@click.option('--framework_name', default='Caffe', help="The framework to use for inference.")
@click.option('--framework_version', default='1.0', help="The framework version to use for inference.")
@click.option('--model_name', default='SqueezeNet', help="The model to use for inference.")
@click.option('--model_version', default='1.0', help="The model version to use for inference.")
def main(carml_url, urls, framework_name, framework_version, model_name, model_version):
    """Console script for carml_python_client."""
    carml_url = carml_url.strip("/")
    if not carml_url.startswith("http"):
        carml_url = "http://" + carml_url
    openAPIURL = carml_url + "/api/predict/open"
    urlsAPIURL = carml_url + "/api/predict/urls"
    closeAPIURL = carml_url + "/api/predict/close"

    chalk.green("performing inference using " + carml_url)

    click.echo("performing open predictor request on " + openAPIURL)
    openReq = requests.post(openAPIURL, json={
        'framework_name': framework_name,
        'framework_version': framework_version,
        'model_name': model_name,
        'model_version': model_version,
        'options': {
            'execution_options': {
                'batch_size': 1,
                'trace_level': "FULL_TRACE",
            }
        }
    })
    openResponseContent = openReq.json()

    predictorId = openResponseContent["id"]
    click.echo("using the id " + predictorId)

    lines = urls.readlines()

    urlReq = [{'id': str(uuid.uuid4()), 'data': url.decode("utf-8").strip()}
              for url in lines]
    # print(urlReq)

    urlReq = requests.post(urlsAPIURL, json={
        'predictor': openResponseContent,
        'urls': urlReq,
        'options': {
            'feature_limit': 0,
        }
    })

    print(urlReq.json())

    requests.post(closeAPIURL, json={'id': predictorId})


if __name__ == "__main__":
    main()
