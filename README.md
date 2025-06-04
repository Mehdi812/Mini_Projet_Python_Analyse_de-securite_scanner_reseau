# Mini-Projet Python en groupe (Analyseur de Logs et Scanner Réseau)

Ce projet est réalisé par :

- **Mehdi MEBARKIA**
- **Nadjib BENSEGHIR**
- **Aymen BOUZERKOUNE**

## Description

Ce projet permet d’analyser des fichiers de logs pour identifier des activités suspectes (tentatives d’accès non autorisées, erreurs HTTP, etc.) et de réaliser un scan réseau pour détecter les ports ouverts sur des IPs suspectes. Il constitue un outil d’aide à la détection de comportements malveillants dans un environnement sécurisé.

---

## Technologies utilisées

- **Python 3.13** : langage de programmation pour l’implémentation
- **pandas** : manipulation et analyse des données
- **matplotlib** : visualisation graphique
- **threading** : parallélisation des scans de ports
- **re (regex)** : extraction précise des données dans les logs

---

## Architecture et démarche technique

### 1. Génération d'un ficheir de logs
execution script generate_fake_log.py pour genere un fichier de log sinon on vous livre un fichier pour tester 

### 2. Analyse des logs (`log_parser.py`)
- Lecture d’un fichier log (format personnalisé ou standard)
- Extraction des lignes pertinentes : erreurs HTTP, échecs de connexion, etc.
- Isolation des adresses IP sources
- Stockage sous forme de dictionnaire (IP → nombre d’occurrences) et de dictionnaire (IP → User-Agent(s))
- Détection de bots et scanners via le User-Agent
### 2. Analyse et visualisation (`data_analyzer.py`)
- Conversion des résultats en DataFrame pandas
- Classement des IPs par activité
- Génération d’un graphique à barres (Top 5)
- Détection automatique de bots via User-Agent
- Export en CSV et rapport HTML synthétique avec résumé et graphique