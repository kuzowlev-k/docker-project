FROM python:3.11-slim

RUN pip install flask pytz

COPY app /app

WORKDIR /app

CMD ["python3", "app.py"]
