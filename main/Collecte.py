from Ressource import Ressource

class Collecte:
    """
    Prend 2 liens HTML ou adresses de répertoire PDF, récupère les ressources en leurs extrayant leur texte 
    et renvoie une liste de contenus sous forme d'un tableau de longueur 2.
    """

    def __init__(self,tableau):
        """
        On enregistre les 2 liens ou adresses de répertoire distinctement afin de les traiter.
        """
        self.lien1=tableau[0]
        self.lien2=tableau[1]
    
    def run(self):
        """
        On recupère les ressources des liens ou adresses et on leurs extrait le texte pertinant.
        """
        #Manipulation sur le lien 1
        self.text1=Ressource(self.lien1)
        self.text1.type()
        self.text1=self.text1.text()

        #Manipulation sur le lien 2
        self.text2=Ressource(self.lien2)
        self.text2.type()
        self.text2=self.text2.text()
        
        #Création d'une variable incluant les 2 textes
        self.textes=[self.text1,self.text2]

    def  content(self):
        """
        On renvoie une liste de contenus sous forme d'un tableau de dimension 2.
        """
        return(self.textes)