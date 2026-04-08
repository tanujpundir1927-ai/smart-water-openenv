# Smart Water Management (OpenEnv)

An OpenEnv-compliant RL environment for smart water management.

## Features
- Real-world simulation
- 3 difficulty levels
- Reward system (0.0–1.0)
- API: reset(), step(), state()

## Run
docker build -t water-env .
docker run -p 8000:8000 water-env

## Inference
python inference.py
