import time
from dataURL import DataURL
from getURL import GetURL
from tkinter import *

useDataURL = DataURL()
useGetURL = GetURL()

pencere = Tk()

def fonksiyon():
    print("Hoşbulduk")

etiket = Label(pencere, text="Mini Örümceğe Hoşgeldiniz!!!\nCevapladıktan sonra başlamak için bu sekmeyi kapatın.")
etiket.pack()

buton = Button(pencere, text="Cevapla", command=fonksiyon)
buton.pack()

pencere.mainloop()

#print("-: Mini Örümceğe hoş geldiniz! :-")
#print("|------------------------------|")
#print("")
#time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = int(input("Tercihiniz: "))
    if menuSecim == 0:
        print("Mini Örümcek kapatılıyor...")
        time.sleep(1)
        break
    elif menuSecim == 1:
        useDataURL.dataRead()
    elif menuSecim == 2:
        useDataURL.dataWrite()
    elif menuSecim == 3:
        useGetURL.getWeb()
    elif menuSecim == 4:
        useGetURL.getList()