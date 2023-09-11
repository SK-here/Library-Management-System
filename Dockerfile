# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the local login.py script to the container
COPY login.py .
COPY Library-Management-Dashboard.py .
COPY library_background.png .
COPY requirements.txt

# Install any necessary dependencies
# For example, if you need MySQL client libraries:
RUN pip install -r requirements.txt

# Command to run the login.py script
CMD ["python", "login.py"]

