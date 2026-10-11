FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends openjdk-21-jre-headless && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir mpxj JPype1
WORKDIR /app
COPY server.py .
RUN useradd -r -u 10001 app
USER app
EXPOSE 8080
CMD ["python", "server.py"]
