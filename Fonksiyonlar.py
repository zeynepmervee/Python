def kare_al(x):
    print(x**2) #x'in karesini alir
kare_al(3)

def kare_al(x):
    print("Girilen sayinin karesi: " + str(x**2)) #sol taraf string oldugundan sag taraf da string olmali
kare_al(5)

def fonk(a,b):
    print(a+b)
fonk(b=3,a=2) #argumanlarin yerini unuttuysak boyle yazabiliriz

def fonk(a,b):
    return (a+b)

print(fonk(2,7))

x= []
def eleman_ekle(y):
    x.append(y) #y elemanini x dizisine ekle
    print(str(y)+" ifadesi x dizisine eklendi.")

eleman_ekle(2)
print(x)



