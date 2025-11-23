# Générateur de Blagues

Une application Python simple qui utilise l'API publique [JokesAPI](https://v2.jokeapi.dev/) pour afficher une blague aléatoire dans la console. Ce projet est conteneurisé avec Docker.

## Fonctionnalités

- Interrogation d'une API REST via la librairie `requests`.
- Gestion des blagues de type "One-liner" et "Setup/Delivery".
- Filtrage des contenus (Safe mode activé).

## Prérequis

- Python 3.x
- Docker (optionnel, pour l'exécution en conteneur)

## Installation et exécution locale

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
