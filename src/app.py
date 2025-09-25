"""
Platform Engineering Flask Application

Cette application Flask démontre les bonnes pratiques de Platform Engineering
avec une API REST simple comprenant des endpoints de santé et de détails.

Auteur: Diags
Version: 1.0.0
"""

import os
from datetime import datetime
from flask import Flask, jsonify

# Configuration de l'application Flask. __name__ est le nom du module ou du package.
app = Flask(__name__)

# Configuration des variables d'environnement
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Métadonnées de l'application
APP_VERSION = "1.0.0"
APP_NAME = "Platform Engineering API"


@app.route('/')
def home():
    """
    Endpoint racine - Page d'accueil de l'API
    
    Retourne les informations générales sur l'API et la liste des endpoints disponibles.
    Utilisé comme point d'entrée pour découvrir l'API.
    
    Returns:
        JSON: Informations sur l'API et liste des endpoints
    """
    return jsonify({
        "message": f"Welcome to {APP_NAME}",
        "version": APP_VERSION,
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "health": "/api/v1/health",
            "details": "/api/v1/details"
        },
        "documentation": {
            "description": "API REST pour démontrer les bonnes pratiques de Platform Engineering",
            "technologies": ["Python", "Flask", "Docker", "Kubernetes", "Helm", "ArgoCD"]
        }
    })


@app.route('/api/v1/health')
def health():
    """
    Endpoint de santé - Health Check
    
    Utilisé par Kubernetes pour les probes de liveness et readiness.
    Retourne le statut de santé de l'application.
    
    Returns:
        JSON: Statut de santé avec code HTTP 200
    """
    return jsonify({
        "status": "up",
        "message": "The service is running",
        "timestamp": datetime.now().isoformat(),
        "version": APP_VERSION,
        "checks": {
            "database": "ok",
            "memory": "ok",
            "disk": "ok"
        }
    }), 200


@app.route('/api/v1/details')
def details():
    """
    Endpoint de détails - Informations détaillées
    
    Retourne des informations détaillées sur l'application et l'environnement.
    Utilisé pour démontrer la structure des réponses JSON.
    
    Returns:
        JSON: Informations détaillées sur l'application
    """
    return jsonify({
        "application": {
            "name": APP_NAME,
            "version": APP_VERSION,
            "environment": os.getenv('FLASK_ENV', 'production'),
            "python_version": os.sys.version,
            "hostname": os.getenv('HOSTNAME', 'localhost')
        },
        "user": {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com",
            "role": "Platform Engineer"
        },
        "system": {
            "timestamp": datetime.now().isoformat(),
            "uptime": "N/A",  # Dans un vrai système, on calculerait l'uptime
            "memory_usage": "N/A"  # Dans un vrai système, on récupérerait l'usage mémoire
        }
    })


@app.errorhandler(404)
def not_found(error):
    """
    Gestionnaire d'erreur 404 - Page non trouvée
    
    Args:
        error: L'erreur 404 générée par Flask
        
    Returns:
        JSON: Message d'erreur avec code HTTP 404
    """
    return jsonify({
        "error": "Not Found",
        "message": "The requested endpoint was not found",
        "status_code": 404,
        "timestamp": datetime.now().isoformat()
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Gestionnaire d'erreur 500 - Erreur interne du serveur
    
    Args:
        error: L'erreur 500 générée par Flask
        
    Returns:
        JSON: Message d'erreur avec code HTTP 500
    """
    return jsonify({
        "error": "Internal Server Error",
        "message": "An internal server error occurred",
        "status_code": 500,
        "timestamp": datetime.now().isoformat()
    }), 500


if __name__ == '__main__':
    """
    Point d'entrée principal de l'application
    
    Démarre le serveur Flask en mode développement ou production
    selon les variables d'environnement.
    """
    # Configuration du serveur
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'production') == 'development'
    
    print(f"Starting {APP_NAME} v{APP_VERSION}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'production')}")
    print(f"Debug mode: {debug}")
    print(f"Server running on http://{host}:{port}")
    
    # Démarrage du serveur Flask
    app.run(
        host=host,
        port=port,
        debug=debug
    )