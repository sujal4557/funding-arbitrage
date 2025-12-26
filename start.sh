#!/bin/bash
set -e

echo "Starting FastAPI..."
uvicorn api:app --host 0.0.0.0 --port 8000 &

sleep 3

echo "Starting Streamlit..."
streamlit run app.py \
  --server.port=$PORT \
  --server.address=0.0.0.0
git config core.autocrlf false

