#!/bin/bash

# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="STEP_TRACE" --framework_name="MXNet" --framework_version="1.3.0" --batch_size 64
#python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FRAMEWORK_TRACE" --framework_name="MXNet" --framework_version="1.3.0" --batch_size 64
# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FULL_TRACE" --framework_name="MXNet" --framework_version="1.3.0" --batch_size 64

# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="STEP_TRACE" --framework_name="Caffe" --framework_version="1.0" --batch_size 64
#python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FRAMEWORK_TRACE" --framework_name="Caffe" --framework_version="1.0" --batch_size 64
# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FULL_TRACE" --framework_name="Caffe" --framework_version="1.0" --batch_size 64

# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="STEP_TRACE" --framework_name="Caffe2" --framework_version="0.8.1" --batch_size 64
python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FRAMEWORK_TRACE" --framework_name="Caffe2" --framework_version="0.8.1" --batch_size 64
# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FULL_TRACE" --framework_name="Caffe2" --framework_version="0.8.1" --batch_size 64

# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="STEP_TRACE" --framework_name="TensorRT" --framework_version="2.1.2" --batch_size 64
#python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FRAMEWORK_TRACE" --framework_name="TensorRT" --framework_version="2.1.2" --batch_size 64
# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FULL_TRACE" --framework_name="TensorRT" --framework_version="2.1.2" --batch_size 64

# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="STEP_TRACE" --framework_name="TensorFlow" --framework_version="1.4" --batch_size 64
#python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FRAMEWORK_TRACE" --framework_name="TensorFlow" --framework_version="1.4" --batch_size 64
# python cli.py --carml_url http://34.229.181.50:8088/ --trace_url http://52.91.29.125 --urls example.txt --trace_level="FULL_TRACE" --framework_name="TensorFlow" --framework_version="1.4" --batch_size 64
