FROM python:3.10-slim

WORKDIR /app

# Copie et installe les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie le code dans l'image
COPY . .

CMD ["python", "main.py"]
