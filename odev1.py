import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri = pd.read_csv("iris-1.csv")  # CSV dosyasını yükle
"""
print(veri.head())
print("*********************************************")
print(veri.tail())
print("*********************************************")
print(veri.columns)
print("*********************************************")
print(veri.info())
print("*********************************************")
print(veri.describe())
print("*********************************************")

# Line Plot (Çizgi Grafiği)
plt.figure(figsize=(6, 2))
plt.plot(veri["Id"], veri["SepalLengthCm"], color="red", alpha=0.8, label="Sepal Length")
plt.plot(veri["Id"], veri["SepalWidthCm"], color="blue", alpha=0.7, label="Sepal Width")
plt.title("Graph")
plt.xlabel("ID")
plt.ylabel("SepalLength-SepalWidth")
plt.grid(True)
plt.legend() 
plt.show()

# Scatter Plot (Dağılım Grafiği)
plt.figure()
plt.scatter(veri["SepalLengthCm"], veri["PetalLengthCm"], color="blue", alpha=0.6)
plt.title("SepalLength-PetalLength")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()
"""
#histogram
plt.figure()
plt.hist(veri["SepalLengthCm"], color = "red", alpha = 0.6, bins=20 , label = "SepalLengthCm")
plt.hist(veri["PetalLengthCm"], color = "blue", alpha = 0.6, bins=20 , label = "PetalLengthCm")
#bins=20 demek 20 sutun olacak demek

plt.ylabel("Frekans (Kaç adet olduğu)")
plt.xlabel("cm")
plt.legend()
plt.show()

#subplots
