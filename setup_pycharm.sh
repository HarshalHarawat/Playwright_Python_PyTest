#!/bin/bash

echo "🔧 Setting up PyCharm project configuration..."

# Navigate to project directory
cd /Users/harshal/PycharmProjects/PythonProject/Playwright_Pytest_Python

# Activate virtual environment
source venv/bin/activate

# Get Python interpreter path
PYTHON_PATH=$(which python)
echo "✅ Python interpreter: $PYTHON_PATH"

# Verify packages
echo "📦 Installed packages:"
pip list | grep -E "(playwright|pytest)"

echo ""
echo "🎯 PyCharm Configuration Steps:"
echo "1. Open PyCharm"
echo "2. File → Open → Select this folder: $(pwd)"
echo "3. Configure interpreter: $PYTHON_PATH"
echo "4. Set test runner to pytest in Settings"
echo ""
echo "✅ Project is ready!"
