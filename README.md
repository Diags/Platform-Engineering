# Platform Engineering

Une application Flask moderne déployée avec Kubernetes, Helm et ArgoCD pour démontrer les bonnes pratiques de Platform Engineering.

## 🚀 Vue d'ensemble

Ce projet illustre un pipeline CI/CD complet avec :
- **Application Flask** : API REST avec endpoints de santé et détails
- **Docker** : Containerisation de l'application
- **Kubernetes** : Orchestration des conteneurs
- **Helm** : Gestion des déploiements Kubernetes
- **ArgoCD** : Déploiement continu (GitOps)
- **GitHub Actions** : Pipeline CI/CD automatisé

## 📁 Structure du projet

```
Platform-Engineering/
├── src/                    # Code source de l'application Flask
│   └── app.py             # Application principale
├── charts/                # Charts Helm
│   └── platform-engineering/
│       ├── templates/     # Templates Kubernetes
│       └── values.yaml    # Configuration par défaut
├── k8s/                   # Manifests Kubernetes (alternative)
├── .github/workflows/     # GitHub Actions CI/CD
├── Dockerfile            # Configuration Docker
├── requirements.txt      # Dépendances Python
└── README.md            # Cette documentation
```

## 🛠️ Technologies utilisées

- **Backend** : Python 3.11, Flask
- **Containerisation** : Docker
- **Orchestration** : Kubernetes
- **Gestion des déploiements** : Helm
- **GitOps** : ArgoCD
- **CI/CD** : GitHub Actions
- **Ingress** : NGINX Ingress Controller

## 🚀 Démarrage rapide

### Prérequis

- Docker
- Kubernetes (Kind recommandé)
- Helm
- ArgoCD

### Installation locale

1. **Cloner le repository**
   ```bash
   git clone https://github.com/Diags/Platform-Engineering.git
   cd Platform-Engineering
   ```

2. **Construire l'image Docker**
   ```bash
   docker build -t platform-engineering:latest .
   ```

3. **Déployer avec Helm**
   ```bash
   helm install platform-engineering ./charts/platform-engineering
   ```

4. **Accéder à l'application**
   - URL : http://platform-engineering.diagsylla.com
   - Health check : http://platform-engineering.diagsylla.com/api/v1/health
   - Details : http://platform-engineering.diagsylla.com/api/v1/details

## 🔧 Configuration

### Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|---------|
| `FLASK_ENV` | Environnement Flask | `production` |
| `PORT` | Port d'écoute | `5000` |

### Configuration Helm

Les valeurs par défaut sont dans `charts/platform-engineering/values.yaml` :

```yaml
replicaCount: 1
image:
  repository: diagsylla/platform-engineering
  tag: latest
service:
  port: 5000
ingress:
  enabled: true
  hosts:
    - host: platform-engineering.diagsylla.com
```

## 🔄 CI/CD Pipeline

Le pipeline GitHub Actions se déclenche automatiquement lors des modifications dans `src/` :

1. **Checkout** : Récupération du code
2. **Build** : Construction de l'image Docker
3. **Push** : Publication vers Docker Hub
4. **Tag** : Utilisation du SHA court (6 caractères)

### Secrets GitHub requis

- `DOCKERHUB_USERNAME` : Nom d'utilisateur Docker Hub
- `DOCKERHUB_TOKEN` : Token d'accès Docker Hub

## 📊 Monitoring et observabilité

### Endpoints de santé

- **GET /** : Page d'accueil avec informations API
- **GET /api/v1/health** : Statut de santé de l'application
- **GET /api/v1/details** : Informations détaillées

### Logs

```bash
# Logs de l'application
kubectl logs -n platform-engineering deployment/platform-engineering

# Logs de l'ingress
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller
```

## 🚀 Déploiement avec ArgoCD

1. **Installer ArgoCD**
   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

2. **Configurer l'application**
   ```bash
   kubectl apply -f charts/platform-engineering/argocd/values-argo.yaml
   ```

3. **Accéder à ArgoCD**
   - URL : https://argocd.diagsylla.com
   - Utilisateur : `admin`
   - Mot de passe : Récupéré avec `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`

## 🛠️ Développement

### Structure de l'API

```python
@app.route('/')
def home():
    """Page d'accueil avec informations sur l'API"""
    return jsonify({
        "message": "Welcome to Platform Engineering API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/v1/health",
            "details": "/api/v1/details"
        }
    })

@app.route('/api/v1/health')
def health():
    """Endpoint de santé pour les probes Kubernetes"""
    return jsonify({
        "status": "up",
        "message": "The service is running"
    }), 200

@app.route('/api/v1/details')
def details():
    """Endpoint retournant des informations détaillées"""
    return jsonify({
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    })
```

### Tests locaux

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python src/app.py

# Tester les endpoints
curl http://localhost:5000/
curl http://localhost:5000/api/v1/health
curl http://localhost:5000/api/v1/details
```

## 📝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteur

**Diags** - [@Diags](https://github.com/Diags)

## 🙏 Remerciements

- [Flask](https://flask.palletsprojects.com/) - Framework web Python
- [Kubernetes](https://kubernetes.io/) - Orchestration de conteneurs
- [Helm](https://helm.sh/) - Gestionnaire de packages Kubernetes
- [ArgoCD](https://argoproj.github.io/cd/) - Déploiement continu GitOps
