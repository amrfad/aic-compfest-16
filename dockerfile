FROM gcr.io/cloudsql-docker/gce-proxy:latest AS cloudsql-proxy

# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim

# Copy the Cloud SQL Proxy binary
COPY --from=cloudsql-proxy /cloud_sql_proxy /cloud_sql_proxy

# Set working directory di container
WORKDIR /app

# Copy file requirements.txt ke working directory
COPY requirements.txt .

# Install dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Menginstall dependensi PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy seluruh kode aplikasi ke working directory
COPY . .

# Expose port yang akan digunakan oleh aplikasi
EXPOSE 8080

# Menjalankan aplikasi
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app
CMD /cloud_sql_proxy -instances=digitalentum-project:asia-southeast2:digitalentum-db=tcp:5432 & python run.py