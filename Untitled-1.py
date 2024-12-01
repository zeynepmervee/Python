#python introduction
print(998.3)
print("hello")
print(type(2))
print(type(2.3))

a=12
b="future"
print(len(b))
print(b.upper())
print(b.lower())
print(b.islower()) #kücük harfli mi?
print(b.isupper()) #buyuk harfli mi?

print("u harfi yerine a harfi yazildi: " + b.replace("u","a")) 

#buraya kadar olan metotların hiçbiri nesneler üzerinde kalıcı değişiklik yapmaz!!!

c= " empty "
print(c.strip()) #kenardaki bosluklari siler

c="*empty*"
print(c.strip("*")) #*lari siler


#boyle yaparsak hicbir sey silinmez
f= " empty "
print(f)
print(f.strip(""))

print(dir(c)) #c degiskeni icin kullanilabilecek tum metotları gosterir


#################################################################################

gel_yaz = "gelecegi_yazanlar"

print(gel_yaz[0]) #0. karakteri yazar

print(gel_yaz[1:3]) #1. indexten 3. indexe kadar yazar. 3. dahil degil!!!

######## Tip Donusumleri #########

birinci_sayi=23
print(type(birinci_sayi))
print(type(str(birinci_sayi)))

print("gelecegi","yazanlar")
print("gelecegi","yazanlar", sep = "_")

print("9"+"1") #cikti 91 olur