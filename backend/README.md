# MuseForge Backend

This is the backend for the MuseForge (MF5) platform, built with FastAPI. It supports model metadata retrieval, prediction execution, and multi-step pipeline orchestration using Replicate and Hugging Face models.

## 📁 Directory Structure

```
/backend/
├── api/                 # Route handlers
├── services/            # Business logic
├── storage/             # File + schema access
├── schemas/             # Pydantic models
├── middleware/          # Auth + rate limiting
├── utils/               # Logging + error handling
├── tests/               # Unit + integration tests
├── main.py              # FastAPI entrypoint
├── config.py            # Environment config
└── requirements.txt     # Dependencies
```

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file

```env
REPLICATE_API_TOKEN=your_replicate_token
HUGGINGFACE_API_TOKEN=your_hf_token
DATABASE_URL=sqlite:///./mf5.db
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=3600
```

### 3. Run the server

```bash
uvicorn backend.main:app --reload
```

## ✅ Tests

```bash
pytest backend/tests/
```

## 🔌 API Overview

- `GET /` – Health check
- `GET /models` – List stored models
- `POST /models/{id}/predict` – Run model prediction
- `POST /pipelines/{id}/execute` – Execute pipeline
- `POST /replicate/models/sync` – Sync from Replicate
- `POST /huggingface/models/sync` – Sync from Hugging Face

---

Developed for MuseForge MF5.
