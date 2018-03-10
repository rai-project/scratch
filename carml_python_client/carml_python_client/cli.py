# -*- coding: utf-8 -*-

"""Console script for carml_python_client."""

import click
import requests
import chalk
import json
import uuid


@click.command()
@click.option('--carml_url', default="http://www.mlmodelscope.org", help='The URL to the CarML website.')
@click.option('--urls', default='example.txt', type=click.File('rb'), help="The file containing all the urls to perform inference on.")
@click.option('--framework_name', default='MXNet', help="The framework to use for inference.")
@click.option('--framework_version', default='0.11.0', help="The framework version to use for inference.")
@click.option('--model_name', default="BVLC-AlexNet", help="The model to use for inference.")
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
            'batch_size': 1,
            'execution_options': {
                'trace_level': "STEP_TRACE",
            }
        }
    })
    openReq.raise_for_status()

    # b3Sampled = openReq.headers["X-B3-Sampled"]
    # b3SpanId = openReq.headers["X-B3-Spanid"]
    # b3TraceId = openReq.headers["X-B3-Traceid"]
    # b3RequestId = openReq.headers["X-Request-Id"]

    headers = {
    "X-B3-Sampled": openReq.headers["X-B3-Sampled"],
    "X-B3-Spanid": openReq.headers["X-B3-Spanid"],
    "X-B3-Traceid":  openReq.headers["X-B3-Traceid"],
    "X-Request-Id": openReq.headers["X-Request-Id"],

    }

    # print(openReq.headers)

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
    },
        headers=headers,
    )

    urlReq.raise_for_status()

    print(urlReq.json()["responses"][0]["features"][:5])

    requests.post(closeAPIURL, json={'id': predictorId}, headers=headers)

    print("http://trace.mlmodelscope.org:16686/trace/" +  openReq.headers["X-B3-Traceid"])


if __name__ == "__main__":
    main()
