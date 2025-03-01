# Tavuk Oyunu

Bu proje, **Kodland Case Çalışması** kapsamında geliştirilmiş bir **2D platform oyunudur**. Oyun, **Pygame Zero** kütüphanesi kullanılarak kodlanmıştır ve temel olarak bir karakterin (Blob) tavuklardan zıplayarak kaçmasını ve puan toplamasını amaçlar.

## 🚀 Özellikler
- **Ana menü** (Oyna, Müzik Aç/Kapat, Çıkış)
- **Blob karakteri** (Sol, sağ hareket ve zıplama mekanikleri)
- **Tavuklar** (Rastgele yönlerde hareket eden düşmanlar)
- **Puan sistemi** (Tavukları belirli bir noktaya ulaştırınca puan kazanılır)
- **Ses efektleri** (Koşma, zıplama, oyun bitiş sesi vb.)
- **Oyun sonu ekranı** (Puan gösterimi ve yeni oyun seçenekleri)

## 🛠 Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki bağımlılıkları yüklemeniz gerekir:

```sh
pip install pgzero
```

## 🎮 Nasıl Çalıştırılır?
Aşağıdaki komutu terminal veya komut satırında çalıştırarak oyunu başlatabilirsiniz:

```sh
pgzrun intro.py
```

## 🕹 Oynanış
- **Sol Ok Tuşu:** Blob karakterini sola hareket ettirir.
- **Sağ Ok Tuşu:** Blob karakterini sağa hareket ettirir.
- **Boşluk (Space):** Blob karakterini zıplatır.
- **Fare Tıklamaları:** Menüdeki butonlara basmak için kullanılır.

## 📂 Dosya Yapısı
```
📁 Tavuk_Oyunu
 ├── 📄 intro.py  # Oyunun ana kod dosyası
 ├── 📂 images/    # Görseller
 ├── 📂 music/    # Müzikler
 ├── 📂 sounds/    # Sesler
 ├── 📄 README.md  # Proje açıklamaları
```

## 🔊 Sesler ve Grafikler
Oyun içindeki görseller ve sesler, Pygame Zero'nun desteklediği formatlarda olup **image/**, **music/** ve **sounds/** klasörlerinden yüklenmektedir.

---

🎮 **İyi eğlenceler!**

_Bu readme dosyası chatGPT ile oluşturulmuştur._
