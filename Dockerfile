# Use the official Python 3 image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy the application code to the working directory
COPY score.py score1.py scores.txt utils.py main_score.py .

# Expose the port the app runs on (optional)
#EXPOSE 8000

# Command to run the application
CMD ["python3", "main_score.py"]

