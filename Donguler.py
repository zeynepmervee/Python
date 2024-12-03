ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci:
    print(i*3) #her indexteki elemani 3 kere yazar

#maaslara yuzde 20 zam yapan uygulama asagidadir
maaslar = [1000,2000,3000,4000,5000]

def zam20(a):
    print(a*1.2)

for i in maaslar:
    zam20(i)
#maasi 3000 ve uzeri olanlara %10, digerlerine %20
def zam10(a):
    print(a*1.1)

for i in maaslar:
    if i >= 3000: #Bazı ondalıklı sayıların ikili karşılıkları tam olarak ifade edilemez.
        zam10(i) #Bu, küçük yuvarlama hatalarına neden olur.bu nedenle 3300.0000000000005 gibi bir çıktı aldık
    else:
        zam20(i)

A = []
B = []

for i in [5,"f",3,"z"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)

print(A[1])