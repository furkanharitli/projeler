from tkinter import *

e = Tk()
e.title("Çalışma Takibi")
e.geometry("400x600")

# Yapılacak iş etiketi ve giriş kutusu
yapilacak_is_etiketi = Label(e, text="Yapılacak İş:")
yapilacak_is_etiketi.grid(row=0, column=0, padx=5, pady=5, sticky=W)

yapilacak_is_giris = Entry(e, width=30)
yapilacak_is_giris.grid(row=0, column=1, padx=5, pady=5)

# Tarih etiketi ve giriş kutusu
tarih_etiketi = Label(e, text="Tarih:")
tarih_etiketi.grid(row=1, column=0, padx=5, pady=5, sticky=W)

tarih_giris = Entry(e, width=30)
tarih_giris.grid(row=1, column=1, padx=5, pady=5)

# Öncelik etiketi ve seçim kutusu
oncelik_etiketi = Label(e, text="Öncelik:")
oncelik_etiketi.grid(row=2, column=0, padx=5, pady=5, sticky=W)

oncelik_secim = StringVar(e)
oncelik_secim.set("Normal")

oncelik_secim_kutusu = OptionMenu(e, oncelik_secim, "Yüksek", "Normal", "Düşük")
oncelik_secim_kutusu.grid(row=2, column=1, padx=5, pady=5)

# Ekle düğmesi
def yapilacak_ekle():
    yapilacak = yapilacak_is_giris.get()
    tarih = tarih_giris.get()
    oncelik = oncelik_secim.get()
    if yapilacak.strip() == "":
        return
    ekleme = f"{yapilacak} ({tarih}, {oncelik})"
    yapilacaklar_listesi.insert(END, ekleme)
    yapilacak_is_giris.delete(0, END)
    tarih_giris.delete(0, END)
    oncelik_secim.set("Normal")

ekle_dugmesi = Button(e, text="Ekle", command=yapilacak_ekle)
ekle_dugmesi.grid(row=3, column=1, padx=5, pady=5, sticky=E)

# Yapılacaklar listesi
yapilacaklar_listesi = Listbox(e, height=20, width=50)
yapilacaklar_listesi.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Silme düğmesi
def yapilacak_sil():
    secili = yapilacaklar_listesi.curselection()
    if len(secili) == 0:
        return
    yapilacaklar_listesi.delete(secili[0])

sil_dugmesi = Button(e, text="Sil", command=yapilacak_sil)
sil_dugmesi.grid(row=5, column=1, padx=5, pady=5, sticky=E)

# Çıkış düğmesi
def cikis():
    e.destroy()
e.mainloop()