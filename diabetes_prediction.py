# Diabetes Prediction Machine Learning Model
import pandas as pd  # Veri işleme
import numpy as np  # Sayısal işlemler
import matplotlib.pyplot as plt  # Grafik çizme
import seaborn as sns  # Gelişmiş grafikler

# 1️⃣ Veri setini oku
df = pd.read_csv("diabetes.csv")

# 2️⃣ İlk 5 satırı göster
print(df.head())

# 3️⃣ Eksik veri var mı?
print(df.isnull().sum())

# 4️⃣ Veri dağılımını incele
print(df.describe())

# 5️⃣ Histogram çizelim
df.hist(bins=10, figsize=(10, 8))
plt.show()

# 6️⃣ Giriş özellikleri (X) ve hedef değişken (y)
X = df.drop(columns=["Outcome"])  # Özellikler
y = df["Outcome"]  # Etiket

from sklearn.model_selection import train_test_split

# 7️⃣ Veriyi böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Egitim veri sayisi:", X_train.shape[0])
print("Test veri sayisi:", X_test.shape[0])

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 8️⃣ Modeli oluştur
model = LogisticRegression(max_iter=200)

# 9️⃣ Modeli eğit
model.fit(X_train, y_train)

# 🔟 Test seti ile tahmin yap
y_pred = model.predict(X_test)

# Model başarısını ölç
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Dogruluk Orani: {accuracy:.2f}")

import joblib

# Modeli kaydet
joblib.dump(model, "diabetes_model.pkl")
