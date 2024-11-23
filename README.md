# Python Klavye ve Fare Logger

Bu Python programı, klavye girişlerini ve fare hareketlerini kaydederek belirli dosyalara yazan bir araçtır. **Eğitim ve farkındalık yaratma** amacıyla geliştirilmiştir. İzinsiz kullanım kesinlikle yasaktır ve etik kurallara aykırıdır.

---

## ⚠️ Uyarı

Bu yazılım yalnızca **eğitim amacıyla** sağlanmaktadır. Sahip olmadığınız veya açık izin almadığınız sistemlerde bu aracı kullanmak **yasa dışıdır**. Lütfen etik kurallara uyun ve yalnızca izin verilen durumlarda kullanın.

---

## Özellikler

- **Klavyeden girişleri kaydeder:**
  - Girilen her 10 tuş kaydını `klavye_logs.txt` dosyasına yazar.
  - `space` (boşluk) tuşu bir satır sonu olarak kaydedilir.
- **Fare hareketlerini kaydeder:**
  - Fare hareketlerini koordinatlarıyla birlikte `fare_logs.txt` dosyasına yazar.
  - Her 10 hareket bir defada dosyaya işlenir.
- **Dinlemeyi durdurma:**
  - Klavye dinleme işlemini sonlandırmak için `Esc` tuşuna basabilirsiniz.

---

## Gereksinimler

Bu program için aşağıdaki yazılımlar gereklidir:

- **Python 3.x**
- `pynput` kütüphanesi (klavye ve fare işlemleri için)

Gerekli kütüphaneyi yüklemek için:

```bash
pip install pynput


Bu projeyi klonlayın ve katkıda bulunmaktan çekinmeyin:

bash

git clone https://github.com/kerim91/python-klavye-fare-logger.git


