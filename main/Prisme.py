from wordcloud import WordCloud

class Prisme:

    def __init__(self,type):
    # crée le prisme générateur d'un nuage de mots
        self.type=type #soit nuage siut image

    def run(self,fichier):
    # lance le traitement sur des ressources web référencées dans fichier
        ...
    
    def show(self):
    # visualise le nuage de mots
        if self.type=='Nuage' or self.type=='nuage':
            wc = WordCloud()
            wc.generate(self.text)