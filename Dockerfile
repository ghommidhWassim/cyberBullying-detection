# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "appcyberBullying:app", "--host", "0.0.0.0", "--port", "8000"]

