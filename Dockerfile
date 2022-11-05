FROM python:latest
WORKDIR /app
COPY . /app/
RUN python -u calculator.py
