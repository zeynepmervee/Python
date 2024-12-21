import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri = pd.read_csv("breast-cancer-data.csv")  # CSV dosyasını yükle
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
plt.plot(veri["id"], veri["radius_mean"], color="red", alpha=0.8, label="Sepal Length")
plt.plot(veri["id"], veri["fractal_dimension_worst"], color="blue", alpha=0.7, label="Sepal Width")
plt.title("Graph")
plt.xlabel("ID")
plt.ylabel("mean-worst")
plt.grid(True)
plt.legend() 
plt.show()

# Scatter Plot (Dağılım Grafiği)
plt.figure()
plt.scatter(veri["radius_mean"], veri["id"], color="blue", alpha=0.6)
plt.title("radius mean-id")
plt.xlabel("radius_mean")
plt.ylabel("id")
plt.grid(True)
plt.show()


print(veri)
