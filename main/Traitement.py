#!/bin/env python3
import os
from pathlib import Path
import numpy.random as npr


class Traitement:   

    """
    Cette classe consiste à compter le nombre de mot de chaque texte contenue dans un tableau de liens.
    Son but à été choisi arbitraiement par nous afin d'avoir un main plus propre.
    """ 

    def load_html(liste_image,file_name):
        """
        .
        """
        Creation_fichier=Path(os.path.join(file_name,'Extraction_images_documents.html'))
        Creation_fichier.touch(exist_ok=True)
        with open(Creation_fichier,mode='w+') as html:
            html.write('<html>')
            for url_img in liste_image:
                html.write(f'<img src={url_img} />')
            html.write('</html>')
    

    def enregistrement_image_html(self):
        """
        On compte le nombre de mot contenu dans chaque texte grâce à la fonction split().
        """
        

    def show(self):
        """
        On retourne un tableau contenant le nombre de mot de chaque texte respectifs.
        """
        ...