#!/bin/bash

# Navigate to project directory
cd /Users/harshal/PycharmProjects/PythonProject/Playwright_Pytest_Python

# Activate virtual environment
source venv/bin/activate

# Set PYTHONPATH to include the project directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

echo "Virtual environment activated!"
echo "Project directory: $(pwd)"
echo "Python version: $(python --version)"
