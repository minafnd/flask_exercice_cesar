# image de base à utiliser
FROM python:3.14-slim
# définir le répertoire de travail dans le conteneur
WORKDIR /app

# copier l'app à l'intérieur du conteneur
COPY . .

# installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# exposer le port 8000
EXPOSE 8000

# docker va lancer la commande qui va générer les workers qui vont gérer les requêtes
CMD ["gunicorn", "w", "2", "-b", "0.0.0.0.8000", "app:app"]