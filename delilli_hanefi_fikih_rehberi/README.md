# 🕌 Delilli Hanefi Fıkıh Rehberi

Bu proje, **"Delilleriyle Hanefi Fıkhı"** eserini temel alan, modern ve kullanıcı dostu bir Streamlit arayüzü ile sunulan dijital fıkıh rehberi ve ilmihal uygulamasıdır.

Uygulama, ham OCR kitap sayfaları yerine temizlenmiş, özetlenmiş ve kategorize edilmiş fıkhi veriler üzerinden çalışarak en doğru fıkhi bilgilere hızlıca ulaşmanızı sağlar.

## 🚀 Özellikler

1. **🏠 Ana Sayfa:** Uygulama hakkında genel bilgiler ve eserin kaynak atıfları.
2. **📚 Fıkıh Rehberi (Konular):** Hanefi fıkhının 9 ana kategorisi altında toplanmış **42 detaylı alt başlıkta** temiz ve zengin ilmihal özetleri.
3. **🔍 Gelişmiş Arama:** İlmihal özetlerinde ve konu başlıklarında kelime bazlı anlık arama yapabilme ve eşleşen kelimeleri altın rengiyle vurgulama.
4. **💡 Günün Fıkhi Kaidesi:** Her gün veya butona basıldığında 42 alt konudan rastgele seçilen fıkhi kaideyi/özeti gösterme.
5. **❓ Fetvalar (Soru-Cevap):** Günlük hayatta en çok karşılaşılan **80 adet detaylı fetva**, kategori etiketleri ve kitaptaki orijinal sayfa numarası referanslarıyla.

## 📁 Proje Yapısı

* `delilli_hanefi_fikih_rehberi.py`: Uygulamanın Streamlit arayüzü, tema ayarları, HTML/CSS render mantığı ve sayfa yönetimini içeren ana dosya.
* `fiqh_data.py`: Uygulamanın beslendiği 42 ilmihal konusunu ve 80 fetvalık veri tabanını barındıran modüler veri dosyası.
* `Delilleriyle Hanefi Fıkhı.json`: Orijinal kitaptan çıkarılan 1216 sayfalık ham OCR verilerini içeren ikincil kaynak dosyası.
* `.streamlit/config.toml`: Uygulamanın koyu yeşil (#071A11) ve altın sarısı (#D4AF37) premium temasını tanımlayan yapılandırma dosyası.

## 💻 Çalıştırma Adımları

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. Uygulamayı başlatın:
   ```bash
   streamlit run delilli_hanefi_fikih_rehberi.py
   ```
