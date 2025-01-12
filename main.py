import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Web sitesinden veri çekme fonksiyonu
def scrape_website():
    url = entry_url.get()
    tag = entry_tag.get()
    class_name = entry_class.get()

    try:
        # Web sitesine istek gönder
        response = requests.get(url)
        response.raise_for_status()  # Hata kontrolü

        # HTML içeriğini parse et
        soup = BeautifulSoup(response.text, "html.parser")

        # Belirli bir etiket ve sınıfa sahip öğeleri bul
        elements = soup.find_all(tag, class_=class_name)

        # Verileri bir listeye kaydet
        data = []
        for element in elements:
            data.append(element.get_text(strip=True))

        # Verileri bir DataFrame'e dönüştür
        df = pd.DataFrame(data, columns=["Veri"])

        # CSV dosyasına kaydet
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Başarılı", f"Veriler başarıyla kaydedildi: {file_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Veri çekme sırasında bir hata oluştu: {e}")

# GUI oluştur
root = tk.Tk()
root.title("Web Scraping Aracı")
root.geometry("500x300")

# Etiketler ve Giriş Alanları
label_url = tk.Label(root, text="Web Sitesi URL:")
label_url.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=10, pady=5)

label_tag = tk.Label(root, text="HTML Etiketi (örn: div, h1, p):")
label_tag.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_tag = tk.Entry(root, width=50)
entry_tag.grid(row=1, column=1, padx=10, pady=5)

label_class = tk.Label(root, text="Sınıf Adı (isteğe bağlı):")
label_class.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_class = tk.Entry(root, width=50)
entry_class.grid(row=2, column=1, padx=10, pady=5)

# Scrape Butonu
button_scrape = tk.Button(root, text="Verileri Çek ve Kaydet", command=scrape_website)
button_scrape.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Uygulamayı çalıştır
root.mainloop()