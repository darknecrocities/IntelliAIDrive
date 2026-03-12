#!/bin/bash

echo "🚀 Starting IntelliDrive AI: Full-Stack Neural System"

# Check for dataset
if [ ! -f "data/video.mp4" ]; then
    echo "⚠️ Warning: data/video.mp4 not found. Video feed will show loading state."
fi

# Install backend dependencies
echo "📦 Installing backend dependencies..."
pip3 install -r requirements.txt

# Setup Frontend
echo "⚛️ Preparing React Frontend..."
cd frontend/react-app
if [ ! -d "node_modules" ]; then
    npm install
fi

# Function to kill background processes on exit
cleanup() {
    echo "🛑 Shutting down IntelliDrive AI..."
    kill $BACKEND_PID $FRONTEND_PID
    exit
}
trap cleanup SIGINT

# Start Backend Server
echo "🌐 Launching FastAPI Backend on http://localhost:8000"
python3 ../../src/main.py &
BACKEND_PID=$!

# Start Frontend
echo "💻 Launching React Dashboard..."
npm run dev 

echo "✅ System initialized. Press Ctrl+C to stop."
wait
