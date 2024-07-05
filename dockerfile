# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim

# Set working directory di container
WORKDIR /app

# Copy file requirements.txt ke working directory
COPY requirements.txt .

# Install dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode aplikasi ke working directory
COPY . .

# Expose port yang akan digunakan oleh aplikasi
EXPOSE 8080

# Menjalankan aplikasi
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]