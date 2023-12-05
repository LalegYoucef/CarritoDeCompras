# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /CarritoDeCompra

# Copy the current directory contents into the container at /app
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip3 install  -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
