# Search API Documentation

## Overview
Ce document décrit l'endpoint de recherche de partenaires de sparring dans l'application.

---

## Recherche de Partenaires de Sparring

### Request
- **Endpoint**: `GET /search`
- **Query Parameters**:
  - `skillLevel` (optionnel): Niveau de compétence, ex. "débutant"
  - `weight` (optionnel): Poids en kilogrammes

### Response
- **Success**:
    - **Code**: 200 OK
    - **Content**:
        ```json
        [
          {
            "username": "sparring_partner_1",
            "details": {
              "skillLevel": "intermédiaire",
              "weight": 75
            }
          },
          ...
        ]
        ```

---

## Notes
- Les résultats retournés dépendent des critères de recherche spécifiés dans la requête.
