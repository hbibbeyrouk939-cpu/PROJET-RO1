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
- Modélisation : Pyomo Framework
- Solveur : HiGHS (`appsi_highs`) via le paquet `highspy`  <!-- FIX: était GLPK, le code utilise HiGHS -->

## Installation des Dépendances

```bash
pip install pyomo highspy
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
