# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /ogrenci_service

# Set the working directory to /music_service
WORKDIR /ogrenci_service

# Copy the current directory contents into the container at /music_service
ADD . /ogrenci_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver","0.0.0.0:8000"]
