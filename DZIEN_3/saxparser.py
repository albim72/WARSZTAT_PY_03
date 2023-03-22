import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ""
        self.id=""
        self.tytul=""
        self.rok=""
        self.kraj=""
        self.czas_t=""
        self.gatunek=""

    def startElement(self,tag,attributes):
        self.currentdata = tag
        if tag == "film":
            print("______________film_______________")

    def endElement(self,tag):
        if self.currentdata == "id_filmu":
            print(f"indentyfikator filmu: {self.id}")
        elif self.currentdata == "tytul":
            print(f"tytuł filmu: {self.tytul}")
        elif self.currentdata == "rok":
            print(f"rok produkcji filmu: {self.rok}")
        elif self.currentdata == "kraj":
            print(f"kraj produkcji filmu: {self.kraj}")
        elif self.currentdata == "czas_trwania":
            print(f"czas trwania filmu: {self.czas_t}")
        elif self.currentdata == "gatunek":
            print(f"gatunek filmu: {self.gatunek}")

    def characters(self,content):
        if self.currentdata == "id_filmu":
            self.id = content
        elif self.currentdata == "tytul":
            self.tytul = content
        elif self.currentdata == "rok":
            self.rok = content
        elif self.currentdata == "kraj":
            self.kraj = content
        elif self.currentdata == "czas_trwania":
            self.czas_t = content
        elif self.currentdata == "gatunek":
            self.gatunek = content

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
handler = UchwytFilmu()
parser.setContentHandler(handler)
parser.parse("filmy.xml")
