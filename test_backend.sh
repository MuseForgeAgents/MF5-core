#!/bin/bash
# Run pytest and log output to pytest.log
cd backend
pytest tests/ | tee pytest.log
