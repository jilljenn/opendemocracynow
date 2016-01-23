# Nesquiz

Outil qui incite les gens à voter en recommandant des articles susceptibles de les intéresser.

En partant des traces numériques, nous cherchons à détecter les similarités entre les votants: c'est une approche par le comportement de l'utilisateur.

L'idée serait de faire un assistant personnel qui permet d'éviter d'être noyé dans la masse de contributions.

2 points de débat et de vigilance dans le groupe:

* La consommation culturelle diffère de la pratique démocratique.
* L'orientation sur des articles ne permet pas le débat.

(peut-être nous pourrions utiliser des outils de cartographie de controverse - comme [Arguman](http://en.arguman.org/)
ou encore le projet [Sciences/Bruno Latour](http://www.sciencespo.fr/edc/fr/blog/controverses-episode-i).)

# Deux composantes

## Votes.CSV (2c4b)
L'objectif est d'appliquer un traitement sur les votes provenant de chaque utilisateurs.

## Script de @jilljenn (algorithme de classification)
Pour identifier les différents collèges de contributeurs, nous procédons:

Un algorithme qui a pour but d'identifier les voisinages par vote : tel utilisateur a voté sur tel article, puis on applique un score par utilisateur.

Le résultat nous permet d'identifier des utilisateurs qui auront voté sur le même article.

L'algorithme classifie le vote de chaque participant et crée un profil pour un score similaire, le script génère à la suite une liste d'utilisateurs qu'on dit « proche de son profil » (c'est-à-dire dont le profil se ressemble beaucoup).

# Travail sur les profils

Nicolas : Lecture du CSV et nettoyage.

Il fait une fonction qui prend un utilisateur en paramètre et affiche son profil.

La fonction procède à l'interprétation du fichier CSV afin qu'il identifie qui est à l'origine d'un vote.

But: Pour un utilisateur donné, on est capable de récupérer la nature de son vote et les articles sur lesquels il a voté.

@jilljenn ensuite applique son algorithme KNN sur le CSV: *Quels sont les voisins d'un utilisateur?*
Puis, chaque utilisateur se voit recevoir la liste de ses voisins les plus proches, et @jilljenn en génère enfin une page personnelle de profil qu'on peut visiter sur Internet.

Constance tente de faire une cartographie sur [Cortext](http://www.cortext.net/): un réseau hétérogène.
Cette initiative fait de l'analyse de co-occurrence. On pourrait se doter d'un fichier qui réunit les données d'un utilisateur ainsi que ses voisins.
L'objectif étant de produire une visualisation.

# Travail sur [le site Internet](http://www.nesquiz.com)

Mori est responsable des points suivants:

* Ocsar: la liste des articles de loi qui font l'objet de débat en ce moment sur le site.
* Antoine : l'écriture du code de la page d'accueil (landing page).

Le résultat est visible sur <nesquiz.com>
La réalisation d'une page HTML statique pour télécharger les voisins en format JSON est disponible sur <odn.jiji.cat> (traitement de données personnelles)

# Travail sur les tags des articles pour rendre lisible la loi

## Comment est-ce qu'on rend compte de la complexité de la loi ?

* Il faut rendre lisible pour les citoyens, pour les juristes, une modification qui va avoir un impact sur d'autres articles.
* Il faudrait se référer à des ontologies juridiques sur lesquelles cette partie du projet pourrait s'appuyer.

l'objectif est de rendre lisible la loi, en fournissant des explications, ou en faisant des renvois sur des références extérieures ([légifrance](http://www.legifrance.gouv.fr/)).
Un mot-clé (_tag_) permet l'accès à ces explications.

Pour chaque article de la loi, un encart avec des explications pédagogiques, et potentiellement une version consolidée du texte.

**Taguer** des mots importants, des mots clés, des thématiques : l'objectif étant d'éviter le parasitage.
Ces mots clés informent sur l'enjeu de l'article, par exemple: « Ouverture des données publiques ».
