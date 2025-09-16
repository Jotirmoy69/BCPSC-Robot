# Blue AI Robot
This is a Raspberry Pi 5 robot project called Blue AI.

## Features
- Bilingual conversation (English + Bangla)
- Local AI model for Q&A using Naive Bayes
- Face recognition for special persons
- Person detection
- Voice input/output
- Motor control
- Optional external AI API integration

## Setup
1. Install dependencies:
   ```
   pip3 install -r requirements.txt
   sudo apt install libatlas-base-dev liblapack-dev cmake libx11-dev
   ```
2. Train the conversation models:
   ```
   python3 src/ai_conversation.py
   ```
3. Run the robot:
   ```
   python3 src/main.py
   ```
