# Utiliser une image de base Python
FROM python:3.8-slim
# Définir le répertoire de travail 
WORKDIR /app 
# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt 
# Installer les dépendances
RUN pip install -r requirements.txt 
# Copier le fichier de l'application 
COPY app.py app.py 
# Définir la commande par défaut 
CMD ["python", "app.py"]
