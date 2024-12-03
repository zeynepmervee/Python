class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili=0
    bildigi_diller=[]
print(VeriBilimci.sql)
VeriBilimci.sql="Hayir" #guncelledik

ali=VeriBilimci() #nesne
ali.bildigi_diller.append("Python") #ali nesnesinin bildigi dillere python eklendi
print(ali.bildigi_diller)

veli=VeriBilimci()
print(veli.bildigi_diller) #veliye de python eklenmis.


########################################################################


class VeriBilimci():
    def __init__(self): #************ornek***
        self.bildigi_diller=["C++"]
ali=VeriBilimci()
ali.bildigi_diller.append("Python") 
print(ali.bildigi_diller)

veli=VeriBilimci()
print(veli.bildigi_diller) #burada velinin bildigi dillerde python yazmaz.
#cunku ****lı yerde __init__(self) kullandik
print(VeriBilimci().bildigi_diller) #burada da python eklenmedi


########################################################################


#ornek metotlari
class VeriBilimci():
    calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''
    def dil_ekle(self,yeni_dil): #orneklerin bildigi dilleri otomatik ekleyen metot
        self.bildigi_diller.append(yeni_dil)
        
ali=VeriBilimci()
print(ali.bildigi_diller)
VeriBilimci.dil_ekle(ali,"Java")
ali.dil_ekle("C")
print(ali.bildigi_diller)
