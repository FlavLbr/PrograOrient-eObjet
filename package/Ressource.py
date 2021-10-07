from PyPDF2 import PdfFileReader
import urllib
from bs4 import BeautifulSoup

class Ressource:
    def __init__(self, fichier):
        self.lien=fichier
    
    def type(self):
    # renvoie "HTML" ou "PDF"
    #Si c'est PDF self.type=0 sinon 1
        ...
    
    def text(self):
    #renvoie le txte épuré de la page ou PDF
        if (self.type==0):
            self.doc= PdfFileReader(open(self.lien, 'rb'))
            pdftext = ""
            for page in range(self.doc.numPages):
                pageObj = self.doc.getPage(page)
                pdftext += pageObj.extractText().replace('\n','')
            return pdftext
            
        elif (self.type==1):
            url = self.lien
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html)
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            # get text
            htmltext = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in htmltext.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            htmltext = '\n'.join(chunk for chunk in chunks if chunk)
            return htmltext
        else:
            print("il faudrait faire la fonction type avant svp")
            return 0
        