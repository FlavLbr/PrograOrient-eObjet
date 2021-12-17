#!/bin/env python3

from wordcloud import WordCloud
import fitz
import io
import requests
from bs4 import BeautifulSoup as bs
from Collecte import Collecte
from Ressource import Ressource
from Traitement import Traitement
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
import webbrowser
import os

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
        liens=lien.readlines()
        self.liens=[]
        for i in liens:
                self.liens.append(i.replace("\n",""))
        textes= Collecte(self.liens)
        textes.run()
        self.textes=textes.content()
        return self.textes
    
    def show(self,lien,concatenation="ON",nombre_mot_wordCloud=None):
        """
        On traite les mots afin de sortir un nuage de mots à l'utilisateur qui sera ouvert texte par texte chacun son tour 
        et dans l'ordre des liens.
        """
        file_name=lien

        
        def EraseFile(repertoire):
            files=os.listdir(repertoire)
            for i in range(0,len(files)):
                os.remove(repertoire+'/'+files[i])

        EraseFile(file_name)


        if self.type=='Nuage' or self.type=='nuage':

            #on posse de base la contenation mais dois mettre ca en option
            
            
            if (concatenation=="ON"):
                texte = ' '.join(self.textes)
                wc = WordCloud(max_words=nombre_mot_wordCloud).generate(texte)
                wc.to_file(f'{file_name}/wordcloud.png')
                webbrowser.open(f'{file_name}/wordcloud.png')
                

            else:
                liste=[]
                for i in range (len(self.textes)):
                    wc = WordCloud(max_words=70).generate(self.textes[i])
                    wc.to_file(f'{file_name}/wordcloud{i}.png')
                    liste.append(f'{file_name}/wordcloud{i}.png')
                    file_name='/users/2022ds/118005444/Bureau/image'
                    Traitement.load_html(liste,file_name)
                    webbrowser.open(f'{file_name}/Extraction_images_documents.html')
            


        elif self.type=='Image' or self.type=='image':
            liste_url=[]

            for i in range (len(self.liens)):
                t=Ressource(self.liens[i])
                t=t.type()
                if t=="HTML":                   
                    url_image=Traitement.enregistrement_image_html(self.liens[i])
                    liste_url+=url_image

                
                
                elif t=="PDF":
                    liste_url+=Traitement.enregistrement_image_pdf(self.liens[i],file_name,i)

            Traitement.load_html(liste_url,file_name)
    
            
            webbrowser.open(f'{file_name}/Extraction_images_documents.html')
                
            
                    
                

           
