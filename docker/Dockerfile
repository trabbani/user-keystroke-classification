# Use an official Python runtime as a parent image
FROM python:3.8

# Sets the working directory in the Docker container
WORKDIR /app/user-keystroke-classification

# Copies the current directory contents into the Docker container
COPY . .

# Installs any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Installs Jupyter notebook
RUN pip install jupyter

# Installs your package
RUN pip install .

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Make sure the contents of our repo are in the working directory
WORKDIR /app/user-keystroke-classification/notebooks/demo

# The command that will run when the container starts
CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='demo'
