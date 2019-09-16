#!/bin/bash

PROTO_PATH="./protos"
PYTHON_OUT="./interface"
GRPC_PYTHON_OUT="./interface"

python3 -m grpc_tools.protoc \
    --proto_path=$PROTO_PATH \
    --python_out=$PYTHON_OUT \
    --grpc_python_out=$GRPC_PYTHON_OUT \
    $PROTO_PATH/*.proto

