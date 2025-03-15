#!/bin/bash
cd /opt/render/project/src || exit
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-7860}


