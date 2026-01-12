# Django App Suivi - Application de Suivi de Collecte

Application web Django complète pour le suivi et la gestion des opérations de collecte avec authentification, tableaux de bord interactifs et exportation de données.

## 🚀 Fonctionnalités

### Authentification
- ✅ Système d'authentification pour **Administrateurs** et **Commerciaux**
- ✅ Gestion des rôles et permissions
- ✅ Page de profil avec modification des informations

### Pages Principales (Sidebar)

#### 1. Tableau de Bord
- Vue d'ensemble avec statistiques clés (opérations totales, clients, montants)
- Graphiques interactifs :
  - Évolution des montants sur 6 mois (graphique linéaire)
  - Répartition des opérations par type (graphique en anneau)
- Tableau des opérations récentes

#### 2. Nouvelle Opération
- Formulaire de création d'opération
- Sélection du client
- Types d'opération : Collecte, Dépôt, Retrait
- Gestion des montants et statuts

#### 3. Suivi Collecte
- Navigation par onglets :
  - **Hebdomadaire** : Opérations de la semaine en cours
  - **Mensuel** : Opérations du mois en cours
  - **Annuel** : Opérations de l'année en cours
  - **Historique** : Toutes les opérations
- Statistiques par période (nombre et montant total)
- Tableau détaillé des opérations

#### 4. Suivi Client
- Liste complète des clients avec recherche et filtres
- Informations clients :
  - Nom & Prénom
  - Email & Téléphone
  - Type (A, B, C)
  - Commercial assigné
  - Statistiques (nombre d'opérations, montant total)
- Page de détail par client avec historique des opérations

#### 5. Centre d'Exportation
- Export des opérations au format CSV
- Export des clients au format CSV
- Compatible avec Excel, Google Sheets, etc.

### Top Bar

#### Notifications
- Système de notifications en temps réel
- Badge avec compteur de notifications non lues
- Dropdown avec les 5 dernières notifications

#### Profil
- Accès rapide aux informations du profil
- Modification des informations personnelles
- Photo de profil
- Déconnexion

## 📋 Données Clients

L'application gère les informations suivantes pour chaque client :
- **Nom & Prénom**
- **Historique des opérations** par client
- **Type** (A, B, C) pour segmentation
- **Email**
- **Téléphone**
- **Commercial assigné**

## 🛠 Technologies Utilisées

- **Backend** : Django 4.2.9
- **Base de données** : PostgreSQL (avec fallback SQLite pour développement)
- **Frontend** : Bootstrap 5.1.3
- **Graphiques** : Chart.js 3.7.0
- **Icons** : Bootstrap Icons
- **Forms** : django-crispy-forms avec Bootstrap 4

## 📦 Installation

### Prérequis
- Python 3.8+
- PostgreSQL (optionnel, SQLite utilisé par défaut)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/DylaneTrader/django-app-suivi.git
cd django-app-suivi
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations**
```bash
python manage.py migrate
```

5. **Générer les données fictives**
```bash
python manage.py generate_fixtures
```

6. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

7. **Accéder à l'application**
Ouvrez votre navigateur et allez sur : `http://localhost:8000/login/`

## 🔐 Comptes de Test

Après avoir exécuté `generate_fixtures`, les comptes suivants sont disponibles :

- **Admin**
  - Username: `admin`
  - Password: `admin123`

- **Commercial 1**
  - Username: `commercial1`
  - Password: `commercial123`

- **Commercial 2**
  - Username: `commercial2`
  - Password: `commercial123`

## 🗄️ Configuration PostgreSQL (Optionnel)

Pour utiliser PostgreSQL au lieu de SQLite :

1. **Créer un fichier `.env`** à la racine du projet :
```env
USE_POSTGRES=True
DB_NAME=suivi_collecte
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

2. **Créer la base de données PostgreSQL**
```bash
createdb suivi_collecte
```

3. **Appliquer les migrations**
```bash
python manage.py migrate
python manage.py generate_fixtures
```

## 📁 Structure du Projet

```
django-app-suivi/
├── accounts/              # Gestion des utilisateurs et authentification
├── clients/               # Gestion des clients
├── dashboard/             # Tableau de bord
├── operations/            # Gestion des opérations
├── exports/               # Exportation de données
├── templates/             # Templates HTML
│   ├── base.html
│   ├── accounts/
│   ├── clients/
│   ├── dashboard/
│   ├── operations/
│   └── exports/
├── suivi_collecte/        # Configuration Django
├── manage.py
└── requirements.txt
```

## 🎨 Captures d'Écran

L'application dispose d'une interface moderne et responsive avec :
- Sidebar de navigation fixe
- Top bar avec notifications et profil
- Tableaux de données interactifs
- Graphiques dynamiques
- Design cohérent avec Bootstrap

## 🔧 Commandes Utiles

### Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### Accéder à l'admin Django
URL : `http://localhost:8000/admin/`

### Régénérer les données de test
```bash
python manage.py generate_fixtures
```

### Collecter les fichiers statiques (production)
```bash
python manage.py collectstatic
```

## 📊 Modèles de Données

### User (Custom)
- Hérite de AbstractUser
- Champs additionnels : role, phone, profile_picture

### Client
- nom, prenom, email, telephone
- type_client (A, B, C)
- commercial (ForeignKey vers User)

### Operation
- client (ForeignKey)
- type_operation (collecte, depot, retrait)
- montant, status, description
- date_operation, created_by

### Notification
- user (ForeignKey)
- title, message
- is_read, created_at

## 🌐 Déploiement

Pour déployer en production :

1. Définir `DEBUG = False` dans settings.py
2. Configurer `ALLOWED_HOSTS`
3. Utiliser PostgreSQL
4. Configurer un serveur web (nginx + gunicorn)
5. Collecter les fichiers statiques
6. Configurer HTTPS

## 📝 Licence

Ce projet est un exemple de démonstration créé pour illustrer une application Django complète.

## 👥 Contributeurs

- Application développée avec Django et Bootstrap
- Graphiques avec Chart.js

## 🆘 Support

Pour toute question ou problème, créez une issue sur GitHub.