#!/bin/env python3

from Ressource import Ressource
from Collecte import Collecte
from Traitement import Traitement
from Prisme import Prisme
"""
une_ressource = Ressource("http://www.archeonavale.org/pdf/cordeliere/test.pdf")
r=une_ressource.type() 
print(r)
r=une_ressource.text()
print(r)"""

"""
une_collecte = Collecte(["/run/media/flebreto/94D2-C54D/pdf1.pdf", "/run/media/flebreto/94D2-C54D/pdf2.pdf"])  
#une_collecte = Collecte(["C:/Users/Flavien/Desktop/certifScol.pdf","C:/Users/Flavien/Desktop/CV.pdf"])
une_collecte.run()                
print(une_collecte.content())"""

"""
le_traitement = Traitement()
le_traitement.load(["https://math.univ-angers.fr/~jaclin/_site2022_poO19_ds1/python_objet/2022/eval/projet.html", "https://math.univ-angers.fr/~jaclin/_site2022_poO19_ds1/python_objet/2022/heritage/heritage.html"])
le_traitement.run()         
le_traitement.show()
"""



un_prisme = Prisme('Image')      # crée le prisme générateur d'un nuage de mots
un_prisme.run("/users/2022ds/118005444/Bureau/liens.txt") 
un_prisme.show()

