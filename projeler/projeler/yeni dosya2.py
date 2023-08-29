import tkinter as tk
from tkinter import messagebox


def dosya_olustur():
    global sayfa_adi_girdi, yazilacak_metin_girdi
    sayfa_adi = sayfa_adi_girdi.get()
    yazilacak_metin = yazilacak_metin_girdi.get("1.0", tk.END)

    if sayfa_adi == "":
        messagebox.showerror("Hata", "Lütfen bir sayfa adı girin.")
        return

    with open(sayfa_adi + ".txt", "w") as dosya:
        dosya.write(yazilacak_metin)
    messagebox.showinfo("Bilgi", "Dosya başarıyla oluşturuldu.")


def entryleri_temizle():
    global sayfa_adi_girdi, yazilacak_metin_girdi
    sayfa_adi_girdi.delete(0, tk.END)
    yazilacak_metin_girdi.delete("1.0", tk.END)


def arayuz_olustur():
    global sayfa_adi_girdi, yazilacak_metin_girdi
    pencere = tk.Tk()
    pencere.title("Dosya Oluşturma Arayüzü")
    pencere.geometry("500x400")
    pencere.resizable(False, False)

    # Sayfa Adı Etiketi ve Girdisi
    sayfa_adi_etiket = tk.Label(pencere, text="Sayfa Adı:")
    sayfa_adi_etiket.place(x=50, y=50)

    sayfa_adi_girdi = tk.Entry(pencere, width=30)
    sayfa_adi_girdi.place(x=150, y=50)

    # Yazılacak Metin Etiketi ve Girdisi
    yazilacak_metin_etiket = tk.Label(pencere, text="Yazılacak Metin:")
    yazilacak_metin_etiket.place(x=50, y=100)

    yazilacak_metin_girdi = tk.Text(pencere, width=30, height=10)
    yazilacak_metin_girdi.place(x=150, y=100)

    # Butonlar
    baslat_buton = tk.Button(pencere, text="Başlat", command=dosya_olustur)
    baslat_buton.place(x=200, y=330)
    