# Utiliser une image Python de base
FROM python:3.9-slim

# Créer un répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY requirements.txt /app/
COPY app.py /app/
COPY Airline_Passenger_Satisfaction_model.joblib  /app/
# Installer les dépendances
RUN pip install -r requirements.txt

EXPOSE 80

# Commande pour démarrer Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
