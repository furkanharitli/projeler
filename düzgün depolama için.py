import tkinter as tk
import pandas as pd
import os

dosya=open("dosya.txt","a")


#pencere oluşturuyoruz
pencere=tk.Tk()
#pencerenin boyutunu ayarlıyoruz 
pencere.geometry("400x400+50+100")

dosyalama=open("dosya.txt","a")

#bu fonksiyon butonumuza basıldığında çalışacak olan fonksiyondur
def degistir():
    #notum kısmı butona basıldığında yazı entrysinin içindeki cümleyi alır
    notum=yazı.get()
    #zaman nott entrysindeki tar
    zaman=nott.get()
    dosyalama.write("\n"+notum+":    "+zaman)
    dosyalama.close()
#veri alacağımız kutucuğu entry ile ayarlarız
yazı=tk.Entry()
#place ile konumunu veririz
yazı.place(x=80,y=20)


nott=tk.Entry(width=50)   
nott.place(x=80,y=100)


#entry yanına tarih yazısı ekliyoruz 
sütun=tk.Label(text="tarih:",font="Courier 14 bold",justify="left")
sütun.place(x=0,y=18)


#entry yanına not yazısını veriyoruz
sütun2=tk.Label(text="not  :",font="Courier 14 bold",justify="left",)
sütun2.place(x=0,y=98)


#duğmeyi buton olarak tanımlayıp commandını degistir fonksiyonuna verip butonun üstündeki yazısını kaydet verip fontunu ayarlıyoruz
dugme=tk.Button(pencere,text="kaydet",command=degistir,font="Courier 14 bold")
#düğmeye konum veriyoruz
dugme.place(x=300,y=135)





# Dosyayı DataFrame olarak yükle
def yukle():
    try:
        veri = pd.read_excel('veriler.xlsx')
        return veri
    except FileNotFoundError:
        return pd.DataFrame(columns=['Not', 'Tarih'])

def degistir():
    notum = yazı.get()
    zaman = nott.get()
    
    veri = yukle()
    yeni_veri = pd.DataFrame({'Not': [notum], 'Tarih': [zaman]})
    veri = pd.concat([veri, yeni_veri], ignore_index=True)
    
    veri.to_excel('veriler.xlsx', index=False)



# Entry'ler ve diğer bileşenler buraya eklenecek

# Düğme
dugme = tk.Button(pencere, text="Kaydet", command=degistir, font="Courier 14 bold")
dugme.place(x=300, y=135)

# Dosyayı yükle
veri = yukle()

# Dosyadaki verileri göstermek için bir örnek olarak bir etiket ekleyebilirsiniz
veri_etiketi = tk.Label(pencere, text=str(veri), font="Courier 12")
veri_etiketi.place(x=10, y=200)

pencere.mainloop()