import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Veriyi içeriye aktar
veri = pd.read_csv("olimpiyatlar.csv")

# Sütun isimlerinin düzenlenmesi
veri.rename(columns={
    "ID": "id",
    "Name": "isim",
    "Sex": "cinsiyet",
    "Age": "yas",
    "Height": "boy",
    "Weight": "kilo",
    "Team": "takim",
    "NOC": "uok",
    "Games": "oyunlar",
    "Year": "yil",
    "Season": "sezon",
    "City": "sehir",
    "Sport": "spor",
    "Event": "etkinlik",
    "Medal": "madalya"
}, inplace=True)

# Gereksiz sütunların çıkarılması
veri.drop(["oyunlar"], axis=1, inplace=True)

# Boy ve kilo sütununda bulunan kayıp verileri dolduralım (etkinlik ortalaması)
essiz_etkinlik = pd.unique(veri.etkinlik)
boy_kilo_list = ["boy", "kilo"]
veri_gecici = veri.copy()

"""
for e in essiz_etkinlik:
    etkinlik_filtresi = veri_gecici["etkinlik"] == e
    veri_filtreli = veri_gecici.loc[etkinlik_filtresi]

    for s in boy_kilo_list:
        ortalama = np.mean(veri_filtreli[s])
        if not np.isnan(ortalama):
            veri_gecici.loc[etkinlik_filtresi, s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri[s])
            veri_gecici.loc[etkinlik_filtresi, s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)

veri = veri_gecici.copy()

# Yaş sütunundaki kayıp verileri dolduralım (cinsiyet ve spor ortalaması)
essiz_cinsiyet = pd.unique(veri.cinsiyet)
essiz_spor = pd.unique(veri.spor)

for c in essiz_cinsiyet:
    for s in essiz_spor:
        cinsiyet_spor_filtresi = (veri["cinsiyet"] == c) & (veri["spor"] == s)
        veri_filtreli = veri.loc[cinsiyet_spor_filtresi]
        ortalama = np.mean(veri_filtreli["yas"])

        if not np.isnan(ortalama):
            veri.loc[cinsiyet_spor_filtresi, "yas"] = veri_filtreli["yas"].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri["yas"])
            veri.loc[cinsiyet_spor_filtresi, "yas"] = veri_filtreli["yas"].fillna(tum_veri_ortalamasi)

# Madalya almayan sporcuları çıkaralım
veri = veri[~veri["madalya"].isnull()]

# Temizlenmiş veriyi kaydedelim
veri.to_csv("olimpiyatlar_temizlenmis.csv", index=False)

# Tek değişkenli veri analizi
sayisal_degisken = ["yas", "boy", "kilo", "yil"]

def plotHistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins=85, color="orange")
    plt.xlabel(degisken)
    plt.show()

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
"""

#korelasyon: 
numeric_correlation=veri.loc[:,["yas","boy","kilo"]].corr()
print(numeric_correlation)

veri_gecici=veri.copy()
veri_gecici=pd.get_dummies(veri_gecici,columns=["madalya"]) # madalya icin sayilar atamaliyiz cunku korelasyonu string ile yapamayiz

#pivot tabla
#madalya alan sporcuların cinsiyetlerine gore boy kilo yas ortalamalarina bakalim
veri_pivot=veri.pivot_table(index="madalya",
                            columns="cinsiyet",
                            values=["boy","kilo","yas"],
                            aggfunc={"boy":np.mean,
                                     "kilo": np.median,
                                     "yas": [np.min,np.max,np.std]})
print(veri_pivot)

"""
# takımlara ve cinsiyete gore alinan madalya sayilarinin toplami max min degerleri
veri_pivot2=veri.pivot_table(index="takim",
                             columns="cinsiyet",
                             values=["Gold","Silver","Bronze"],
                             aggfunc={"Gold":[np.sum],
                                      "Silver":[np.sum],
                                      "Bronze":[np.sum]})
print(veri_pivot2)
"""
print(veri.columns)