#!/bin/env python3
# LEBRETON Flavien / GERAULT Thomas 
from Prisme import Prisme

lien_fichier=input(f"\nBonjour à vous! Et bienvenue sur Prisme! \n\nPouvez-vous nous renseigner le lien du fichier où les urls sont enregistés (1 lien par ligne): ")
choix=input("Maintenant veuillez entrer le choix du traitement (pour un nuage de mots entrez 'Nuage' et pour les images entrez 'Image'): ")
if choix=="Nuage": 
    concatenation=input("Voulez vous un nuage de mot global ou par document? (entrez 'ON' pour un seul nuage de mots et 'OFF' sinon): ")
    nombre_mot=int(input("Combien voulez vous de mots dans le nuage de mots ?  "))
fichier_enregistement=input("Veuillez renseigner le chemin du fichier où Prisme doit enregistrer le HTML: ")
print("C'est partie!")

un_prisme = Prisme(choix)      
un_prisme.run(lien_fichier)
if choix=="Nuage":
    un_prisme.show(fichier_enregistement,concatenation,nombre_mot)
else:
    un_prisme.show(fichier_enregistement)

