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

