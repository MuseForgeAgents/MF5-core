#!/bin/bash
# Run MuseForge backend and log output to server.log
export PYTHONPATH=.
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000 | tee server.log
