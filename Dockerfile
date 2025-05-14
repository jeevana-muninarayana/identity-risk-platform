FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ /app/src
COPY model.pkl /app/model.pkl
ENV MODEL_PATH="/app/model.pkl"
CMD ["uvicorn","src.api.app:app","--host","0.0.0.0","--port","8080"]
