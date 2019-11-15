#!/bin/sh
# start API server for image classification

python -m uvicorn src.api_classifier:app --reload
