FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY score.py score1.py scores.txt utils.py main_score.py .

CMD ["python3", "main_score.py"]

