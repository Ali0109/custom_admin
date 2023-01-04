FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /custom_admin_django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
