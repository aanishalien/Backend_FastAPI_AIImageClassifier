# 🧠 Backend_FastAPI_AIImageClassifier

## 🖼️ AI Image Classifier API

This is a backend project built with **FastAPI** that serves an AI-powered image classification model. It takes image input and returns predicted class labels.


## 🚀 Features

- 🧠 AI model for image classification
- 📦 REST API built using FastAPI
- 🔄 Real-time image prediction
- 🌐 Supabase integration for environment configuration
- ✅ Easily extensible with new classes or model improvements


## 📁 Project Structure

Backend_FastAPI_AIImageClassifier/
├── main.py # FastAPI entry point
├── model_loader.py # PyTorch model loading
├── predict.py # Prediction logic
├── supabase_client.py # (If used for auth/data)
├── .env # Environment variables
├── requirements.txt
└── README.md


## 🛠️ Environment Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
📦 Installed Packages
🔹 FastAPI & Server
pip install "fastapi[standard]"
pip install "uvicorn[standard]"
🔹 Environment Management (with Supabase)
pip install pydantic-settings
🔹 AI Image Classification (PyTorch, Transformers)
pip install python-multipart pillow
pip install torch torchvision transformers
▶️ Run the FastAPI Server
uvicorn main:app --host 0.0.0.0 --port 8000
