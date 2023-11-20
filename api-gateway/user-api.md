# Users API Documentation

## Overview
Ce document décrit les endpoints relatifs à la gestion des utilisateurs dans l'application de Sparring Partners.

---

## Enregistrement d'un Nouvel Utilisateur

### Request
- **Endpoint**: `POST /users`
- **Body**:
    ```json
    {
      "username": "nom_utilisateur",
      "password": "mot_de_passe"
    }
    ```

### Response
- **Success**:
    - **Code**: 200 OK
    - **Content**:
        ```json
        { "message": "User registered successfully!" }
        ```

---

## Mise à Jour du Profil Utilisateur

### Request
- **Endpoint**: `PUT /users`
- **Body**:
    ```json
    {
      "username": "nom_utilisateur",
      "profile_info": {
        "skillLevel": "débutant",
        "weight": 70
      }
    }
    ```

### Response
- **Success**:
    - **Code**: 200 OK
    - **Content**:
        ```json
        { "message": "Profile updated successfully!" }
        ```

---

## Notes
- Les mots de passe doivent être envoyés de manière sécurisée et chiffrés dans la base de données.
