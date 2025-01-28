#!/bin/bash

# Vérifier si Flask-Migrate est installé
if ! pip show flask-migrate > /dev/null 2>&1; then
    echo "Flask-Migrate n'est pas installé. Installation en cours..."
    pip install flask-migrate
fi

# Créer une migration
echo "Génération d'une migration pour les modifications du modèle..."
flask db migrate -m "Update models"

# Appliquer la migration
echo "Application des migrations..."
flask db upgrade

# Optionnel : Réinitialiser la base de données (détruire puis recréer les tables)
read -p "Souhaitez-vous réinitialiser la base de données ? Toutes les données seront perdues ! (y/n): " choice
if [ "$choice" == "y" ]; then
    echo "Réinitialisation de la base de données..."
    flask shell <<EOF
from your_app import db
db.drop_all()  # Supprimer toutes les tables
db.create_all()  # Créer toutes les tables
EOF
    echo "Base de données réinitialisée et tables recréées."
fi

echo "Script terminé avec succès."
