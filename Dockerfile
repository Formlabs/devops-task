# base image that python has installed
FROM python:3.9-slim

WORKDIR /app

# Copying the app files into a container
COPY requirements.txt .
COPY helloapp/ helloapp/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# A command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "helloapp.app:app"]