FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend
WORKDIR /app/backend
COPY requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/backend/