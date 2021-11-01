from Ressource import Ressource


class Collecte:
    """
    Prend 2 liens HTML ou adresses de répertoire PDF, récupère les ressources en leurs extrayant leur texte 
    et renvoie une liste de contenus sous forme d'un tableau de longueur n.
    """

    def __init__(self,tableau):
        """
        On enregistre les n liens ou adresses de répertoire distinctement afin de les traiter.
        """
        self.liens=tableau
    
    def run(self):
        """
        On recupère les ressources des liens ou adresses et on leurs extrait le texte pertinant.
        """
        self.textes=[]
        for i in range(len(self.liens)):
            texte=Ressource(self.liens[i])
            texte.type()
            self.textes.append(texte.text())



    def  content(self):
        """
        On renvoie une liste de contenus sous forme d'un tableau de dimension n.
        """
        return(self.textes)