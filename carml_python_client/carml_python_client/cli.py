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
@click.option('--framework_version', default='1.3.0', help="The framework version to use for inference.")
@click.option('--model_name', default="BVLC-AlexNet", help="The model to use for inference.")
@click.option('--model_version', default='1.0', help="The model version to use for inference.")
@click.option('--batch_size', default=256, help="The batch size to use for inference.")
@click.option('--trace_url', default="trace.mlmodelscope.org", help="The URL to the tracing server.")
@click.option('--trace_level', default='STEP_TRACE', help="The trace level to use for inference.")
def main(carml_url, urls, framework_name, framework_version, model_name, model_version, batch_size, trace_url, trace_level):
    """Console script for carml_python_client."""

    carml_url = carml_url.strip("/")
    if not carml_url.startswith("http"):
        carml_url = "http://" + carml_url
    trace_url = trace_url.strip("/")
    if not trace_url.startswith("http"):
        trace_url = "http://" + trace_url

    openAPIURL = carml_url + "/api/predict/open"
    urlsAPIURL = carml_url + "/api/predict/urls"
    closeAPIURL = carml_url + "/api/predict/close"

    # chalk.green("performing inference using " + carml_url)

    # click.echo("performing open predictor request on " + openAPIURL)
    openReq = requests.post(openAPIURL, json={
        'framework_name': framework_name,
        'framework_version': framework_version,
        'model_name': model_name,
        'model_version': model_version,
        'options': {
            'batch_size': int(batch_size),
            'execution_options': {
                'trace_level': trace_level,
                'device_count': {'GPU': 0}
            }
        }
    }, allow_redirects=False)
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
    # click.echo("using the id " + predictorId)

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
        allow_redirects=False,
    )

    urlReq.raise_for_status()

    # print(urlReq.json()["responses"][0]["features"][:5])

    requests.post(closeAPIURL, json={'id': predictorId}, headers=headers, allow_redirects=False)

    print( trace_url + ":16686/trace/" +  openReq.headers["X-B3-Traceid"])


if __name__ == "__main__":
    main()
