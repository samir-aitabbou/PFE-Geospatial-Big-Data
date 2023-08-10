# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN mkdir -p /app/Django_Backend_Project/

RUN mkdir -p /app/
# Copy the Django project into the container
COPY Django_Backend_Project /app/

RUN cd Django_Backend_Project

# Copy the Django app into the container         
# COPY spark_app/ /app/spark_app/

# Set the default command to start the Django development server
CMD ["python3", "Django_Backend_Project/manage.py", "runserver", "0.0.0.0:8000"]

# /home/samir/Big_Data/PFE-Geospatial-Big-Data/backend/Django_Backend_Project