#!/bin/env python3
from wordcloud import WordCloud
from Collecte import Collecte
from Ressource import Ressource
from Traitement import Traitement
import webbrowser
import os

class Prisme:
    """
        Prisme prend un fichier txt, traite les liens présent dans le ficher et en fait un nuage de mots ou
        extrait  les images sur un fichier html ouvert ensuite sur une page web.
    """

    def __init__(self,type):
        """
            Il va y avoir 2 types principaux qui seront traités différement, Nuage et Image. 
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
    
    def show(self,lien,concatenation=None,nombre_mot_wordCloud=None):
        """
            On extrait les mots sous un nuage de mots ou les images dans un fichier html.
        """
        file_name=lien

        # Premièrement, nous nous assourons que le fichier que nous utilisons est bien vide en supprimant son contenu.
        def EraseFile(repertoire):
            files=os.listdir(repertoire)
            for i in range(0,len(files)):
                os.remove(repertoire+'/'+files[i])

        EraseFile(file_name)

        # On extrait les mots sous un nuage de mots qui souvre sur une page web. Nous avons ajouté l'option qui permet d'avoir le choix
        # entre un nuage de mots global et un pour chaque document.
        if self.type=='Nuage' or self.type=='nuage':

            if (concatenation=="ON" or concatenation=="on"):
                texte = ' '.join(self.textes)
                wc = WordCloud(max_words=nombre_mot_wordCloud).generate(texte)
                wc.to_file(f'{file_name}/wordcloud.png')
                webbrowser.open(f'{file_name}/wordcloud.png')
                

            elif (concatenation=="OFF" or concatenation=="off"):
                liste=[]
                for i in range (len(self.textes)):
                    wc = WordCloud(max_words=70).generate(self.textes[i])
                    wc.to_file(f'{file_name}/wordcloud{i}.png')
                    liste.append(f'{file_name}/wordcloud{i}.png')
                    file_name='/users/2022ds/118005444/Bureau/image'
                    Traitement.load_html(liste,file_name)
                webbrowser.open(f'{file_name}/Extraction_images_documents.html')
            
            else: raise ValueError("Veuillez bien écrire 'ON' ou 'OFF' s'il vous plaît.")
            

        # On extrait les images sur un fichier html qui s'ouvre, à la fin, sur une page web. Nous avons fait le choix de différencier le 
        # traitement entre les html et pdf.
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
        
        else: raise ValueError("Veuillez bien écrire 'Image' ou 'Nuage' s'il vous plaît.")
                
            
                    
                

           
