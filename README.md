# Otomatik İş Başvuru Botu

Bu proje, web kazıma (scraping) ve doğal dil işleme (NLP) teknikleri kullanarak iş ilanlarını analiz eden ve kullanıcının tercihleriyle eşleşen ilanlara otomatik başvuru yapan bir sistemdir.

## 📌 Özellikler
- **Web Kazıma**: Youthall gibi kariyer platformlarından iş ilanlarını çeker.
- **Kullanıcı Tercihleri**: Kullanıcıdan iş arama kriterleri alınır (şehir, sınıf, çalışma türü vb.).
- **Akıllı Eşleştirme**: Kullanıcının verdiği bilgiler ile iş ilanındaki gereksinimleri karşılaştırarak bir eşleşme yüzdesi hesaplar.
- **Otomatik Başvuru**: Eşleşme oranı belirlenen eşiğin (örneğin %50) üzerindeyse, sistem otomatik olarak başvuru yapar.
- **Streamlit Arayüzü**: Kullanıcı dostu bir arayüz sağlar.
- **Başvuru Takibi**: Yapılan başvuruların durumunu ekranda gösterir.

---

## 🚀 Kurulum ve Çalıştırma
### 1️⃣ Gerekli Bağımlılıkları Yükleyin
Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerini yükleyin:
```bash
pip install selenium streamlit fuzzywuzzy googletrans4 webdriver-manager
```

### 2️⃣ ChromeDriver'ı Ayarlayın
- **Chrome tarayıcınızın sürümüne uygun** [ChromeDriver](https://sites.google.com/chromium.org/driver/) yüklü olmalıdır.
- Alternatif olarak, `webdriver_manager` ile otomatik olarak yüklenir.

### 3️⃣ Projeyi Çalıştırın
```bash
streamlit run app.py
```

---

## 🛠 Çalışma Mantığı
1. **İş ilanlarını çekme:**
   - Selenium ile sayfa kaydırılarak tüm ilanlar yüklenir.
   - İlan başlıkları ve açıklamaları çekilir.
   
2. **Kullanıcıdan bilgi alma:**
   - Kullanıcıdan çalışma tercihi, sınıfı, şehir gibi bilgiler alınır.

3. **Eşleştirme ve Oran Hesaplama:**
   - Kullanıcının verdiği bilgiler iş ilanındaki anahtar kelimelerle karşılaştırılır.
   - Örneğin: Kullanıcı "İstanbul" ve "Stajyer" yazmışsa ve iş ilanında bu kelimeler geçiyorsa %75 oranla eşleşmiş sayılır.

4. **Başvuru Süreci:**
   - Eğer eşleşme oranı yeterliyse, Selenium kullanarak başvuru butonuna tıklanır.
   - Başvurunun başarılı olup olmadığı ekranda gösterilir.

---

## 📌 Örnek Kullanım
Kullanıcıdan şu bilgiler alınır:
```
Şehir: İstanbul
Sınıf: 3. Sınıf
Çalışma Türü: Stajyer
```
Ve şu iş ilanı analiz edilir:
```
Şirket: XYZ Teknoloji
Pozisyon: Yazılım Stajyeri
Lokasyon: İstanbul
Şartlar: 2. veya 3. sınıf öğrencisi olmak, staj yapabilecek olmak.
```
Eğer kullanıcı bilgileri ile ilan %75 oranında eşleşirse başvuru otomatik olarak yapılır.

---

## 🔥 Geliştirme Aşamaları
- [x] Web kazıma ile iş ilanlarını çekme
- [x] Kullanıcıdan tercihleri alma
- [x] NLP ile metinleri karşılaştırma
- [x] Başvuru butonunu otomatik tıklama
- [ ] Farklı platformlardan ilan çekme
- [ ] Başvuruların durumunu kaydetme ve takip etme

---

## 🤝 Katkıda Bulunma
Projeye katkıda bulunmak için lütfen bir **pull request** açın veya hata bildirmek için bir **issue** oluşturun.

---

## 📜 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

