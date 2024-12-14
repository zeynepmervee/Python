sinir=4000
print(sinir==5000) #false yazar
gelir=3000
if gelir<sinir:
    print(f"gelir:{gelir}, sinirdan kucuk")

elif gelir==sinir:
    print("gelir sinira esit")
else:
    print("gelir sinirdan buyuk")

magaza_adi=input("Magaza adi nedir? ")
gelir=int(input("Gelirinizi giriniz: ")) #int yapmasaydik inputla alinan deger string olacagindan type error alirdik

if gelir>sinir:
    print("Tebrikler " + magaza_adi + ", promosyon kazandiniz!")
elif gelir<sinir:
    print("Promosyon kazanmak icin geliriniz en az " + str(sinir) + " olmalidir.")
else:
    print("Takibe devam.")

deger=3
liste=[2,3,4,5,6]

if deger in liste:
    print("deger listede mevcut")
else:
    print("deger listede degil")

dictionary={"Turkiye":"Ankara",
            "Ingiltere":"Londra",
            "Almanya":"Berlin"}
print(dictionary.keys())
deger2="Ingiltere"
if deger2 in dictionary.keys():
    print("deger2 keylerin icinde")
else:
    print("icinde degil")

liste1=["pazartesi","sali","carsamba"]
if liste1[2]=="Pazartesi":
    print("pazartesi ikinci indexte")
else:
    print("pazartesi 2. indexte degil")