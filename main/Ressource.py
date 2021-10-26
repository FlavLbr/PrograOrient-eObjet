import requests
import urllib
from bs4 import BeautifulSoup

class Ressource:
    def __init__(self, fichier):
        self.lien=fichier
    
    def type(self):
    # renvoie "HTML" ou "PDF"
    #Si c'est PDF self.type="PDF" sinon "HTML"
        if self.lien[len(self.lien)-1]=="f" and self.lien[len(self.lien)-2]=="d" and self.lien[len(self.lien)-3]=="f":
            return "PDF"
        else: return "HTML"
        
    def text(self):
    #renvoie le texte épuré de la page ou PDF
        #Pour un document PDF
        if (self.type=="PDF"):
            ...
        # Pour un document HTML    
        elif (self.type=="HTML"):
            url = self.lien
            html = urllib.urlopen(url).read()
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
            print("il faudrait faire la fonction type avant svp")
            return 0
        