#!/usr/bin/env bash

# define output_path
OUTPUT_PATH="./release/"  # must endswith /
packages="jieba"

rm -rf $OUTPUT_PATH && \
  mkdir -p $OUTPUT_PATH && \
  cp -r ../jieba $OUTPUT_PATH && \
  true

pushd $OUTPUT_PATH
  nuitka3 --module --include-module=jieba jieba && rm -rf jieba && rm -f "jieba.pyi" && rm -rf "jieba.build"
popd
