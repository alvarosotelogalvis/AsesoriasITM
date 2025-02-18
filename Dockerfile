FROM python:3.11-slim

WORKDIR /app

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application's port
EXPOSE 5000

# Variables
ENV FLASK_APP=project/shared/config/app.py

# Command to run the Flask application using Uvicorn
CMD ["python", "-m", "project.shared.config.app", "host=0.0.0.0"]