# SparringPartner-api

## Description
SparringPartner est une application serverless conçue pour aider les passionnés de sports de combat à trouver des partenaires de sparring locaux. Elle utilise AWS Lambda pour la logique backend, DynamoDB pour le stockage des données, et AWS API Gateway pour la gestion des requêtes HTTP.

## Fonctionnalités
- **Enregistrement et Authentification des Utilisateurs** : Permet aux utilisateurs de créer un compte et de se connecter.
- **Création et Gestion de Profil** : Les utilisateurs peuvent gérer leurs informations de profil, comme le niveau de compétence et le poids.
- **Recherche de Partenaires de Sparring** : Fonctionnalité pour trouver des partenaires basés sur des critères spécifiques.

## Architecture
Cette application utilise AWS Lambda pour exécuter le code sans serveur, DynamoDB pour stocker les informations des utilisateurs et les données des matchs, et API Gateway pour router les requêtes HTTP vers les fonctions Lambda appropriées.

## Démarrage Rapide

### Prérequis
- AWS CLI installé et configuré.
- Compte AWS avec les permissions nécessaires.

### Installation
1. **Cloner le Repository** :
   ```
   git clone https://github.com/SnowKiss/SparringPartner-api
   ```
2. **Déployer les Fonctions Lambda** :
   - Pour chaque fonction dans le dossier `lambda/`, zippez le code et les dépendances, puis utilisez AWS CLI ou la console AWS pour les déployer.
3. **Configurer DynamoDB** :
   - Créez les tables nécessaires dans DynamoDB selon les schémas fournis dans le dossier `dynamodb/`.
4. **Configurer API Gateway** :
   - Utilisez la console AWS API Gateway pour configurer votre API en suivant les spécifications du dossier `api-gateway/`.

## Utilisation
Les utilisateurs peuvent s'inscrire, mettre à jour leur profil, et rechercher des partenaires de sparring. Voici quelques exemples de requêtes API :

- **Enregistrement d'un Utilisateur** :
  ```
  POST /users
  {
      "username": "user1",
      "password": "password123"
  }
  ```
- **Mise à Jour de Profil** :
  ```
  PUT /users
  {
      "username": "user1",
      "profile_info": {
          "skillLevel": "beginner",
          "weight": 70
      }
  }
  ```
- **Recherche de Partenaires** :
  ```
  GET /search?skillLevel=beginner&weight=70
  ```

## Contributions
Les contributions à ce projet sont les bienvenues. Veuillez suivre les bonnes pratiques de développement et soumettre des pull requests pour toute proposition de modification ou d'amélioration.

## Licence
Ce projet est actuellement sans licence spécifique et est donc soumis aux droits d'auteur standards.

