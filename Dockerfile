# Używamy obrazu Python
FROM python:3.9-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki projektu do kontenera
COPY . /app

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Uruchamiamy aplikację przy pomocy Gunicorna
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
