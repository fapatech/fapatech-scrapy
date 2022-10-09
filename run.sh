#!/bin/bash


source $(pwd)/venv/bin/activate
project_dir=$(pwd)/fapatech/fapatech


python $project_dir/spiders/fapaspider.py

# export PYTHONPATH=$PYTHONPATH:$project_dir/utils
# # export PYTHONPATH=$PYTHONPATH:$(pwd)/fapatech/fapatech

# echo $PYTHONPATH