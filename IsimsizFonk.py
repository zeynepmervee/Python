def old_summary(a,b):
    return a+b
print(old_summary(4,5))

new_summary=lambda a,b: a+b #boyle de fonk tanimlanabilir
print(new_summary(4,5)) #a ve b'ye bagli ve a+b işlevini yerine getiren fonksiyon


sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)] #icinde tuple'lar olan liste
print(sirasiz_liste)

sorted(sirasiz_liste, key= lambda x:x[1]) 

#iki dizideki elemanlari carpan dongu OOP
a=[1,2,3,4]
b=[2,3,4,5]
ab=[]
print(range(0, len(a))) #range(0, 4) ciktisi verir

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
print(ab)
#ayni uygulamayi daha kolay yapabiliriz FP
import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
print(a*b)

#**********************map***************************
liste=[1,2,3,4,5]
for i in liste:
    print(i+10)
print(  list(map(lambda x: x+10,liste))  )
#map fonksiyonu verilen fonksiyonun icinde (liste) tanimlanacak isimsiz fonskiyonu(lambda) calistirmamizi saglar

#*********************filter***************************
liste=[1,2,3,4,5,6,7,8,9,10]
print(  list(filter(lambda x:x%2==0,liste))  )
#soldaki sarti saglayan elemanlari (cift sayilari) sagdaki fonksiyondan secip ekrana yazdirir

#******Liste elemanları sırayla toplanarak ***************reduce***************************
from functools import reduce
liste=[1,2,3,4]
print(  reduce(lambda a,b: a+b, liste)  )
#Liste elemanları ikili olarak sırayla toplanarak 10 bulunur


#*********************Modul***************************
import Fonksiyonlar as F
F.kare_al(3) #kendi yazdigimiz fonksiyonlar modulunu burada kullandik

from Fonksiyonlar import fonk #sadece fonk fonksiyonunu almak icin