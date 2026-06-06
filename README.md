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
├── backend/
|   |--Dockerfile            #
│   ├── app.py               # FastAPI application + endpoints
│   ├── model.py             # HuggingFace model loading + inference
│   ├── schemas.py           # Pydantic request/response models
│   ├── test_model.py        # Model testing script
│   └── requirements.txt
│
├── frontend/
│   ├── index.html           # UI interface
│   ├── style.css            # Dark theme styling
│   └── script.js            # API calls + result rendering
│
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
## 🐳 Docker

```bash
cd backend
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

### 4. Run the API
```bash
uvicorn app:app --reload
```

### 5. Open frontend
Open `frontend/index.html` in your browser.

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
