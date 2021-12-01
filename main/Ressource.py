#!/bin/env python3
from urllib.request import urlopen
#pip install beautifulsoup4
from bs4 import BeautifulSoup
#pip install pdfplumber
import requests
from pdfminer.high_level import extract_text
from io import BytesIO



class Ressource:
    """ 
    Ressource prend un lien pour un HTML ou un adresse de répertoire pour un pdf, retourne si c'est un PDF ou un HTML
    avec la fonction type et retourne l'adresse sous forme dans texte avec la fonction text.   
    """

    def __init__(self, url):
        """
        theo ilyas et maxime lol
        """
        self.url = url

        self.r = requests.get(self.url)
        self.content_type = self.r.headers.get('content-type')
    
    def type(self):
        """
        On retourne si le lien ou l'adresse est un PDF ou un document HTML et enregistre le type sur une 
        variable self.
        """
        if 'application/pdf' in self.content_type:
            self.type = "PDF"
            self.pdf_name = self.url.split('/')[-1]
            self.pdf_content = self.r.content
            return "PDF"

        elif 'text/html' in  self.content_type:
            self.type = "HTML"
            return "HTML"
            
        else :
            self.type = "Non supporté"
            return "Non supporté"

        
    def text(self):
        """
        On renvoi un texte épuré dans document HTML ou d'un PDF. Attention! Il faut faire le .type avant afin 
        que le self.type soit définit
        """
        
        if (self.type=="PDF"):
            #Fonction utilisé pour un document PDF
            pdf = BytesIO(self.pdf_content)
            return extract_text(pdf)

        
        elif (self.type=="HTML"):
            #Fonction utilisé pour un document HTML
            url = self.url
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            # On retire tous les éléments autres que le texte
            for script in soup(["script", "style"]):
                script.extract()  
            # On prend le texte sur une variable
            htmltext = soup.get_text()
            # On retire les lignes en trop vide ainsi que les espaces vides
            lines = (line.strip() for line in htmltext.splitlines())
            # On divise chaque gros titre afin de pouvoir organiser
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # On combine toutes les grosses partie pour former un document
            htmltext = '\n'.join(chunk for chunk in chunks if chunk)
            return htmltext

        elif (self.type == "Non supporté"): ... #faire une fonction erreur
        else:
            #demande à l'utilisateur d'utiliser la fonction type avant afin d'avoir une valeur au self.type
            print("Il faudrait faire la fonction type avant svp")
            return 0
        