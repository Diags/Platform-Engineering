# Platform Engineering - Flask Application Dockerfile
# 
# Ce Dockerfile construit une image Docker pour l'application Flask
# de Platform Engineering avec Python 3.11 et les dépendances minimales.

# Utilisation d'une image Python officielle basée sur Debian slim
# pour réduire la taille de l'image finale
FROM python:3.11-slim

# Métadonnées de l'image
LABEL maintainer="Diags <diagsylla@example.com>"
LABEL description="Platform Engineering Flask Application"
LABEL version="1.0.0"

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier requirements.txt vers /tmp pour l'installation des dépendances
# Cette étape est séparée pour optimiser le cache Docker
COPY requirements.txt /tmp

# Installation des dépendances Python
# --no-cache-dir : évite de stocker le cache pip dans l'image
# --upgrade : met à jour pip vers la dernière version
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Copie du code source de l'application dans le conteneur
COPY ./src /src

# Exposition du port 5000 (port par défaut de Flask)
EXPOSE 5000

# Variables d'environnement pour la configuration Flask
ENV FLASK_APP=/src/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/src

# Commande par défaut pour démarrer l'application
# Utilisation de la forme exec pour un meilleur signal handling
CMD ["python", "/src/app.py"]