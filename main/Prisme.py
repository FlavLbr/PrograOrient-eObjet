from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#https://ichi.pro/fr/creer-des-nuages-de-mots-personnalises-en-python-145227399773811

from Collecte import Collecte

class Prisme:
    """
    Prisme prend un fichier txt, traite les liens présent dans le ficher et en fait un nuage de mot.
    """

    def __init__(self,type):
        """
        Il va y avoir 2 types principaux qui seront traités différement, Nuage et Image. Pour l'instant nous traiton que Nuage.
        """
        self.type=type 

    def run(self,fichier):
        """
        On lance le traitement sur des ressources web ligne par ligne référencées dans fichier txt. On retourne un tableau de 
        textes.
        """
        lien = open(fichier,"r")
        self.liens=lien.readlines()
        for i in range (len(self.liens)):
                self.liens[i]=self.liens[i].replace("\n","")
        textes= Collecte(self.liens)
        textes.run()
        self.textes=textes.content()
        return self.textes
    
    def show(self):
        """
        On traite les mots afin de sortir un nuage de mots à l'utilisateur qui sera ouvert texte par texte chacun son tour 
        et dans l'ordre des liens.
        """
        if self.type=='Nuage' or self.type=='nuage':
            for i in range (len(self.textes)):
                wc = WordCloud(max_font_size=40).generate(self.textes[i])
                plt.imshow(wc, interpolation='bilinear')
                plt.axis("off")
                plt.show()