#preprocessing: verinin training icin hazir hale getirilmesi
#EDA(kesifsel veri analizi): outlier tespiti,feature extraction,correlation
#.csv veya .txt formatinda bir dosyamiz varsa bunlarin import edilmesi icin pandas kutuphanesi kullanilir
import pandas as pd

# DataFrame için dictionary tanımlamalıyız
dictionary = {
    "isim": ["ali", "veli", "kenan", "murat", "ayse", "hilal"],
    "yas": [15, 34, 24, 32, 33, 45],
    "maas": [100, 200, 300, 400, 500, 600]
}

# DataFrame oluşturma
veri = pd.DataFrame(dictionary)
print(veri)

print(veri["yas"]) #sadece yas sutununu alir
veri["sehir"]=["istanbul","ankara","izmir","bursa","adiyaman","trabzon"] #yeni sutun ekleme
print(veri["sehir"])
veri["maas_zamli"] = veri["maas"]*120/100 #yuzde 20 zamli maas olusturma
print(veri["maas_zamli"])
print(veri.loc[:, "yas"]) #[satir,sutun]
print(veri.loc[:3, "yas"]) #yaslarda 0-1-2-3 (3 dahil) yazdirir
print(veri.loc[0:2, ['yas','sehir']])
print(veri.loc[0:2, 'yas':'sehir']) #loc olunca sayi yazamiyoruz sutun kismina, sayi yazmak icin iloc kullaniriz
print(veri.iloc[0:2,1]) #iloc'ta 2 dahil degil!!! 0-1
print(veri.iloc[0:2,1:2]) #usttekiyle ayni
print(veri.iloc[2:4,1:2])

print(veri.iloc[3,0:2])
print(veri.loc[3,'isim':'yas'])


print(veri.iloc[4:,1:3])
print(veri.loc[4:,"yas":"maas"])

print(veri.iloc[1,0],veri.iloc[4,1])
print(veri.loc[1,"isim"],veri.loc[4,"yas"])


print("***************** veri head ***********")
print(veri.head())  # İlk beş satır

print("***************** veri tail ***********")
print(veri.tail())  # Son beş satır

print("***************** veri columns ***********")
print(veri.columns)  # Sütun isimleri

print("***************** veri info ***********")
veri.info()  # `info()` doğrudan çıktı verir, birleştirilemez.

print("***************** veri describe ***********")
print(veri.describe())  # Sayısal sütunlar için özet istatistikler


import pandas as pd
dictionary = {
    "isim": ["ali", "veli", "kenan", "murat", "ayse", "hilal"],
    "yas": [15, 34, 24, 32, 33, 45],
    "sehir": ["izmir","ankara","konya","ankara","antalya","trabzon"]
}
veri = pd.DataFrame(dictionary)

#**********filtreleme*******
filtre1=veri["yas"]>22
print(filtre1)

filtrelenmis_veri=veri[filtre1]
print(filtrelenmis_veri) #sadece yasi 22den buyuk olanlari yazdirir
filtre2=veri["sehir"]=="ankara"

veri[filtre1 & filtre2]
print(veri)

""""
#maas sutunu ekle
#yas/maas orani sutunu ekle
#yas/maas sutunu icin ortalamayi print ettir
#ankarada yasayanlarin ortalama yasini bul
#ankarada yasayanlarin icinden en yuksek maasi bul
"""

import pandas as pd
dictionary = {
    "isim": ["ali", "veli", "kenan", "murat", "ayse", "hilal"],
    "yas": [15, 34, 24, 32, 33, 45],
    "sehir": ["izmir","ankara","konya","ankara","antalya","trabzon"]
}
veri = pd.DataFrame(dictionary)

veri["maas"] = [100,2323,23232,2322,3322,232332]
print(veri)

veri["yas_maas_orani"]=veri["yas"]/veri["maas"]
print(veri)
import numpy as np
#ortalama yas maas orani
print(np.mean(veri["yas_maas_orani"]))

#ankarada yasayanlarin ortalama maasi
print(veri[veri["sehir"]=="ankara"]["yas"].mean())

#ankarada yasayanlarin icinden en yuksek maas
print(veri[veri["sehir"]=="ankara"]["maas"].max())

#for dongusu ile max maas alanin ismi
max_maas=0
max_isim=""


# Ankara'da yaşayanlar için yeni bir DataFrame (reset_index ile indeksi sıfırlama)
ankarada_yasayanlar = veri[veri["sehir"] == "ankara"].reset_index(drop=True)
for i in range(len(ankarada_yasayanlar)):
    if ankarada_yasayanlar["maas"][i]>max_maas:
        max_maas=ankarada_yasayanlar["maas"][i]
        max_isim=ankarada_yasayanlar["isim"][i]
print(max_isim)
