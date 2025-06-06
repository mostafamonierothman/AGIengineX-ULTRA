# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (not strictly needed for HF Spaces but good practice)
EXPOSE 7860

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
