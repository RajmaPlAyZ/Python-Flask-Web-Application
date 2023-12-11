# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install Flask

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Define environment variable
ENV FLASK_APP=main.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]
