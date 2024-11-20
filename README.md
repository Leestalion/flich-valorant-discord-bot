# flich-valorant-discord-bot
## Introduction

Ce projet est un bot Discord pour le jeu Valorant, conçu pour fournir diverses fonctionnalités et informations aux joueurs. Le bot est construit en utilisant Python et utilise plusieurs API pour récupérer des données en temps réel.

## Fonctionnalités

- **Statistiques des joueurs** : Obtenez des statistiques détaillées sur les joueurs de Valorant.
- **Informations sur les agents** : Consultez les détails et les capacités des agents de Valorant.
- **Mises à jour et actualités** : Recevez les dernières nouvelles et mises à jour sur Valorant.
- **Commandes personnalisées** : Créez et gérez des commandes personnalisées pour le serveur Discord.

## Installation

Pour installer et exécuter le bot, suivez les étapes ci-dessous :

1. Clonez le dépôt GitHub :
    ```powershell
    > git clone https://github.com/lemar/flich-valorant-discord-bot.git
    ```
2. Accédez au répertoire du projet :
    ```powershell
    > cd flich-valorant-discord-bot
    ```
3. Installez les dépendances Python :
    ```powershell
    > pip install -r requirements.txt
    ```
4. Configurez les variables d'environnement dans le fichier `.env`.
    ```.env
    # .env file
    DOCKER_TOKEN='Your_Docker_Token'
    ```
6. Exécutez le bot :
    ```powershell
    > python main.py
    ```

# Configuration avancée
## Prérequis

Avant de commencer, assurez-vous d'avoir rempli les conditions suivantes :
- Vous avez un compte GitHub. Sinon, vous pouvez en créer un [ici](https://github.com/join).
- Vous avez installé GitHub CLI. Vous pouvez le télécharger [ici](https://cli.github.com/).

## Connexion à GitHub

Pour vous connecter à GitHub en utilisant GitHub CLI dans le terminal de VS Code, suivez ces étapes :

1. Ouvrez le terminal dans VS Code.
2. Exécutez la commande suivante pour vous authentifier auprès de GitHub :
    ```sh
    > gh auth login
    ```
3. Suivez les instructions pour terminer le processus d'authentification.

## Fichier .env

Le fichier `.env` contient les variables d'environnement nécessaires pour exécuter l'application. Par exemple, il peut inclure des jetons d'API, des clés secrètes, et d'autres configurations sensibles. Assurez-vous de ne pas partager ce fichier publiquement.

## Environnement virtuel (venv)

Un environnement virtuel (venv) est un outil qui permet de créer des environnements Python isolés. Cela permet de gérer les dépendances spécifiques à un projet sans interférer avec les autres projets. Pour créer un environnement virtuel, exécutez les commandes suivantes :

```powershell
> python -m venv venv
> .\venv\Scripts\activate
```

## Exigences

Le fichier `requirements.txt` répertorie toutes les dépendances Python nécessaires pour exécuter l'application. Ces dépendances seront installées à l'intérieur du conteneur Docker.

## Dockerfile

Le `Dockerfile` est utilisé pour créer une image Docker pour l'application. Il comprend les étapes suivantes :

1. Utiliser l'image officielle de Python depuis Docker Hub.
2. Définir le répertoire de travail dans le conteneur à `/app`.
3. Copier le fichier `requirements.txt` dans le conteneur.
4. Installer les dépendances listées dans `requirements.txt`.
5. Copier le reste du code de l'application dans le conteneur.
6. Définir la commande pour exécuter l'application (`python main.py`).

## fly.toml

Le fichier `fly.toml` est le fichier de configuration pour déployer l'application sur Fly.io. Il inclut les paramètres suivants :

- `app` : Le nom de l'application.
- `kill_signal` : Le signal à envoyer à l'application pour la terminer.
- `kill_timeout` : Le temps d'attente avant de forcer la terminaison de l'application.
- `processes` : Une liste de processus à exécuter (actuellement vide).
- `env` : Les variables d'environnement pour l'application.

Pour plus d'informations sur la configuration de `fly.toml`, consultez la [documentation de Fly.io](https://fly.io/docs/reference/configuration/).