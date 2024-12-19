import pandas as pd
import numpy as np
dictionary = {
    "isim": ["ali", "veli", "kenan", "murat", "ayse", "hilal"],
    "yas": [15, 34, 24, 32, 33, 45],
    "sehir": ["izmir","ankara","konya","ankara","antalya","trabzon"]
}
veri = pd.DataFrame(dictionary)
def yas10YilSonrasi(age):
    output= age +10
    return output

def yasCarpim(df):
  if df.sehir == "ankara":
    return df.yas*2
  else:
    return df.yas*5
     
print(veri.apply(yasCarpim,axis=1)) #axis=1 satır satır gonderir

# dataframe de bulunan insanlarin isimlerinin uzunlugu == 5 ise yeni yasi 2 ile varpalim
# eger isim uzunlugu == 4 ise 3 ile carpalim else 4 ile carpalim
def isimUzunlugu(row):
  if len(row.isim) == 5:
    return row.yas * 2
  elif len(row.isim) == 4:
    return row.yas * 3
  else: return row.yas * 4
print(veri.apply(isimUzunlugu, axis = 1)) # veriyi satir satir isim uzunlugna gonder


import pandas as pd
sozluk1 = {"isim": ["ali", "veli"],
           "yas": [15, 16]}
veri1 = pd.DataFrame(sozluk1)
print(veri1)
sozluk2 = {"isim": ["murat", "ayse"],
           "yas": [32, 33]}
veri2 = pd.DataFrame(sozluk2)
print(veri2)
sozluk3 = {"isim": ["zeynep", "merve"],
           "yas": [47, 83]}
veri3 = pd.DataFrame(sozluk3)

# concat
veri_dikey = pd.concat([veri1, veri2], axis = 0)
print(veri)


veri_dikey = pd.concat([veri1, veri3], axis = 0, ignore_index=True)
# veri_dikey.reset_index(drop=True, inplace=True)
print(veri_dikey)

# concat
veri_yatay = pd.concat([veri1, veri2], axis = 1)
print(veri_yatay)



