import numpy as np #numpy kullan np takma adiyla

#numpy array
liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dizi = np.array(liste)
print(dizi)

#array boyutu
print(dizi.shape) #15x1'lik bir vektor

#15x1lik arrayi 3x5lik matrise cevirme
dizi2 = dizi.reshape(3,5)
print(dizi2)
print("shape:",dizi2.shape) #shape (3,5) ciktisi verir. 3 satir 5 sutun
print("dimension:", dizi2.ndim)
print("size:",dizi2.size)
print("type:",type(dizi2))

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

#sifirlardan olusan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

bir_dizi = np.ones((3,2))
print(bir_dizi)

bos_dizi=np.empty((2,4)) 
print(bos_dizi)

#arrange(x,y,basamak) xden  baslar y'ye kadar (y dahil degil) gider.
#basamak buyuklugunde artarak ilerler

dizi_aralik=np.arange(10,50,8)
print(dizi_aralik)

#linspace (x,y,basamak) xden  baslar y'ye kadar (y dahil)
#basamak kadar sayiya boler
dizi_bosluk=np.linspace(10,50,42) #10-50 arasini 42 tane sayiya bolduk
print(dizi_bosluk)

#Numpy temel operasyonlari
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print("Toplama:" , a+b)
print("Cikarma:" , a-b)
print("Dizinin kendisiyle carpimi:" , a*a)

#filtreleme
a=np.array([1,2,3])
print(a<2) #a arrayinin icinde bulunan 2den kucuk mu? [ True False False]

#matris carpimi
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[7,8,9]])
print(a.dot(b.T)) #transpoz alınır. yani satir ve sutun yerleri degisir

a=np.array([[1,2,3],[4,5,6]])
print(sum(a)) #[5 7 9]
print(np.sum(a)) #21
print(a.sum()) #21
print(a.max()) #6
print(np.max(a)) #6
print(a.sum(axis=1)) #satir satir toplama. [ 6 15]
print(a.sum(axis=0)) #sutun sutun toplama. [5 7 9]

print(np.sqrt(a)) #karekoku
print(np.square(a)) #karesi
print(a**2) #karesi

import numpy as np
#rastgele sayi uretme
rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)
rastgele_dizi=np.random.normal(0,1,5) #0 ortalamalı 1 standart sapmalı 5 adet deger uretir
print(rastgele_dizi)

import numpy as np
dizi=np.array([1,2,3,4,5,6,7])
print(dizi[1:5])
print(dizi[::-1]) #dizinin tersini alir

dizi2D=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D[1,2]) #8

#satir,sutun,kacinci sutuna kadar
print(dizi2D[:, 2:4]) #tum satirlari aldik satir kisminda : var diye
                        #2. sutun dahil 3. sutun dahil degil

print(dizi2D[1, 2:4]) #1 indisli satiri 2. sutundan 4. sutuna kadar yazdirir.
                        #2. sutun dahil 4. sutun dahil degil


#shape manipulation
import numpy as np
dizi2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D.shape) 
dizi2D_shape=dizi2D.shape #tupledir.
print(dizi2D.reshape(dizi2D_shape[0]*dizi2D_shape[1],-1))



"""
1) A array = 2 boyutlu bir tane array -> (3,5)
2) B array = 1 boyutlu bir tane array -> (15,)
3) B array'ini (3,5) olacak sekilde reshape yapalim
4) C = A + B
5) D=linspace ve E=arange ile (3,5) lik matrisler olusturalim.
6) F = D + E
7) C'nin ve F'nin her bir elemanini for dongusu ile eleman eleman carpip G = (15,1) boyutunda elde edelim.
8) C ve F'yi (15,1) sonrasında C'nin ilk elemani ile F'nin son elemani toplayarak ilerleyelim.
9) toplam degerleri eger 1 den buyukse G1 isimli bir listeye atalim, else ise G2 isimli listeye atalim
"""
import numpy as np
# 2 boyutlu bir dizi oluşturma (3x5)
A = np.random.rand(3, 5)  # 0 ile 1 arasında rastgele sayılarla dolu 3x5'lik bir dizi
# 1 boyutlu bir dizi oluşturma (15 elemanlı)
B = np.arange(15)  # 0'dan 14'e kadar sayıları içeren bir dizi
# B dizisini 3x5 boyutunda yeniden şekillendirme
B = B.reshape(3, 5)
# A ve B dizilerini toplama
C = A + B
print("C: ",C)
D=np.linspace(10,50,15).reshape(3,5)
print("D: ",D)
E=np.arange(10,160,10).reshape(3,5)
print("E: ",E)
F=D+E
print("F: ",F)
G = []
for i in range(C.shape[0]):  # 3
    for j in range(C.shape[1]):  # 5
        G.append(C[i, j] * F[i, j])
print("G shape: ",np.array(G).shape)

#carpim yaparken NxM * MxN olmali

#Stacking - Istifleme - Dizi Birlestirme

import numpy as np
dizi1=np.array([[1,2],[3,4]])
print(dizi1)
dizi2=np.array([[5,6],[7,8]])
print(dizi2)
dizi_dikey=np.vstack((dizi1,dizi2)) 
print(dizi_dikey)
dizi_yatay=np.hstack((dizi1,dizi2)) 
print(dizi_yatay)

import numpy as np
ar1=np.array([[3,2],[5,6]])
ar2=np.array([[1,3],[5,3]])
dizi_dikey=np.vstack((ar1,ar2)) 
print(dizi_dikey)
dizi_yatay=np.hstack((ar1,ar2))
print(dizi_yatay)

