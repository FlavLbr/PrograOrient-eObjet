#!/bin/env python3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import fitz
import io
import requests
import re
from bs4 import BeautifulSoup as bs
from Collecte import Collecte
from Ressource import Ressource
import urllib.request
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

class Prisme:
    """
    Prisme prend un fichier txt, traite les liens présent dans le ficher et en fait un nuage de mot.
    """

    def __init__(self,type):
        """
        Il va y avoir 2 types principaux qui seront traités différement, Nuage et Image. Pour l'instant nous traiton que Nuage.
        """
        self.type=type 

    def run(self,fichier):
        """
        On lance le traitement sur des ressources web ligne par ligne référencées dans fichier txt. On retourne un tableau de 
        textes.
        """
        lien = open(fichier,"r")
        liens=lien.readlines()
        self.liens=[]
        for i in liens:
                self.liens.append(i.replace("\n",""))
        textes= Collecte(self.liens)
        textes.run()
        self.textes=textes.content()
        return self.textes
    
    def show(self):
        """
        On traite les mots afin de sortir un nuage de mots à l'utilisateur qui sera ouvert texte par texte chacun son tour 
        et dans l'ordre des liens.
        """
        if self.type=='Nuage' or self.type=='nuage':
            for i in range (len(self.textes)):
                wc = WordCloud(max_font_size=40).generate(self.textes[i])
                plt.imshow(wc, interpolation='bilinear')
                plt.axis("off")
                plt.show()
        
        elif self.type=='Image' or self.type=='image':
            for i in range (len(self.liens)):
                t=Ressource(self.liens[i])
                t=t.type()
                if t=="HTML":
                    def is_valid(url):
                    
                        parsed = urlparse(url)
                        return bool(parsed.netloc) and bool(parsed.scheme)

                    def get_all_images(url):
                    
                        soup = bs(requests.get(url).content, "html.parser")
                        urls = []
                        for img in tqdm(soup.find_all("img"), "Extracting images"):
                            img_url = img.attrs.get("src")
                            if not img_url:
                            # if img does not contain src attribute, just skip
                                continue
                            # make the URL absolute by joining domain with the URL that is just extracted
                            img_url = urljoin(url, img_url)
                            try:
                                pos = img_url.index("?")
                                img_url = img_url[:pos]
                            except ValueError:
                                pass
                            # finally, if the url is valid
                            if is_valid(img_url):
                                urls.append(img_url)
                        return urls

                    url_image=get_all_images(self.liens[i])

                    
                    for i in range (len(url_image)):
                        urllib.request.urlretrieve(url_image[i], "Image.jpg")
                
                elif t=="PDF":
                    r = requests.get(self.liens[i])
                    content_type = r.headers.get('content-type')
                    pdf_content = r.content

                    doc = fitz.open(stream=io.BytesIO(pdf_content),filetype='pdf')
                    for i in range(len(doc)):
                        for img in doc.getPageImageList(i):
                            xref = img[0]
                            pix = fitz.Pixmap(doc, xref)
                        if pix.n < 5:       # c'est GRAY or RGB
                            pix.writePNG("p%s-%s.png" % (i, xref))
                        else:               # CMYK: convert to RGB first
                            pix1 = fitz.Pixmap(fitz.csRGB, pix)
                            pix1.writePNG("p%s-%s.png" % (i, xref))
                            pix1 = None
                        pix = None
                
            
                    
                