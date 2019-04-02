#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR

jupyter-notebook --allow-root --no-browser -y --port=8888 --ip=0.0.0.0 
