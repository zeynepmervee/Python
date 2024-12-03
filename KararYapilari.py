sinir=4000
print(sinir==5000) #false yazar
gelir=3000
if gelir<sinir:
    print("gelir sinirdan kucuk")

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
