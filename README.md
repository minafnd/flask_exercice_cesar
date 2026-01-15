# Flask Exercice César

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-✓-brightgreen)

Exercice réalisé dans le cadre d'un cours **Flask**, consistant à créer une application web pour le **(dé)chiffrement de message avec le code César**, avec Docker et Nginx.

---

## 🚀 Fonctionnalités

- Chiffrement et déchiffrement de texte avec le code César
- Interface web simple avec Flask
- Stockage des données via SQLite
- Déploiement via Docker & Docker Compose (BDD mySQL)
- Reverse proxy avec Nginx

---

## 📁 Structure du projet

```

app.py           # Application Flask principale
cesar.py         # Logique de chiffrement César
templates/       # Fichiers HTML
static/          # CSS et ressources statiques
Dockerfile       # Image Docker de l'application
docker-compose.yml # Orchestration services (web + DB)
nginx/           # Configuration Nginx
requirements.txt # Dépendances Python
site.db          # Base SQLite

````

---

## ⚡ Installation & lancement

### Cloner le dépôt
```bash
git clone https://github.com/minafnd/flask_exercice_cesar.git
cd flask_exercice_cesar
````

### Local (optionnel)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py
```

### Avec Docker

```bash
docker-compose up --build
```

Accès : [http://localhost:8097](http://localhost:8097)

---

## 📝 Auteur

Exercice réalisé par moi-même pour un cours Flask.
