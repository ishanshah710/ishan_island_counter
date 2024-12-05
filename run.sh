#!/bin/bash
# Shell script to build and run the solution using Docker

set -e  # Exit on errors

# Build the Docker image and supressing the docker related output
docker build -t island-counter . > /dev/null 2>&1

# Run the container with the input file
docker run --rm -v $(pwd):/app island-counter python3 main.py "$1"
