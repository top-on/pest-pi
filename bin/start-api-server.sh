#!/bin/sh
# start API server for image classification

python -m uvicorn pest_pi.api_classifier:app --reload
