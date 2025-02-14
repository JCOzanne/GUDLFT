
# GUDLFT

Le projet est une application de réservation pour les compétitions régionales de compétitions de force pour l’entreprise Güdlft.  
Son objectif est de fournir une plateforme **simple**, **rapide** et **équitable**, garantissant la transparence des réservations.  
Il a été réalisé à partir du projet [Python-Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing)  
Ce projet était à l’état de prototype.  
Il a été amélioré en suivant une approche **Test Driven Development (TDD)**

## Fonctionnalités principales
L’application permet de :
- Se connecter avec une adresse e-mail de club.
- Consulter les compétitions à venir et les places disponibles.
- Réserver des places en utilisant les points du club.
- Consulter un tableau public des points des clubs , même sans être connecté

## Installation

### Prérequis

- Python 3.12+
- Flask 3.1.0

### Étapes d’installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/JCOzanne/GUDLFT.git

   cd GUDLFT
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Sur Windows : .venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Lancez le serveur Flask :
   ```bash
   $env:FLASK_APP = "server.py"
   flask run
   ```

5. Accédez à l'application :

   - Ouvrez [http://127.0.0.1:5000](http://127.0.0.1:5000) dans votre navigateur.


## Structure du projet
```
GUDLFT/
├── templates/
├── tests/
├       ├── unit_tests
├       ├── integration_tests
├       ├── performance_tests
├── requirements.txt
├── competitions.json
├── clubs.json
└── server.py      
```

## Tests

### Tests unitaires et tests d’intégration
Ils sont exécutés avec la librairie [Pytest](https://docs.pytest.org/en/stable/).   
Pour effectuer l’ensemble des tests unitaires et d’intégration, lancer la commande : 
```
pytest tests/
```

Nous avons utilisé la librairie [Coverage](https://coverage.readthedocs.io/en/7.6.12/) pour connaître le taux de couverture des tests.  
Un rapport de couverture est généré avec la commande : 
```
pytest --cov=. tests/
```

### Tests de performance
Nous avons utilisé la librairie [Locust](https://docs.locust.io/en/stable/index.html) pour réaliser les tests de performance.  
Pour lancer le serveur de test, entrer la commande : 
```
locust tests/performance_tests/locustfile.py
```
Puis ouvrir son navigateur et saisir l’url  http://localhost:8089   
Enfin, renseigner les champs :   
Number of total users to simulate : 6  
Spawn rate : 1  
Host : http://127.0.0.1:5000/  


