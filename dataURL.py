import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    adres = "https://"
    adres = "http://"
    kontrolhttps = siteURL[:7]
    kontrolhttp = siteURL[:8]
    if kontrolhttp == "http://" or kontrolhttps == "https://":
      print("Adres kaydedildi.")
      dataOpen.write(siteURL+"\n")
    else:
      print("http:// veya https:// ön ekini kullanarak geçerli bir adres girin.")
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    if os.stat(self.dataFile).st_size == 0:
      print("Henüz kaydedilmiş adres yok.")
    else:
      for dataShow in dataOpen:
        print(dataShow)
    dataOpen.close()