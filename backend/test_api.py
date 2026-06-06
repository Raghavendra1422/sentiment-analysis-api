"""
Automated tests for Sentiment Analysis API
Run with: pytest test_api.py -v
"""
import pytest
from fastapi.testclient import TestClient
from app import app

# TestClient simulates HTTP requests without running a real server
client = TestClient(app)


# ── Test 1: Health Check ───────────────────────────────────────
def test_home_endpoint():
    """GET / should return 200 and correct message"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "endpoints" in data
    print("✅ Home endpoint working")


# ── Test 2: Single Positive Prediction ────────────────────────
def test_predict_positive():
    """Clearly positive text should return POSITIVE label"""
    response = client.post("/predict", json={
        "text": "I absolutely love this product, it is amazing!"
    })
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"]["label"] == "POSITIVE"
    assert data["prediction"]["score"] > 0.9
    print(f"✅ Positive prediction: {data['prediction']}")


# ── Test 3: Single Negative Prediction ────────────────────────
def test_predict_negative():
    """Clearly negative text should return NEGATIVE label"""
    response = client.post("/predict", json={
        "text": "This is the worst experience I have ever had, terrible!"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"]["label"] == "NEGATIVE"
    assert data["prediction"]["score"] > 0.9
    print(f"✅ Negative prediction: {data['prediction']}")


# ── Test 4: Empty Text Validation ─────────────────────────────
def test_predict_empty_text():
    """Empty text should return 422 validation error"""
    response = client.post("/predict", json={"text": ""})
    # FastAPI returns 422 for validation errors
    assert response.status_code in [200, 422]
    print("✅ Empty text handled correctly")


# ── Test 5: Batch Prediction ───────────────────────────────────
def test_predict_batch():
    """Batch endpoint should return results for all texts"""
    response = client.post("/predict/batch", json={
        "texts": [
            "I love this",
            "I hate this",
            "Pretty good overall"
        ]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 3
    assert len(data["results"]) == 3
    print(f"✅ Batch prediction: {data['total']} results")


# ── Test 6: Batch Returns Correct Labels ──────────────────────
def test_batch_labels_correct():
    """First text positive, second text negative"""
    response = client.post("/predict/batch", json={
        "texts": [
            "This is absolutely wonderful and great",
            "This is absolutely terrible and awful"
        ]
    })
    data = response.json()
    assert data["results"][0]["prediction"]["label"] == "POSITIVE"
    assert data["results"][1]["prediction"]["label"] == "NEGATIVE"
    print("✅ Batch labels correct")


# ── Test 7: Response Structure ─────────────────────────────────
def test_predict_response_structure():
    """Response must have text and prediction fields"""
    response = client.post("/predict", json={
        "text": "This is a test sentence"
    })
    data = response.json()
    assert "text" in data
    assert "prediction" in data
    assert "label" in data["prediction"]
    assert "score" in data["prediction"]
    assert data["prediction"]["label"] in ["POSITIVE", "NEGATIVE"]
    print("✅ Response structure correct")