


a=input("bir plaka:")
a1=a[0:2]
harf=["a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w","x","q"]#harf karakterleri
sayı=["1","2","3","4","5","6","7","8","9","0"]#string sayıların kontrolü
a2=a[2]#indexleri belirtmek
a3=a[3]
a4=a[4]
a5=a[5] 
a6=a[6]
for i in a1:
    if i in harf:
        print("geçersiz")
    else:
        print(1)
if len(a)==7:   #plaka uzunluğu 7 olcak koşulu
    if (a2 in harf):
        if  (a3 in sayı) and (a4 in sayı) and (a5 in sayı) and (a6 in sayı):#saadece 2. indeksteki harf ise 3 4 5 ve 6. indexlerin sayı olup olmadığını kontrol edicez
            print("oldu")
        else:
            print(0)
        if (a2 in harf) and (a3 in harf):
            if  (a4 in sayı) and (a5 in sayı) and (a6 in sayı):#saadece 2. ve 3.indeksteki harf ise  4 5 ve 6. indexlerin sayı olup olmadığını kontrol edicez
                print("oldu")
                
        else:
            print(0)
        if (a2 in harf) and (a3 in harf) and (a4 in harf):#2 3 ve 4. dekileri harf ise 5 ve 6. indexlerin sayı olup olmadığını kontrol edicez
            print("oldu")
            if (a5 in sayı) and (a6 in sayı):
                print("oldu")
            else:
                print(0)
else:
    print("7 harfli olmadı hocaam :D")

if len(a)==8:#plaka uzunluğu 8 olcak koşulu
    a7=a[7]
    if (a2 in harf):
        if (a3 in sayı) and (a4 in sayı) and (a5 in sayı) and (a6 in sayı) and (a7 in sayı):#saadece 2. indeksteki harf ise 3 4 5 ve 6 7. indexlerin sayı olup olmadığını kontrol edicez
            print("oldu") 
            print("oldu")
        else:
            print(0)
        if (a2 in harf) and (a3 in harf):
            if (a4 in sayı) and (a5 in sayı) and (a6 in sayı) and (a7 in sayı):#2ve 3. indekileri harf ise 4 5 6 ve 7. indexlerin sayı olup olmadığını kontrol edicez
                print("oldu")
        else:
            print(0)
        if (a2 in harf) and (a3 in harf) and (a4 in harf):#2 3 ve 4. dekileri harf ise 5 6 ve 7. indexlerin sayı olup olmadığını kontrol edicez
            if (a5 in sayı) and (a6 in sayı) and (a7 in sayı):
                print("8 harfli oldu")
            else:
                print(0)