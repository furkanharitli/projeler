import tkinter as tk

#tkinter kütüphanesini as metodunu kullanarak tk ye kısalttık
import pandas as pd

#pandas kütüphanesini çağırdık eğer pandas yoksa cmd ye pip install pip daha sonra pip install pandas yaz abi :D


#alt satırda dosya açtırtıyoruz dosyayı "a" ile tanımlıyoruz ki üzerinde çalışabilelim
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





pencere.mainloop()