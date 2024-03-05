# Use an official Python runtime as a parent image
FROM python:3.12

ARG APP_HOME=/home/app

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR ${APP_HOME}

# Install dependencies
COPY backend/requirements.txt backend/
RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Collect static files

WORKDIR /home/app/backend/src/

# Execute entrypoint script
ENTRYPOINT ["/bin/bash","/home/app/docker/entrypoint.sh"]
