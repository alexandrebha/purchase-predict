FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements-api.txt ./
RUN uv pip install --system -r requirements-api.txt

COPY app.py ./
COPY data/06_model/model.pkl data/06_model/model.pkl
COPY data/04_feature/transform_pipeline.pkl data/04_feature/transform_pipeline.pkl

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
