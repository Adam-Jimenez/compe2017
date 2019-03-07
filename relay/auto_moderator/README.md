# Resumé énoncé

Le but de l'application est de faire du sentiment analysis d'un message par rapport à l'un de nos produits.

Un dictionnaire est fourni qui décrit les mots qui seront dans le message sous un format spécifié dans la section Dictionnaire.
Format dictionnaire:
<mot>\[<attributs mots>]

Notre programme prend un fichier csv en parametre décrivant un message et détermine s'il est positif, négative, neutral ou non relié a notre produit.

# Fonctionnalités accomplies
- Lecture du csv
- Lecture du dictionaire
- Regle 1: Ideji + "b" = negative
- Regle 2: Ideji + "g" = positive
- Regle 3: "your" + "product" or "app" or ... + "b" = positive
- Regle 4: "your" + "product" or "app" or ... + "g" = negative
- Regle 5: !Ideji = neutral
- Regle 6: "c" + "b" = positive
- Regle 7: "c" + "g" = negative

