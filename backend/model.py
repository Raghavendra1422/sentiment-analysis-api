from transformers import pipeline

# Load model once when application starts
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def predict_sentiment(text: str):
    result = classifier(text)

    return {
        "label": result[0]["label"],
        "score": float(result[0]["score"])
    }