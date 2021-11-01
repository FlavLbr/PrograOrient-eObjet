from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#https://ichi.pro/fr/creer-des-nuages-de-mots-personnalises-en-python-145227399773811


class Prisme:

    def __init__(self,type):
    # crée le prisme générateur d'un nuage de mots
        self.type=type #soit nuage siut image

    def run(self,fichier):
    # lance le traitement sur des ressources web référencées dans fichier
        ...
    
    def show(self):
    # visualise le nuage de mots
        if self.type=='Nuage' or self.type=='nuage':
            wc = WordCloud(max_font_size=40).generate(self.text)
            plt.imshow(wc, interpolation='bilinear')
            plt.axis("off")
            plt.show()