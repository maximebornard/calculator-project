Author: Maxime BORNARD

# Calculator Project

## Présentation générale

Ce projet consiste à créer un paquet Python nommé `calculator` contenant une classe `SimpleCalculator` permettant d’effectuer des opérations arithmétiques de base.

L’objectif principal du projet est de mettre en pratique les bonnes pratiques modernes du développement Python :

- Création d’un paquet installable  
- Utilisation d’une structure de projet moderne (`src/`)  
- Écriture de tests unitaires  
- Utilisation d’outils de qualité de code  
- Distribution du projet  

Ce projet a été réalisé dans un cadre pédagogique afin de comprendre les différentes étapes du cycle de développement d’un projet Python.

---

## Fonctionnalités

La classe `SimpleCalculator` propose les opérations suivantes :

| Méthode | Description | Type de retour |
|----------|-------------|----------------|
| `fsum(a, b)` | Addition de deux entiers | `int` |
| `substract(a, b)` | Soustraction de deux entiers | `int` |
| `multiply(a, b)` | Multiplication de deux entiers | `int` |
| `divide(a, b)` | Division de deux entiers | `float` |

---

## Règles de fonctionnement

- Tous les paramètres doivent être des entiers (`int`).
- Les méthodes `fsum`, `substract` et `multiply` retournent un entier.
- La méthode `divide` retourne toujours un nombre flottant (`float`).
- Un type invalide déclenche une `TypeError`.
- Une division par zéro déclenche une `ZeroDivisionError`.

---

## Structure du projet

```
calculator-project/
├── pyproject.toml
├── LICENSE
├── README.md
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── simple_calculator.py
└── tests/
    └── test_simple_calculator.py
```

---

## Rôle des fichiers

### `pyproject.toml`

Fichier de configuration principal du projet.  
Il contient :

- Les métadonnées du projet  
- Les dépendances  
- Les outils de test et de qualité  

### `simple_calculator.py`

Contient la classe `SimpleCalculator` et les opérations arithmétiques.

### `__init__.py`

`SimpleCalculator` pour permettre l’import simplifié :

```python
from calculator import SimpleCalculator

### `test_simple_calculator.py`

Contient les tests unitaires qui vérifient le bon fonctionnement du calculateur.

