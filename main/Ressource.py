#!/bin/env python3
# LEBRETON Flavien / GERAULT Thomas 
#pip install beautifulsoup4
from bs4 import BeautifulSoup
#pip install pdfminer
import requests
from pdfminer.high_level import extract_text
from io import BytesIO
from urllib.request import build_opener, HTTPCookieProcessor



class Ressource:
    """ 
    Ressource prend un lien pour un HTML ou un pdf, retourne si c'est un PDF ou un HTML
    avec la fonction type et retourne l'adresse sous forme d'un texte avec la fonction text.   
    """

    def __init__(self, url):
        """
        Lecture de l'url par request pris sur LE PROGRAMME D'ILYAS TASLI ET THEO LEGRUEL
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
            raise ValueError("Le document renseigné n'est ni un pdf, ni un html.")

        
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
            #html = urlopen(url).read()
            opener = build_opener(HTTPCookieProcessor())
            html = opener.open(url)
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

        else:
            raise ArithmeticError("Veuillez faire le '.type' avant de faire le '.text'")
        