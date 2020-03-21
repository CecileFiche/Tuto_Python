# Tuto Python

Avant toute chose, tu dois installer Python sur ton environnement de travail. Il existe plusieurs versions de python, les verions < 2.7 sont obsoletes et la version 2.7 elle-même sera très prochainement dépréciée. Le mieux est de te mettre aux version python 3.*

Pour connaître ta version python si tu as déjà une :
`python --version`

En fonction de tes projets et tes besoins, tu peux avoir besoin d'avoir plusieurs versions de python qui cohabitent sur ton espéce de travail. Pourquoi ? 
Imaginons que ton projet nécéssite l'utilisation d'une librairie (package) qui n'est pas suivie pour les versions de python > 3.4 et que ton installation de python est globale à ton ordinateur (en n'importe quel point la même), tu seras bloqué sur cette version 3.4 au risque de te retrouver bloqué sur d'autres projets qui eux réclémeront d'avoir une version de python moins obsolètes... Tu as donc tout intérêt à avoir ce que l'on appelle un environnement virtuel adapté à chacun de tes projets ce qui te permettra de les utiliser indépendamment les uns les autres.
!! Pas de panique, c'est hyper simple à installer et ça pourra faciliter ton travail avenir ! Mieux vaut y passer un tout petit peu de temps ;)

Donc, tu DOIS installer une librairie, «virtualenv» (pour virtual environment) qui te permettra de ne pas avoir de problème de version python. 


## Etape 1 :
**Installation de python 3** 
Comme je ne sais pas sur quel environnement tu travailles mais que je suppose que c'est le seul sur lequel je n'ai jamais eu à faire d'installation de ce genre (Windows), je te laisse chercher sur internet les commandes adequates, sorry :)

## Etape 2 :
**Installation de la librairie «pip»** qui est LA librairie de référence qui gère toute l'installation des packages Python : elle gère les dépendances, les versions etc...
cf :  https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Etape 3:
**Installation du package «virtualenv»** qui va te permettre d'installer des packages, dans une version 
suivre les instructions pour windows sur cette même page. https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Etape 4
**Créer ton propre environnement virtuel** que tu peux appeller comme tu veux (généralement je précise le nom de la version python dedans pour de futures utilisations). Les commandes sont explicites, toujours sur cette même page.

## Etape 5
**Activer ton environnement virtuel**. A chaque fois que tu voudras travailler sur ton projet, c'est la première chose que tu devras faire (avant tout !)
`.\env\Scripts\activate`  #-- si tu as nommé ton environnement virtuel "env", sous windows


**`Exemple d'utilisation`**

`pip install pandas`  #-- Pour installer le package "pandas" qui devrait te servir
Si tu as un doute sur le nom d'un package, je t'invite à aller là: https://pypi.org/project/pandas/ par exemple pour connaître la commande, la version etc... d'un package (ici pandas)

`pip install --upgrade pip`  #-- pour upgrader le package "pip" lui même 

`pip install pandas --upgrade`  #-- pour upgrader un autre package (ex pandas) 

`pip freeze` #-- pour voir tous les packages installés et leurs versions 

`pip install -r requirements.txt` #-- pour installer tous les packages mentionnés dans "requirements.txt", un fichier .txt tout bête que tu peux éditer très simplement.


## Etape 6
**Installation de Jupyter !**
cf: https://jupyter.org/install C'est trop cool ! En gros, ça te permet d'ouvrir un server "jupyter" en local
