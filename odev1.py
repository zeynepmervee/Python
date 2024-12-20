import pandas as pd

# CSV dosyasını yükle
iris_data = pd.read_csv("iris-1.csv")

# İlk 5 satırı görüntüle
print(iris_data.head())
