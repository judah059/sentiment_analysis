FROM python:3.10


# Install build dependencies
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    && apt-get clean


WORKDIR /app

COPY requirements.txt requirements.txt

ENV PYTHONPATH=/app

# Run pip install with GitHub token directly
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000