# 🤗 Sentiment Analysis API

A production-ready Sentiment Analysis REST API built with **HuggingFace Transformers** and **FastAPI** — demonstrates real-world usage of pretrained NLP models without training from scratch.

---

## 🧠 Problem Statement

Businesses need to understand customer sentiment at scale:
- Product reviews, support tickets, social media comments
- Manual reading is impossible at volume
- Training custom NLP models requires massive datasets and GPUs

**HuggingFace solves this** — pretrained models like DistilBERT are ready to use immediately, with state-of-the-art accuracy.

---

## ✅ Solution — Pretrained NLP Model as a REST API

```
User Input (text)
      ↓
FastAPI Endpoint
      ↓
Pydantic Validation
      ↓
HuggingFace DistilBERT Pipeline
      ↓
Tokenization → Embeddings → Attention → Classification
      ↓
JSON Response (label + confidence score)
```

---

## 🏗️ Project Structure

```
sentiment-analysis-api/
│
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD pipeline
│
├── backend/
│   ├── app.py               # FastAPI application + endpoints
│   ├── model.py             # HuggingFace model loading + inference
│   ├── schemas.py           # Pydantic request/response models
│   ├── test_api.py          # Automated pytest test suite (7 tests)
│   ├── test_model.py        # Model testing script
│   ├── Dockerfile           # Docker container configuration
│   ├── .dockerignore        # Files excluded from Docker build
│   └── requirements.txt     # Python dependencies
│
├── frontend/
│   ├── index.html           # UI interface
│   ├── style.css            # Dark theme styling
│   └── script.js            # API calls + result rendering
│
├── docker-compose.yml       # Docker Compose configuration
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| NLP Model | **HuggingFace DistilBERT** | Pretrained sentiment classification |
| API Framework | **FastAPI** | REST API with auto Swagger docs |
| Validation | **Pydantic** | Request/response schema validation |
| Server | **Uvicorn** | ASGI server for FastAPI |
| Frontend | **HTML + CSS + JS** | Interactive UI |
| Container | **Docker** | Portable containerized deployment |
| Orchestration | **Docker Compose** | Multi-container management |
| Testing | **pytest** | Automated API test suite |
| CI/CD | **GitHub Actions** | Auto test + build on every push |

---

## 🤖 Model Details

```
distilbert-base-uncased-finetuned-sst-2-english
```

| Part | Meaning |
|---|---|
| DistilBERT | Compressed version of BERT — 40% smaller, 60% faster |
| Base | Standard model size |
| Uncased | Ignores capitalization |
| Fine-tuned | Pre-trained specifically for sentiment |
| SST-2 | Stanford Sentiment Treebank dataset |
| English | English language model |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Raghavendra1422/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Create virtual environment
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
uvicorn app:app --reload
```

### 5. Open frontend
Open `frontend/index.html` in your browser.

---

## 🐳 Docker & CI/CD

### Run with Docker
```bash
docker build -t sentiment-api ./backend
docker run -p 8000:8000 sentiment-api
```

### Run with docker-compose (recommended)
```bash
docker compose up
```

### Run Tests
```bash
cd backend
pytest test_api.py -v
```

### CI/CD Pipeline
Every push to `master` automatically:
- Runs all 7 pytest tests on Ubuntu
- Builds the Docker image
- Shows ✅ green badge if everything passes

<details>
<summary><b>CI/CD Pipeline Steps — Click to expand</b></summary>

```
Push code to GitHub
        ↓
GitHub Actions triggers automatically
        ↓
Step 1: Checkout code on Ubuntu machine
        ↓
Step 2: Install Python 3.11
        ↓
Step 3: Install all dependencies (CPU-only torch)
        ↓
Step 4: Run pytest test_api.py -v (7 tests)
        ↓
Step 5: Build Docker image
        ↓
✅ Green badge — all good!
❌ Red badge — something broke, fix before deploying
```

</details>

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/predict` | Single text sentiment |
| POST | `/predict/batch` | Multiple texts at once |

### Single Prediction

**Request:**
```json
{
  "text": "I love this product, it is amazing!"
}
```

**Response:**
```json
{
  "text": "I love this product, it is amazing!",
  "prediction": {
    "label": "POSITIVE",
    "score": 0.9998
  }
}
```

### Batch Prediction

**Request:**
```json
{
  "texts": [
    "I love this product",
    "Worst experience ever",
    "Pretty good overall"
  ]
}
```

**Response:**
```json
{
  "total": 3,
  "results": [
    {"text": "I love this product", "prediction": {"label": "POSITIVE", "score": 0.9998}},
    {"text": "Worst experience ever", "prediction": {"label": "NEGATIVE", "score": 0.9997}},
    {"text": "Pretty good overall", "prediction": {"label": "POSITIVE", "score": 0.9986}}
  ]
}
```

---

## 💡 Key Concepts Demonstrated

- **HuggingFace Transformers** — loading and running pretrained models locally
- **Transfer Learning** — using a model pre-trained on millions of examples
- **Tokenization** — converting text to token IDs the model understands
- **Embeddings** — tokens converted to numerical vectors
- **Attention Mechanism** — model understands context ("not bad" = positive)
- **FastAPI** — production REST API with automatic Swagger documentation
- **Batch Processing** — analyzing multiple texts in one API call
- **Docker** — containerized deployment for consistent environments
- **pytest** — automated test suite with 7 tests covering all endpoints
- **GitHub Actions** — CI/CD pipeline that runs on every push

---

## 🧪 Test Results

| Input | Label | Confidence |
|---|---|---|
| "I love this product" | POSITIVE | 100.0% |
| "Worst experience ever" | NEGATIVE | 100.0% |
| "the phone is not bad worth the price" | POSITIVE | 99.8% |
| "this is not quality worth product" | NEGATIVE | 100.0% |

Note: The model correctly handles negation — "not bad" → POSITIVE, showing the attention mechanism understanding context.

---

## 📈 Future Improvements

- [ ] Add multilingual sentiment support
- [ ] Add emotion detection (joy, anger, fear, sadness)
- [ ] Deploy to HuggingFace Spaces
- [ ] Add model comparison (BERT vs DistilBERT vs RoBERTa)
- [ ] Add RAGAS evaluation pipeline

---

## 🔗 Swagger Documentation

Once running, visit:
```
http://127.0.0.1:8000/docs
```

---

## 👤 Author

**Chelimela Raghavendra Goud**
- GitHub: [@Raghavendra1422](https://github.com/Raghavendra1422)
- LinkedIn: [raghavendra1422](https://linkedin.com/in/raghavendra1422)
