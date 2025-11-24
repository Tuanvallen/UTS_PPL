# 🐍 Python Automated ZigZag Pattern (`AutoZigZag.py`)

# BY:23.83.0951_VALLEN AJI KURNIAWAN

Proyek ini adalah pengembangan dari script Python sederhana yang membuat pola "zigzag" bergerak di konsol. Kami telah mengintegrasikan tiga fitur otomatisasi tak terduga yang bertujuan untuk membuat pola bergerak ini lebih dinamis, adaptif, dan responsif terhadap lingkungan (waktu) dan iterasi.

## ✨ Fitur Otomasi Kunci

Program ini secara otomatis menyesuaikan perilaku intinya berdasarkan waktu dan iterasi, menjadikannya bukan sekadar perulangan statis.

| Fitur | Tema Otomasi | Deskripsi |
| :--- | :--- | :--- |
| **1. Auto-Speed** | Adaptasi Waktu | Kecepatan gerakan (`time.sleep`) secara otomatis disesuaikan berdasarkan jam sistem saat ini: **Lebih cepat** pada jam kerja/siang (09:00-16:59), dan **lebih lambat** pada malam hari/dini hari (22:00-05:59). |
| **2. Auto-Character Change** | Visual Dinamis | Setiap kali pola pergerakan berbalik arah (mencapai batas kiri atau kanan), karakter atau string yang dicetak secara otomatis diganti dengan pilihan acak dari daftar yang tersedia. |
| **3. Auto-Boundary Adjustment** | Siklus Dinamis | Batas maksimum indentasi (`max_indent`) secara otomatis diubah ke nilai acak baru (antara 10-30) setiap 100 iterasi. Ini memastikan pola zigzag tidak pernah memiliki jangkauan yang statis. |

---

## 🛠️ Instalasi dan Cara Menjalankan

Proyek ini hanya memerlukan instalasi Python standar dan tidak memerlukan *library* eksternal tambahan selain yang sudah terpasang (Built-in).

### Prasyarat

* Python 3.x

### Langkah-Langkah

1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/NamaPenggunaAnda/NamaRepoAnda.git](https://github.com/NamaPenggunaAnda/NamaRepoAnda.git)
    cd NamaRepoAnda
    ```

2.  **Jalankan Script:**
    ```bash
    python AutoZigZag.py
    ```

3.  **Hentikan Program:**
    Tekan `Ctrl + C` (*KeyboardInterrupt*) untuk menghentikan program yang sedang berjalan.

---

## 🖼️ Bukti Visual (Screenshots)

Untuk menampilkan proyek dengan baik di GitHub, sertakan *screenshot* yang menunjukkan ketiga fitur dalam aksi.

**Cara Membuat Screenshot yang Rapi:**

1.  **Tampilan Normal (Siang Hari):** Ambil *screenshot* yang menunjukkan pergerakan cepat dan pergantian karakter.
2.  **Tampilan Batas Baru:** Tunggu hingga muncul pesan `[Sistem Otomasi: Batas indentasi baru: XX]` dan ambil *screenshot* untuk mendemonstrasikan Fitur 3.
3.  **Tampilan Malam Hari (Opsional):** Jika memungkinkan, tunjukkan pergerakan yang lebih lambat.

### Galeri

| Fitur yang Ditampilkan | Screenshot |
| :---: | :---: |
| **BUKTI Screenshot** | `[Bukti Screnshot.png](https://github.com/Tuanvallen/UTS_PPL/blob/main/Bukti%20Screnshot.png)` |

---

## 📄 Kode Sumber (`AutoZigZag.py`)

Berikut adalah kode sumber lengkap yang menggabungkan semua fitur otomasi:

```python
import time, sys
import datetime 
import random 

# --- Variabel Utama ---
indent = 0 
indentIncreasing = True 
max_indent = 20 
iteration_count = 0 

char_options = ['********', '########', '@@@@@@@@', '--------', '>>>><<<<', 'PYTHONIC']
current_char = char_options[0] 

try:
    while True: 
        
        # --- Fitur 1: Otomasi Kecepatan Berdasarkan Waktu ---
        current_hour = datetime.datetime.now().hour
        if 22 <= current_hour or current_hour < 6: 
            sleep_duration = 0.2 
        elif 9 <= current_hour < 17: 
            sleep_duration = 0.05 
        else: 
            sleep_duration = 0.1 
        # ----------------------------------------------------

        print(' ' * indent, end='')
        print(current_char) 
        time.sleep(sleep_duration) 

        # --- Fitur 3: Otomasi Penyesuaian Batas Indentasi ---
        iteration_count += 1
        if iteration_count >= 100: 
            new_max_indent = random.randint(10, 30)
            print(f"\n[Sistem Otomasi: Batas indentasi baru: {new_max_indent}]\n")
            max_indent = new_max_indent
            iteration_count = 0 
        # ---------------------------------------------------

        if indentIncreasing:
            indent = indent + 1
            if indent >= max_indent: 
                indentIncreasing = False
                # Fitur 2: Ganti karakter saat berbalik
                current_char = random.choice([c for c in char_options if c != current_char]) 
        else:
            indent = indent - 1
            if indent <= 0: 
                indentIncreasing = True
                # Fitur 2: Ganti karakter saat berbalik
                current_char = random.choice([c for c in char_options if c != current_char])
                if indent < 0: indent = 0 
                
except KeyboardInterrupt:
    sys.exit()
