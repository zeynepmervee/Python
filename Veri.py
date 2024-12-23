import pandas as pd

# veriyi iceriye aktar
veri = pd.read_csv("olimpiyatlar.csv")
veri_head = veri.head(15)
"""
veride nan degerler var, cikart veya doldur
games columnı gereksiz, veriden drop
her sporcu madalya almamis: madalya nan = madalya alamamis
id gereksiz
bir kisi iki takima katilmis? 1900 yilinda orada iki ulke varmiydi
ülke kısaltması yada takim gereksiz.
1920 den oncesi acaba guvenilir veri mi?
"""

veri.info()

# sutun isimlerinin duzenlenmesi
column = veri.columns
veri.rename(columns = {
    "ID" : "id",
    "Name" : "isim",
    "Sex" : "cinsiyet",
    "Age" : "yas",
    "Height" : "boy",
    "Weight" : "kilo",
    "Team" : "takim",
    "NOC": "uok", # ulusal olimpiyat komite
    "Games" : "oyunlar",
    "Year" : "yil",
    "Season" :"sezon",
    "City" : "sehir",
    "Sport" : "spor",
    "Event" : "etkinlik",
    "Medal" : "madalya"
    }, inplace = True)

# gereksiz/yararsiz verinin cikarilmasi
veri = veri.drop(["oyunlar"], axis = 1) 
veri_head = veri.head(15)
veri_duplicated = veri[veri.duplicated()] # birbirini tekrarlayan veri

# %% kayip veri problemi

"""
boy ve kilo sutununda bulunan kayip verileri dolduralim (etkinlik ortalamasi) ?
ortalama veya  medyan? bu veri seti icin fark etmez.
madalya alamayan sporculari veri setinden cikartalim

"""
# ortalama veya  medyan?
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.hist(veri.boy, bins = 100)
plt.title("boy")

plt.figure()
plt.hist(veri.kilo, bins = 100)
plt.title("kilo")

describe = veri.describe()

# boy ve kilo sutununda bulunan kayip verileri dolduralim (etkinlik ortalamasi)

# unique etkinliklerin ve sayisinin bulunmasi
essiz_etkinlik = pd.unique(veri.etkinlik) 

veri_gecici = veri.copy() # gercek veriyi kaybetmemek icin kopyala

boy_kilo_list = ["boy", "kilo"] # kayip veri sorunu olan sutunlar

for e in essiz_etkinlik: # etkinlik ozelinde iterasyona basla
    
    # etkinlik filtresi olustur
    etkinlik_filtresi = veri_gecici.etkinlik == e

    # veriyi etkinlige gore filtrele
    veri_filtreli = veri_gecici[etkinlik_filtresi]
    
    # boy ve kilo icin etkinlik ozelinde ortalam bul
    for s in boy_kilo_list:
        
        ortalama = np.mean(veri_filtreli[s])
        
        if np.isnan(ortalama) == False:
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri[s])
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)

    veri_gecici[etkinlik_filtresi] = veri_filtreli

veri = veri_gecici.copy()
veri.info()

# yas da bulunan kayip veri sorununu cinsiyet ve spora gore dolduralim
essiz_cinsiyet = pd.unique(veri.cinsiyet) 
essiz_spor = pd.unique(veri.spor) 

veri_gecici = veri.copy() # gercek veriyi kaybetmemek icin kopyala

for c in essiz_cinsiyet: 
    for s in essiz_spor:
    
        # cinsiyet ve spor filtresi olustur
        cinsiyet_spor_filtresi = np.logical_and(veri_gecici.cinsiyet == c, veri_gecici.spor == s)
    
        # veriyi etkinlige gore filtrele
        veri_filtreli = veri_gecici[cinsiyet_spor_filtresi]
        
        ortalama = np.mean(veri_filtreli["yas"])
        
        if np.isnan(ortalama) == False:
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri["yas"])
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(tum_veri_ortalamasi)

        veri_gecici[cinsiyet_spor_filtresi] = veri_filtreli

veri = veri_gecici.copy()
veri.info()

# madalya alamayan sporcularin bulunmasi
madalya_degiskeni = veri.madalya
null_sayisi = pd.isnull(madalya_degiskeni).sum() # madalya alamayan sporcu sayisi

madalya_degiskeni_filtresi = pd.isnull(madalya_degiskeni)

veri = veri[~madalya_degiskeni_filtresi]

veri.to_csv("olimpiyatlar_temizlenmis.csv", index = False)

# %% tek degiskenli veri analizi
import matplotlib.pyplot as plt

def plotHistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins =85, color = "orange")
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas", "boy", "kilo", "yil"]
for degisken in sayisal_degisken:
    plotHistogram(degisken)


def plotBox(degisken):
    plt.figure()
    plt.boxplot(veri[degisken])
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas", "boy", "kilo"]
for degisken in sayisal_degisken:
    plotBox(degisken)