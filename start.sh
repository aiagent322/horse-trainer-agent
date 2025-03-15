#!/bin/bash
cd /opt/render/project/src  # Navigate to the correct directory
source venv/bin/activate  # Activate virtual environment
exec uvicorn main:app --host 0.0.0.0 --port 10000  # Start FastAPI app

