# Dockerfile

FROM python:3.10-slim

# Prevents Python from writing pyc files to disk and buffers stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . /app/

# Run migrations and collect static files
RUN python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput

# Set environment variables for the admin user
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin123

# Create the superuser non-interactively
RUN python manage.py createsuperuser --noinput || true

# Expose port 8000
EXPOSE 8000

# Run gunicorn server
CMD ["gunicorn", "tech_test.wsgi:application", "--bind", "0.0.0.0:8000"]
