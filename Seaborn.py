from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# Iris veri setini yükle
iris = load_iris()

# Veri setini pandas DataFrame'e dönüştür
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

# CSV olarak kaydet
data.to_csv("iris.csv", index=False)  # CSV'yi oluşturur
print("Veri CSV olarak kaydedildi.")

# Kaydedilen CSV'yi oku
veri = pd.read_csv("iris.csv")

# Veri hakkında genel bilgiler
def veri_ozet():
    print("\nVeri Başlıkları:")
    print(veri.head())
    print("\nVeri Son Kısımları:")
    print(veri.tail())
    print("\nVeri Bilgisi:")
    print(veri.info())
    print("\nVeri İstatistiksel Özeti:")
    print(veri.describe())

veri_ozet()

# Line Plot (Çizgi Grafiği)
plt.figure(figsize=(6, 2))  # Grafik boyutu
plt.plot(veri.index, veri["sepal length (cm)"], color="red", alpha=0.8, label="Sepal Length")
plt.plot(veri.index, veri["sepal width (cm)"], color="blue", alpha=0.7, label="Sepal Width")

plt.title("Iris Çiçeği Çizgi Grafiği")
plt.xlabel("ID (Satır İndeksi)")  # x ekseni etiketi
plt.ylabel("Uzunluk ve Genişlik (cm)")  # y ekseni etiketi
plt.grid(True)  # Izgara görünümü
plt.legend()  # Çizgi açıklamaları
plt.show()

# Scatter Plot (Dağılım Grafiği)
plt.figure()
plt.scatter(veri["sepal width (cm)"], veri["petal width (cm)"], color="blue", alpha=0.6)

plt.title("Iris Çiçeği Dağılım Grafiği")
plt.xlabel("Sepal Width (cm)")  # x ekseni etiketi
plt.ylabel("Petal Width (cm)")  # y ekseni etiketi
plt.grid(True)  # Izgara görünümü
plt.show()