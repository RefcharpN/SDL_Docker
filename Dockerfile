FROM python:3.10.13-slim-bullseye

WORKDIR /app

RUN mkdir -p /app/templates

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .

COPY index.html /app/templates/

CMD ["python3", "app.py"]

