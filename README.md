Analyse de Sentiments avec Flask

Ce projet utilise Flask pour créer une application web permettant d'analyser le sentiment d'un texte en utilisant deux méthodes : TextBlob et NLTK's Vader.

Prérequis

Avant de commencer, assurez-vous d'avoir Python et Flask installés sur votre système. Vous pouvez installer les dépendances nécessaires en exécutant :

                           pip install flask textblob nltk spacy
                           python -m spacy download en_core_web_sm



Fonctionnalités

L'application offre les fonctionnalités suivantes :


Analyse de Sentiments avec TextBlob : Utilisation de TextBlob pour déterminer si le texte est positif, négatif ou neutre.
Analyse de Sentiments avec NLTK's Vader : Utilisation de NLTK's Vader pour calculer les pourcentages de positivité, négativité et neutralité dans le texte.


Structure du Projet

app.py : Contient le code principal de l'application Flask.
templates/ :
home.html : Page d'accueil de l'application.
index.html : Formulaire pour saisir le texte à analyser et affichage des résultats.



Utilisation

1- Clonez ce repository 
2- Lancez l'application avec python app.py
3- Accédez à l'application dans votre navigateur à l'adresse : http://localhost:5000
