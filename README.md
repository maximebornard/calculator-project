Auteur: Maxime BORNARD

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
Les outils de qualité sont définis dans pyproject.toml :  
    test = ["pytest>=7.0", "pytest-cov", "pylint", "black", "radon"]  

### `simple_calculator.py`

Contient la classe `SimpleCalculator` et les opérations arithmétiques.

### `__init__.py`

`SimpleCalculator` pour permettre l’import simplifié :

```python
from calculator import SimpleCalculator
```

### `test_simple_calculator.py`

Contient les tests unitaires qui vérifient le bon fonctionnement du calculateur.

## Installation du projet

### Création d’un environnement virtuel

Sous Windows :
python -m venv .venv

### Activation

.venv_calculator\Scripts\activate

### Installation du projet et des dépendances de test

pip install -e .[test]  

Cette commande :  
    Installe le paquet calculator  
    Installe les outils de test et de qualité  
    Active le mode développement (editable)  
    
## Les tests unitaires avec pytest

### Qu’est-ce qu’un test unitaire ?

Un test unitaire est un petit programme qui vérifie qu’une fonction :  
    Renvoie le bon résultat  
    Ou déclenche l’erreur attendue  
L’objectif est de s’assurer que le code fonctionne correctement et qu’il ne casse pas lors de modifications futures.  

### Pourquoi utiliser pytest ?

pytest est un framework de test très populaire en Python car il est :  
    Simple à utiliser  
    Lisible  
    Puissant  
    Standard dans les projets modernes  

### Structure d’un test pytest
Exemple simple :  
def test_addition():  
    assert 2 + 3 == 5

Fonctionnement :  
    pytest exécute la fonction  
    Il évalue le assert  
    Si la condition est vraie → test réussi  
    Sinon → test échoué  

### Tester une erreur

Pour vérifier qu’une fonction déclenche une erreur :  
with pytest.raises(TypeError):  
    calc.fsum("2", 3)  
    
Fonctionnement :  
pytest exécute la ligne  
Si une TypeError est levée → test réussi  
Sinon → test échoué  

### Lancer les tests

Dans le dossier du projet :  

pytest  
Résultat attendu :  
13 passed  

Cela signifie que tous les tests ont réussi.  

Détail des tests du projet  

Les tests couvrent toutes les méthodes du calculateur.  

## Tests de l’addition (fsum)

Vérifie :  
L’addition de deux entiers positifs  
L’addition de deux entiers négatifs  
La gestion des types invalides  

Exemple :  
def test_fsum_positive():  
    assert calc.fsum(2, 3) == 5  
    
## Tests de la soustraction (substract)

Vérifie :  
Une soustraction simple  
Une soustraction avec nombres négatifs  
La gestion des types invalides  

## Tests de la multiplication (multiply)

Vérifie :  
Une multiplication normale  
Une multiplication par zéro  
La gestion des types invalides  

## Tests de la division (divide)

Vérifie :  
Une division normale  
Un numérateur égal à zéro  
Une division par zéro  
La gestion des types invalides  

Exemple :  

def test_divide_by_zero():  
    with pytest.raises(ZeroDivisionError):  
        calc.divide(5, 0)  

## Couverture de code avec pytest-cov

pytest-cov permet de mesurer la couverture des tests.  

Commande :  
    pytest --cov=calculator  

Cela affiche :  
    Le pourcentage de code testé  
    Les lignes non couvertes  
    Objectif : atteindre une couverture proche de 100 %.  
    Analyse de qualité du code  

## Pylint — Qualité du code

Analyse :  
    Le style du code  
    Les erreurs potentielles  
    La lisibilité  

Commande :  
    pylint src/calculator/simple_calculator.py  

Objectif :  
    10.00/10 -> note obtenu avec ce projet sur tout les fichiers  

## Black — Formatage automatique

Formate automatiquement le code pour :  
    Respecter un style standard  
    Supprimer les espaces inutiles  
    Améliorer la lisibilité  

Commande :  
    black .  

## Radon — Complexité du code

Analyse :  
    La complexité cyclomatique  
    La maintenabilité  

Commande :  
    radon cc src -a  

## Exemple d’utilisation
from calculator import SimpleCalculator  

calc = SimpleCalculator()  

    print(calc.fsum(2, 3))        # 5  
    print(calc.substract(5, 2))   # 3  
    print(calc.multiply(4, 3))    # 12  
    print(calc.divide(6, 3))      # 2.0  

## Construction du paquet

Génération des distributions :  

python -m build  
Fichiers générés dans dist/ :  
    .whl (wheel)  
    .tar.gz (source)  

## Publication sur TestPyPI

Upload du paquet :  
twine upload --repository testpypi dist/*  

---

# Intégration Continue et Déploiement Continu (CI/CD)

Afin d’automatiser la qualité du code et la publication du paquet, une pipeline CI/CD a été mise en place sur **GitHub** et **GitLab**.

## CI/CD avec GitHub Actions

Un workflow GitHub Actions a été configuré dans :

```
.github/workflows/main.yml
```

### Partie CI (Intégration Continue)

À chaque `push` ou `pull request`, la pipeline exécute automatiquement :

- Installation de Python (version 3.10)
- Installation des dépendances
- Vérification du format avec **Black**
- Analyse statique avec **Ruff / Pylint**
- Exécution des tests avec **pytest**
- Vérification de la couverture de code

Objectif : garantir que le code est propre, testé et fonctionnel avant toute publication.

---

### Partie CD (Déploiement Continu)

Lorsqu’un tag au format `vX.Y.Z` est créé (exemple : `v0.0.4`), la pipeline :

1. Construit le paquet (`python -m build`)
2. Génère les artefacts (`.whl` et `.tar.gz`)
3. Publie automatiquement le paquet sur **TestPyPI** via `twine`

Cela permet une publication automatisée et sécurisée.

---

## CI/CD avec GitLab CI

Une pipeline équivalente a été mise en place sur GitLab via le fichier :

```
.gitlab-ci.yml
```

### Stages configurés

La pipeline GitLab est divisée en plusieurs étapes :

- `lint` → vérification du format et de la qualité
- `test` → exécution des tests unitaires
- `build` → construction du paquet
- `publish` → publication sur TestPyPI

---

### Déclenchement

- Un simple `push` déclenche la CI (lint + tests + build).
- Un tag au format `vX.Y.Z` déclenche en plus la publication automatique sur TestPyPI.

Exemple :

```
git tag v0.0.4
git push origin v0.0.4
```

---

## Sécurisation des publications

La publication sur TestPyPI utilise un **API Token** stocké comme variable sécurisée :

- GitHub → `Secrets`
- GitLab → `CI/CD Variables`

Le token permet d’authentifier `twine` sans exposer de mot de passe dans le code.

---

## Objectif pédagogique

La mise en place du CI/CD permet de :

- Comprendre l’automatisation des tests
- Industrialiser la qualité du code
- Automatiser la distribution d’un paquet Python
- Se rapprocher des pratiques professionnelles modernes

Cette étape complète le cycle de vie du projet :
développement → test → build → publication automatisée.

## Auteur

Maxime Bornard

## Licence

Projet distribué sous licence Unlicense.  
La licence Unlicense place le projet dans le domaine public, permettant à toute personne d’utiliser, modifier et redistribuer le code sans aucune restriction.  
Ce choix est adapté à un projet pédagogique, car il favorise la libre réutilisation et la simplicité juridique sans contraintes de licence.  
