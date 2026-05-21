# Projet de Recherche Opérationnelle - 2026

## Informations de l'Équipe
- Présenté par :
  - Mohamed Lehbib Mbarek Beyrouk — C27888
  - Aly Mohamed Aly — C28916
  - Maidla Isselmo — C28462
- Filière : L2 (MIAGE / DA2I) — S4

## Description du Projet
Ce dépôt contient trois études de cas optimisées en utilisant la programmation linéaire,
réalisées dans le cadre du module Recherche Opérationnelle.

### Sujets Traités
1. **Situation 6.1 (RIM)** : Optimisation du transport de poissons (Nouadhibou → Nouakchott).
2. **Situation 6.3 (RIM)** : Routage des camions d'eau dans les quartiers périphériques (TSP – MTZ).
3. **Situation 2.3** : Dimensionnement de stock par le modèle EOQ (Wilson).

## Technologies Utilisées
- Langage : Python 3.x
- Modélisation :Pyomo Framework
- Solveur :GLPK (Méthode du Simplexe)

## Installation des Dépendances

```bash
pip install pyomo
```
```bash
pip install glpk
```
ou
```bash
conda install -c conda-forge glpk pyomo
```

## Exécution des Modèles

```bash
# Résoudre le problème de transport de poissons
python transport_poisson.py

# Lancer le routage des camions d'eau
python routage_eau.py

# Exécuter le calcul EOQ (valeurs par défaut du rapport)
python gestion_stock.py

# EOQ avec paramètres personnalisés
python gestion_stock.py --demand 1200 --order-cost 50 --holding-cost 2
```
---

## 📺 Présentations Vidéos (Démos Loom)

Pour accompagner notre rapport et valider l'implémentation technique de chaque partie, vous pouvez visionner les explications détaillées et les démonstrations de code en cliquant sur les liens ci-dessous :

| # | Partie du Projet | Intervenant | Lien de la Vidéo (Loom) |
| :-: | :--- | :--- | :--- |
| 1 | **Introduction & Optimisation du Transport de Poisson** | Mouhamed Lehbib Beyrouk | [▶ Regarder la vidéo](https://www.loom.com/share/7d19636821a249fd8407f32cbd4549d5) |
| 2 | **Routage des Camions d'Eau (Formulation MTZ)** | Aly Mohamed Aly / Maidla | [▶ Regarder la vidéo](الرابط_الخاص_بفيديو_المياه) |
| 3 | **Gestion des Stocks (Modèle de Harris-Wilson)** | Aly Mohamed Aly / Maidla | [▶ Regarder la vidéo](الرابط_الخاص_بفيديو_المخزون) |

> 💡 **Note :** Chaque vidéo contient une explication théorique de la situation modélisée ainsi qu'une exécution en direct (Live Demo) du script Python correspondant.
 