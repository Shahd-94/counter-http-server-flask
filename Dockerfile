FROM python:3.9

WORKDIR /app

COPY dependencies/requirements.txt .
RUN pip install -r requirements.txt

COPY src/app.py .
COPY data/counter.txt .

CMD ["python", "app.py"]