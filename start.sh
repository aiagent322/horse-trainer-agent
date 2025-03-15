#!/bin/bash
cd /opt/render/project/src  # Change to the Render project folder
source ~/.zshrc  # Load API keys
source venv/bin/activate  # Activate virtual environment (if used)
python3 main.py  # Run AI agent

