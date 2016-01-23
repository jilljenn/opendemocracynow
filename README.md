# Nesquiz

Outil qui incite les gens à voter en recommandant des articles suscetibles de les intéresser.
En partant des traces numériques, détecter les similarités entre les votants: aprproche par le comportement de l'utilisateur
L'idée serait de faire un assistant personnel qui permette d'éviter d'être noyé dans la masse de contributions.
2 points de débat et de vigilance dans le groupe: 
1. consommation culturelle diffère de la pratique démocratique. 
2. orientation sur des articles ne permet pas le débat 
(peut-etre peut-on utiliser des outils de cartographie de controverse - comme arguman http://en.arguman.org/; 
voir aussi le projet Sciences/Bruno Latour http://www.sciencespo.fr/edc/fr/blog/controverses-episode-i).

# fichier : votes.csv (2c4b)

objectif d'appliquer un traitement sur les votes. sur ce fichier, on a chaque vote des utilisateurs.
Pour identifier les différents collèges de contributeurs.

# un script (de JiJi) : une liste d'instructions qui a pour but d'identifier les voisinages par vote : tel utilisateur a voté sur tel article, et on applique un score par utilisateur, ce qui permet d'identifier des utilisateurs qui auront voté sur le même .
il identifie le vote pour chaque participant, et il définit un profil un score similaire. le script donne une méthode pour tel utilisateur voilà le ou les profils les plus proches.

# comment est-ce qu'on rend la complexité de la loi visible ? rendre lisible pour les citoyens, pour les juristes, une modification qui va avoir un impact sur d'autres articles.
faire une maquette qui  permette de rendre lisible

#Nicolas : lecture du csv et nettoyage 
il fait une fonction : il prend un utilisateur et affiche le profil
doit faire une fonction qui scanner le fichier csv et pour qu'il identifie qui a fait quel vote 
soit tu as la liste, soit le dictionnaire 
fonction en python : pour un utilisateur donné, récupération de la nature du vote, et des articles sur lesquels il a voté

#JJ: il applique le script de voisinage sur le csv
quel voisin d'un utilisateur ?
recueil des données qui sont similaires à un utilisateur 1
pour chaque utilisateur on obtient la liste de ses voisins organisés par ordre de proximité

#JJ a réalisé des pages de profil

#Constance : elle essaie de faire une carto sur cortext : un réseau hétérogène.
ce système fait de l'analyse de cooccurrence. 
on pourrait avoir un fichier qui réunit les données sur un utilisateur et ses voisins
soit un objet python, 
soit un dictionnaire : 
objectif est de produire une visualisation 
#Mori : travail sur la page d'accueil:
Oscar : la liste des articles de loi qui sont en cours de débat sur le site
Antoine : développe la page d'accueil 

site visible sur nesquiz.com
réalisation d'une page html statique pour télécharger les voisins enfichier .json sur odn.jiji.cat
(traitement de données personnelles)

# travail sur les tags des articles
il existe des ontologies juridiques. objectif de rendre lisible la loi, en fournissant des explications, ou ne faisant des renvois sur des références extérieures. Un mot-clef qui te donne accès à des explications. 
- TAGUER : éviter le parasitage. les mots-clefs qui donnent l'enjeu de l'article : ouverture des données publiques
