from Ressource import Ressource

une_ressource = Ressource("http://news.bbc.co.uk/2/hi/health/2284783.stm")
r=une_ressource.type() 
print(r)
r=une_ressource.text()
print(r)
