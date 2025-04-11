import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Başlangıç 5x5 gri ton matris (örnek görüntü)
image = np.array([
    [10, 10, 10, 10, 10],
    [10, 50, 50, 50, 10],
    [10, 50,100, 50, 10],
    [10, 50, 50, 50, 10],
    [10, 10, 10, 10, 10]
], dtype=np.uint8)

# Görüntüyü büyütmek için (daha iyi görmek adına)
image_big = cv2.resize(image, (100, 100), interpolation=cv2.INTER_NEAREST)

# 2️⃣ Otsu Eşikleme
_, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_big = cv2.resize(otsu, (100, 100), interpolation=cv2.INTER_NEAREST)

# 3️⃣ Erozyon ve Genişleme (dilation)
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(otsu, kernel, iterations=1)
dilation = cv2.dilate(otsu, kernel, iterations=1)
edges = cv2.subtract(dilation, erosion)

# Büyütülmüş halleri
erosion_big = cv2.resize(erosion, (100, 100), interpolation=cv2.INTER_NEAREST)
dilation_big = cv2.resize(dilation, (100, 100), interpolation=cv2.INTER_NEAREST)
edges_big = cv2.resize(edges, (100, 100), interpolation=cv2.INTER_NEAREST)

# 4️⃣ Histogramlar (orijinal ve Otsu sonrası)
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_otsu = cv2.calcHist([otsu], [0], None, [256], [0, 256])

# 5️⃣ Görselleri çiz
fig, axs = plt.subplots(3, 3, figsize=(12, 10))

axs[0, 0].imshow(image_big, cmap='gray')
axs[0, 0].set_title("Orijinal Gri Ton")
axs[0, 0].axis('off')

axs[0, 1].imshow(otsu_big, cmap='gray')
axs[0, 1].set_title("Otsu Eşikleme")
axs[0, 1].axis('off')

axs[0, 2].imshow(edges_big, cmap='gray')
axs[0, 2].set_title("Erozyon + Genişleme ile Kenar")
axs[0, 2].axis('off')

axs[1, 0].imshow(erosion_big, cmap='gray')
axs[1, 0].set_title("Erozyon")
axs[1, 0].axis('off')

axs[1, 1].imshow(dilation_big, cmap='gray')
axs[1, 1].set_title("Genişleme")
axs[1, 1].axis('off')

axs[1, 2].axis('off')  # boş

axs[2, 0].plot(hist_original, color='black')
axs[2, 0].set_title("Histogram - Orijinal")

axs[2, 1].plot(hist_otsu, color='black')
axs[2, 1].set_title("Histogram - Otsu")

axs[2, 2].axis('off')  # boş

plt.tight_layout()
plt.show()
