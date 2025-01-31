# Challenge-Robotique

Ce projet est une simulation de robot qui navigue à travers des cylindres tout en optimisant son chemin pour éviter les collisions et maximiser les récompenses.

## Structure du projet

- **Calcul.py** : Contient les fonctions principales pour calculer le chemin optimal, simuler le chemin, dessiner le chemin et écrire le chemin dans un fichier.
- **Colision.py** : Contient les fonctions pour détecter les collisions entre les segments de chemin et les cylindres.
- **GenerateMap.py** : Génère une carte aléatoire de cylindres et écrit cette carte dans un fichier CSV.
- **Robot.py** : Définit la classe `Robot` avec ses attributs et méthodes.
- **links.py** : Contient les liens vers les fichiers d'entrée et de sortie.
- **main.py** : Point d'entrée principal du programme. Génère la carte, calcule le chemin optimal, et affiche les résultats.
- **train_ia.py** : Contient les fonctions pour entraîner l'IA du robot.
- **input.py** : Contient la fonction pour lire la carte à partir d'un fichier CSV.
- **Cylindres.py** : Définit la classe `Cylindres` représentant les cylindres sur la carte.
- **test_Maps/** : Contient des fichiers de cartes de test.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/Challenge-Robotique.git
    ```
2. Accédez au répertoire du projet :
    ```sh
    cd Challenge-Robotique
    ```
3. Installez les dépendances nécessaires :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

Pour exécuter le programme principal, utilisez la commande suivante :
```sh
python main.py
```
pour entrainer le programme
```sh
python train_ia.py
```