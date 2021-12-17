#!/bin/env python3
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup as bs
import fitz
import io
import requests


class Traitement:   
    """
        Cette classe nous serre à traiter les documents html et pdf et à leurs extraire les images sur un document html.
    """ 

    def load_html(liste_image,file_name):
        """
            On enregistre les images sur un document html que nous avons créé sur un repertoire demandé. 
        """
        Creation_fichier=Path(os.path.join(file_name,'Extraction_images_documents.html'))
        Creation_fichier.touch(exist_ok=True)
        with open(Creation_fichier,mode='w+') as html:
            html.write('<html>')
            for url_img in liste_image:
                html.write(f'<img src={url_img} />')
            html.write('</html>')
    

    def enregistrement_image_html(url):
        """
            On extrait les images d'un document html et on les enregistre sous forme d'une liste de lien correspondant à chaque images.
        """
        def is_valid(url):
                    
                    parsed = urlparse(url)
                    return bool(parsed.netloc) and bool(parsed.scheme)

        def get_all_images(url):
                    
                    soup = bs(requests.get(url).content, "html.parser")
                    urls = []
                    for img in tqdm(soup.find_all("img"), "Extracting images"):
                        img_url = img.attrs.get("src")
                        if not img_url:
                            continue
                        img_url = urljoin(url, img_url)
                        try:
                            pos = img_url.index("?")
                            img_url = img_url[:pos]
                        except ValueError:
                            pass
                        if is_valid(img_url):
                            urls.append(img_url)
                    return urls
        return get_all_images(url)


    def enregistrement_image_pdf(url,file_name,i):
        """
            On extrait les images d'un document pdf, on les télécharge et on enregistre sous forme d'une liste de chemin correspondant à chaque images.
        """
        r = requests.get(url)
        pdf_content = r.content
        doc = fitz.open(stream=io.BytesIO(pdf_content),filetype='pdf')
        listeimage=[]
        for j in range(len(doc)):
            for img in doc.getPageImageList(j):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                        
            if pix.n < 5:       
                pix.writePNG(f'{file_name}/document{i+1}_image_pdf{j}.jpg')
                listeimage.append(f'{file_name}/document{i+1}_image_pdf{j}.jpg')

            else:              
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(f'{file_name}/document{i+1}_image_pdf{j}.jpg')
                listeimage.append(f'{file_name}/document{i+1}_image_pdf{j}.jpg')
                pix1 = None
            pix = None
        return listeimage
        
