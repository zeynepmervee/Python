liste=["sut","yumurta","ekmek"]
print(liste)

listeFiyat=[10,20,30]
type(listeFiyat)
liste[0]
print(liste[len(liste)-1]) #len'den (3) bir kucuk olunca son eleman (2) oluyor
print(liste[-1]) #son eleman
print(liste[0:2]) #0 dahil 2 dahil degil. [:2] yazsak da olurdu
liste.append(2)
print(liste)
liste.remove("yumurta") #buldugu ilk yumurtayi kaldirir. 2 tane varsa sadece biri cikarilir
print(liste)
liste.reverse() #listeyi ters cevirme
print(liste)


print("**********TUPLELAR**********")
tupleSayi=(1,2,3,3,4,5,6) #tuplelari degistiremeyiz
print(tupleSayi[-2])
print(tupleSayi[-2])
print(tupleSayi.count(3)) #tupleda kac tane 3 var

print("**********DICTIONARY********** cok kullaniliyor!!!")
#anahtar-deger ciftleri
dictionary={"anahtar":10,"key":"ankara"}
print(dictionary)
sehirPlaka={"Istanbul":34,
            "izmir":35,
            "konya":42
            }
print(sehirPlaka)
print(sehirPlaka.keys())
print(sehirPlaka["izmir"])

parameters={"weights":[],
            "bias":[],
            "learning_rate":0,
            "model_name":"model1"
            }
list_parameters = []
list_parameters.append(parameters)
print("***********TIP DONUSUMLERI*************")
sayi=10
kesirli=10.2
metin="19"
metin_int=int(metin)
print(type(metin_int))
kesirli_str=str(kesirli)
print(type(kesirli_str))
sayi_float=float(sayi)
print(sayi_float)


