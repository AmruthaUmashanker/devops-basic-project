FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 5000

# gunicorn is a production-grade server (Flask's built-in one is for dev only)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
