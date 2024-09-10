FROM python:3.12.2

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir -r /code/requirements.txt

# Copy the rest of the application code
COPY ./app /code/app

# Expose port 8000 for the application
EXPOSE 8000

# Start the Uvicorn server with consistent double quotes
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
