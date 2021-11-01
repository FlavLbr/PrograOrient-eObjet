from Collecte import Collecte

class Traitement:    

    def load(self,tableau):
    #génère plusieurs page ou PDF
        self.liens=tableau
        une_collecte=Collecte(self.liens)
        une_collecte.run()
        self.textes=une_collecte.content()
        return self.textes
    
    def run(self):
        #génère le résultat
    
    def show(self):
        #affiche le résultat
        