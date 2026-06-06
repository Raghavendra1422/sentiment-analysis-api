FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir \
    fastapi==0.111.0 \
    "uvicorn[standard]==0.30.0" \
    "torch==2.3.0+cpu" --extra-index-url https://download.pytorch.org/whl/cpu \
    "transformers==4.41.0" \
    "pydantic==2.7.0"

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]