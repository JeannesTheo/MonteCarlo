# Utilisation d'un Monte Carlo pour prédire la meilleure stratégie de BlackJack

Basé sur le code de Donal Byrne, disponible sur [son repository GitHub](https://github.com/djbyrne/MonteCarlo).

Ce répertoire contient le code source d'un programme permettant de prédire la meilleure stratégie de BlackJack en
utilisant des Monte Carlo.

Trois variantes de Monte-Carlo sont implémentées dans le fichier [`monte_carlo.ipynb`](monte_carlo.ipynb):

- Une version On-Policy First-Visit, basée sur le code de [_Donal Byrne_](https://github.com/djbyrne/MonteCarlo))
- Une version On-Policy Every-Visit
- Une version Off-Policy First-Visit avec un mécanisme de Weighted Importance Sampling

Le fichier [`plot_utils.py`](plot_utils.py) contient des fonctions utilitaires pour afficher les résultats des
Monte-Carlo dans des graphiques.