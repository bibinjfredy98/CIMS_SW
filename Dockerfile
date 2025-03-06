







# Use the official Python slim image
FROM python:3-slim 

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    default-mysql-client \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Give execute permission to wait-for-mysql.sh
RUN chmod +x wait-for-mysql.sh

# Expose the application port
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
