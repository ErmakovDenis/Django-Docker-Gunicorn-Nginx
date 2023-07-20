# Pull official base Python Docker image
FROM python:3.10.6


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1



# Set work directory
WORKDIR /code


# Install dependencies
RUN pip install --upgrade pip
COPY ../../requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt install -y netcat

# Copy the Django project
COPY ../.. /code/

ENTRYPOINT ["/code/entrypoint.sh"]