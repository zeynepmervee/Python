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

print(dir(c)) #c degiskeni icin kullanilabilecek tum metotları gosterir

