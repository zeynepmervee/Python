import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# veriyi iceriye aktar
veri = pd.read_csv("olimpiyatlar.csv")

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

# Yas sutunu secimi, sütun adları değiştirildikten sonra yapılmalı
yas = veri.yas.dropna()
# Histogram cizimi
plt.hist(yas, bins=100)

# 1. ceyrek
Q1 = np.percentile(yas, 25)

# 3. ceyrek
Q3 = np.percentile(yas, 75)

# ceyrekler acikligi
IQR = Q3 - Q1

# aykiri deger tespiti icin IQR degerinin bir carpan ile carpılması
outlier_step = 1.5 * IQR

ust_sinir = Q3 + outlier_step
alt_sinir = Q1 - outlier_step
# Bu sınırların dışında kalan değerler aykırı kabul ediliyor.

# Aykırı değerlerin tespiti
yas_aykirilar = yas[(yas < alt_sinir) | (yas > ust_sinir)]
print("Aykiri Degerler:")
print(yas_aykirilar)

print("Minimum Yas:", yas.min())
print("Maksimum Yas:", yas.max())
print("Alt Sinir:", alt_sinir)
print("Ust Sinir:", ust_sinir)


plt.show()


