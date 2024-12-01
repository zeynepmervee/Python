#Veri yapıları 
print("*****************************Listeler***********************************************")
notlar = [90,40,70,50]
print(type(notlar))

liste=["a",19.3,90]
list_genis=["a",19.3,90,notlar]
print(list_genis[3][1]) #notlar (3. indexte oldugu icin) dizisinin 1. indexinde olan 40 ekrana yazilir

print(len(list_genis)) #uzunlugu 4

del liste[1] #1. indexteki elemani (19.3) siler
del liste #liste adlı listeyi siler


print(list_genis[:2]) #list_genis[0:2] yazmakla aynı sey. list_genis[2:] olsaydı 2. indexten sona kadar yazardı
list_genis.append("feyyaz") #append metodu liste üzerinde kalıcı bir degisiklik yapti. feyyaz elemanini sona ekledi
print(list_genis)
list_genis.remove("a") #a elemanini kalici olarak sildik
print(list_genis)
list_genis.insert(0,"zeynep") #0. elemana zeynep ekledik
print(list_genis)
list_genis.insert(len(list_genis),"elma") #len ile listenin boyunu ölçüp son elemana elma ekledik
print(list_genis)
list_genis.pop(5) #5. indexteki elemani siler
print(list_genis)
print(list_genis.count("zeynep")) #dizide kac tane zeynep elemanı var sayar, ekrana 1 yazdirir.

liste_yedek=list_genis.copy()  #eski listeyi kaybetmemek icin kopyalayıp yedek listeye aktardik

list_genis.extend(["a","b"]) #list_genis dizisiyle extend'in icindeki dizi birlestirilir
print(list_genis)

print(list_genis.index("a")) #a elemaninin kacinci indexte oldugunu gosterir
list_genis.reverse() #elemanlari sondan basa dogru olacak sekilde gunceller
print(list_genis)

liste=[10,23,2,67]
liste.sort() #listeyi siralayarak kalici olarak degistirir
print(liste)

liste.clear() #listenin elemanlarini temizler
print(liste)


print("**************************TUPLE**********************")
#degistirilemez olmasiyla dizilerden ayrilir

t=(45,30,"a",[1,2,3])
t=45,30,"a",[1,2,3] # iki sekilde de tuple olusturulabilir
print(t)

t=("eleman") #boyle yaparsak bu tuple olmaz, string olur
t=("eleman",) #son virgul koyulmus hali tuple'dir.
print(t)

print("**************************SOZLUK**********************")
#Sozluklerin key'leri sabittir!!!
sozluk={"REG" : "Regresyon Modeli",
        "LOJ" : "Lojistik Regresyon",
        "CART" : "Classification and Reg"}

print(sozluk)
len(sozluk) #3 ciktisi verir
print(sozluk["REG"])
sozluk["GBM"]="Gradient Boosting Mac"
print(sozluk)

l=[1] #l adinda bir liste olusturduk. listeler, string-int-tuple gibi sabit degildir. degisebilir.
#sozluk[l]="yeni" #boyle yaparsak "unhashable type: 'list'" hatası aliriz. cunku key yerine sabit bir sey yazmamiz lazimken biz liste yazdik.
t=("tuple",)
sozluk[t]="yeni" #tuple sabit oldugu icin sozluk'un key'i olarak kullanilabilir
print(sozluk)


print("**************************SETLER**********************")

l=[1,3,4,"sad"]
s=set(l)
print(s)

t=("a","b","c","b","a") #tekrarlanan ogeleri yalnizca bir kere yazar
s=set(t)
print(s)
print(len(s))
s.add("d") #d elemani eklendi
print(s)
s.remove("a") #tekrar a'yı silmek istersek key error verir
print(s)

set1=set([1,3,5])
set2=set([1,2,3])

print(set1.difference(set2)) #set1'de olup set'de olmayan elemanlari yazdirir
print(set1-set2) #usttekiyle ayni ciktiyi verir
print(set1.symmetric_difference(set2)) #iki set arasinda farkli olan her eleman yazilir

print(set1.intersection(set2)) #iki set'in kesisimlerini yazar
print(set1 & set2) #usttekiyle ayni ciktiyi verir

print(set1.union(set2)) #birlesim

set1.intersection_update(set2) #set1'in degerini bu iki set'in kesisimi olarak gunceller
print(set1)

print(set1.isdisjoint(set2)) #iki kumenin kesisimi bos mu? bossa true bos degilse false doner

print(set1.issubset(set2)) #set1'in tum elemanlari set2'nin icinde yer aliyor mu?

print(set2.issuperset(set1)) #set2 set1'in tum elemanlarini kapsiyor mu?

