FROM python:3.9-slim-buster

WORKDIR /app

COPY ./dependencies/requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./src/app.py .
COPY ./data/counter.txt .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]