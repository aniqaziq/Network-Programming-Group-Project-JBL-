FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY collect_metrics.py .

CMD ["python", "collect_metrics.py"]
