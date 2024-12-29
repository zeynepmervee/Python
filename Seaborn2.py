import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# veriyi iceriye aktar
# boy-kilo
veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")


plt.figure()
plt.title("boy vs kilo")
sns.scatterplot(x="boy",y="kilo",data=veri)
sns.set_style("darkgrid")
#plt.show()


plt.figure()
plt.title("boy vs kilo")
sns.scatterplot(x="boy",y="kilo",data=veri)
sns.set_style("whitegrid")
#plt.show()

# madalya tipine gore:
plt.figure()
sns.scatterplot(x="boy",y="kilo",data = veri, hue = "madalya")
#plt.show()


plt.figure()
sns.regplot(x="boy",y="kilo",data = veri,marker="+",scatter_kws={"alpha":0.2})
plt.show()


plt.figure()
sns.scatterplot(x="boy",y="kilo",data = veri, hue = "sezon",palette="Accent")
plt.title("Boy-Kilo Dagilimi - Beyaz Izgara Tema")
plt.show

#lineplot
plt.figure()
sns.lineplot(x="boy",y="kilo",data = veri)
plt.show()

#histogram
plt.figure()
sns.displot(veri,x="kilo",hue="cinsiyet")
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

plt.figure()
sns.displot(veri,x="kilo",col = "cinsiyet")

plt.figure()
sns.displot(veri,x="kilo",y="boy",kind="kde",hue="cinsiyet")
