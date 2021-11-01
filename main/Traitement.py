from Collecte import Collecte
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Traitement:    

    def load(self,tableau):
    #génère plusieurs page ou PDF
        self.liens=tableau
        une_collecte=Collecte(self.liens)
        une_collecte.run()
        self.textes=une_collecte.content()
    
    def run(self):
        #génère le résultat
        self.nombre=[]
        for i in range(len(self.textes)):
            split=self.textes[i].split()
            self.nombre.append(len(split))

    def show(self):
        #affiche le résultat
        return print(self.nombre)