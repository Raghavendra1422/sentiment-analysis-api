from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import SentimentRequest, BatchSentimentRequest
from model import predict_sentiment

app = FastAPI(
    title="Sentiment Analysis API",
    description="HuggingFace DistilBERT Sentiment Analysis using FastAPI",
    version="1.0.0"
)

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API Running",
        "model": "distilbert-base-uncased-finetuned-sst-2-english",
        "endpoints": ["/predict", "/predict/batch", "/docs"]
    }

@app.post("/predict")
def predict(request: SentimentRequest):
    result = predict_sentiment(request.text)
    return {
        "text": request.text,
        "prediction": result
    }

@app.post("/predict/batch")
def predict_batch(request: BatchSentimentRequest):
    results = []
    for text in request.texts:
        prediction = predict_sentiment(text)
        results.append({
            "text": text,
            "prediction": prediction
        })
    return {
        "total": len(results),
        "results": results
    }