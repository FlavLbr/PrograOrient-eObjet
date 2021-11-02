from Collecte import Collecte
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Traitement:   

    """
    Cette classe consiste à compter le nombre de mot de chaque texte contenue dans un tableau de liens.
    Son but à été choisi arbitraiement par nous afin d'avoir un main plus propre.
    """ 

    def load(self,tableau):
        """
        On effectue une collecte à partir de plusieurs lien saisie dans un tableau.
        """
        self.liens=tableau
        une_collecte=Collecte(self.liens)
        une_collecte.run()
        self.textes=une_collecte.content()
    

    def run(self):
        """
        On compte le nombre de mot contenu dans chaque texte grâce à la fonction split().
        """
        self.nombre=[]
        for i in range(len(self.textes)):
            split=self.textes[i].split()
            self.nombre.append(len(split))

    def show(self):
        """
        On retourne un tableau contenant le nombre de mot de chaque texte respectifs.
        """
        return print(self.nombre)