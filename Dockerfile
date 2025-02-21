FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all the files from the current directory to the /app folder in the container
COPY . .

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
