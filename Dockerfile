FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip
RUN apt install python3-dev libpq-dev nginx -y

# Set up Python environment and install Django and other dependencies
RUN pip install django gunicorn psycopg2

# Copy requirements.txt and install additional Python packages
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire project to the /app directory
ADD . /app

# Set the working directory
WORKDIR /app

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Command to run the Gunicorn server
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangokubernetesproject.wsgi"]
