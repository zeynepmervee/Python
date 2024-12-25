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


# Histogram (Dağılım Grafiği) - Sepal Length
plt.figure(figsize=(6, 4))
plt.hist(veri["sepal length (cm)"], bins=20, color="green", edgecolor="black", alpha=0.7)
plt.title("Sepal Length Histogramı")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frekans")
plt.grid(True)
plt.show()

# Box Plot (Kutu Grafiği) - Sepal Width
plt.figure(figsize=(6, 4))
plt.boxplot(veri["sepal width (cm)"], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Sepal Width Kutu Grafiği")
plt.xlabel("Sepal Width (cm)")
plt.show()

# Pairplot (Çiftli Dağılım Grafiği) - Tüm değişkenler için
import seaborn as sns
sns.pairplot(veri, hue="target", palette="Set1", markers=["o", "s", "D"])
plt.suptitle("Iris Veri Seti Çiftli Dağılım Grafiği", y=1.02)
plt.show()

# Correlation Matrix (Korelasyon Matrisi)
correlation = veri.iloc[:, :-1].corr()  # target sütununu hariç tutarak korelasyon
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Değişkenler Arası Korelasyon Matrisi")
plt.show()

# Bar Plot (Çubuk Grafiği) - Ortalama Sepal Length her hedef sınıfı için
mean_sepal_length = veri.groupby('target')["sepal length (cm)"].mean()
plt.figure(figsize=(6, 4))
mean_sepal_length.plot(kind="bar", color="purple", alpha=0.7)
plt.title("Hedef Sınıfına Göre Ortalama Sepal Length")
plt.xlabel("Target")
plt.ylabel("Ortalama Sepal Length (cm)")
plt.show()

# Verinin Target sınıflarıyla dağılmasını gösteren Pie Chart (Pasta Grafiği)
target_count = veri["target"].value_counts()
plt.figure(figsize=(6, 6))
target_count.plot(kind="pie", autopct="%.1f%%", colors=["#ff9999", "#66b3ff", "#99ff99"], startangle=90)
plt.title("Iris Veri Seti Sınıf Dağılımı")
plt.ylabel("")  # Y ekseni etiketini kaldır
plt.show()
