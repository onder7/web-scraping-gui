# Web Scraping GUI Uygulaması

Bu proje, **BeautifulSoup** ve **Requests** kütüphanelerini kullanarak web sitelerinden veri çekmeyi otomatikleştiren bir Python GUI uygulamasıdır. Kullanıcılar, belirli bir web sitesinden HTML etiketlerine ve sınıflarına göre veri çekebilir ve bu verileri bir CSV dosyasına kaydedebilir.

---

## Özellikler

- **Kullanıcı Dostu Arayüz**: Basit ve anlaşılır bir GUI ile web scraping işlemi.
- **Veri Çekme**: Belirli HTML etiketleri ve sınıflarına göre veri çekme.
- **CSV Kaydı**: Çekilen verileri CSV dosyasına kaydetme.
- **Hata Yönetimi**: Veri çekme sırasında oluşabilecek hatalar kullanıcıya bildirilir.

---

## Kurulum

### Gereksinimler

- Python 3.x
- `tkinter` (Python ile birlikte gelir, ek kurulum gerekmez)
- `requests` (HTTP istekleri için)
- `beautifulsoup4` (HTML parsing için)
- `pandas` (CSV dosyasına kaydetmek için)

### Kütüphaneleri Kurma

Gerekli kütüphaneleri kurmak için aşağıdaki komutu çalıştırın:

```bash
pip install requests beautifulsoup4 pandas
```

---

## Kullanım

1. **Uygulamayı Çalıştırma**:
   - Terminal veya komut istemcisinde proje dizinine gidin.
   - Aşağıdaki komutu çalıştırarak uygulamayı başlatın:
     ```bash
     python web_scraping_gui.py
     ```

2. **Web Sitesi URL'si**:
   - Veri çekmek istediğiniz web sitesinin URL'sini girin.

3. **HTML Etiketi**:
   - Verilerin bulunduğu HTML etiketini girin (örneğin, `div`, `h1`, `p`).

4. **Sınıf Adı**:
   - İsteğe bağlı olarak, belirli bir sınıfa sahip öğeleri hedeflemek için sınıf adını girin.

5. **Verileri Çek ve Kaydet**:
   - "Verileri Çek ve Kaydet" butonuna tıklayarak verileri çekin ve bir CSV dosyasına kaydedin.

---

## Ekran Görüntüleri

### Ana Pencere


### Başarılı Mesaj


### Hata Mesajı


---

## Yazar Bilgileri

- **Yazar**: Önder Aköz
- **E-posta**: onder7@gmail.com
- **GitHub**: [github.com/onder7](https://github.com/onder7)

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

---

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:
1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`).
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`).
4. Branch'inizi pushlayın (`git push origin yeni-ozellik`).
5. Bir Pull Request oluşturun.

---

## Teşekkürler

- Python ve `tkinter` ekibine bu harika araçları sağladıkları için teşekkürler!
- Tüm kullanıcılara ve katkıda bulunanlara teşekkürler!

---

