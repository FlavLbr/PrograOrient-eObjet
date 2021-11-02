from urllib.request import urlopen
#pip install beautifulsoup4
from bs4 import BeautifulSoup
#pip install pdfplumber
import pdfplumber


class Ressource:
    """ 
    Ressource prend un lien pour un HTML ou un adresse de répertoire pour un pdf, retourne si c'est un PDF ou un HTML
    avec la fonction type et retourne l'adresse sous forme dans texte avec la fonction text.   
    """

    def __init__(self, fichier):
        """
        On enregistre le lien dans un self afin de l'utiliser dans les 2 fonctions.
        """
        self.lien=fichier
    
    def type(self):
        """
        On retourne si le lien ou l'adresse est un PDF ou un document HTML et enregistre le type sur une 
        variable self.
        """
        if self.lien[len(self.lien)-1]=="f" and self.lien[len(self.lien)-2]=="d" and self.lien[len(self.lien)-3]=="p":
            self.type="PDF"
            return "PDF"
        else:
            self.type="HTML" 
            return "HTML"

        
    def text(self):
        """
        On renvoi un texte épuré dans document HTML ou d'un PDF. Attention! Il faut faire le .type avant afin 
        que le self.type soit définit
        """
        
        if (self.type=="PDF"):
            #Fonction utilisé pour un document PDF
            with pdfplumber.open(self.lien) as pdf:
                first_page = pdf.pages[0]
                return(first_page.extract_text())
            """ca doit imprimer que la premier page donc voir si boucle for imprime plusieurs page"""
    
        elif (self.type=="HTML"):
            #Fonction utilisé pour un document HTML
            url = self.lien
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

        else:
            #demande à l'utilisateur d'utiliser la fonction type avant afin d'avoir une valeur au self.type
            print("Il faudrait faire la fonction type avant svp")
            return 0
        