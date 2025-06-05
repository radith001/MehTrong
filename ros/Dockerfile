FROM php:8.1-apache

# Copy semua file ke direktori web container
COPY . /var/www/html/

# Install ekstensi mysqli
RUN docker-php-ext-install mysqli

# Ubah hak akses agar Apache bisa baca semua file
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html
