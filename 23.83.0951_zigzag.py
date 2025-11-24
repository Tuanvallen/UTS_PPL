import time, sys
import datetime 
import random 

# --- Variabel Utama ---
indent = 0 # Posisi awal indentasi
indentIncreasing = True # Arah pergerakan (True = kanan, False = kiri)
max_indent = 20 # Batas indentasi awal (Fitur 3)
iteration_count = 0 # Penghitung iterasi untuk mengubah batas (Fitur 3)

# Daftar karakter/string untuk diganti (Fitur 2)
char_options = ['********', '########', '@@@@@@@@', '--------', '>>>><<<<', 'PYTHONIC']
current_char = char_options[0] # Karakter yang sedang dicetak

try:
    while True: 
        
        # --- Fitur 1: Otomasi Kecepatan Berdasarkan Waktu ---
        current_hour = datetime.datetime.now().hour
        # Set durasi tidur (sleep_duration):
        if 22 <= current_hour or current_hour < 6: # Malam/Dini hari (22:00 - 05:59)
            sleep_duration = 0.2  # Lebih lambat
        elif 9 <= current_hour < 17: # Jam kerja/siang (09:00 - 16:59)
            sleep_duration = 0.05 # Lebih cepat
        else: # Waktu lainnya
            sleep_duration = 0.1  # Kecepatan default
        # ----------------------------------------------------

        print(' ' * indent, end='')
        print(current_char) # Menggunakan karakter yang sedang aktif (Fitur 2)
        time.sleep(sleep_duration) # Menggunakan durasi tidur yang sudah dihitung (Fitur 1)

        # --- Fitur 3: Otomasi Penyesuaian Batas Indentasi ---
        iteration_count += 1
        if iteration_count >= 100: # Setiap 100 iterasi
            # Pilih batas baru secara acak antara 10 dan 30
            new_max_indent = random.randint(10, 30)
            print(f"\n[Sistem Otomasi: Batas indentasi baru: {new_max_indent}]\n")
            max_indent = new_max_indent
            iteration_count = 0 # Reset penghitung
        # ---------------------------------------------------

        if indentIncreasing:
            # Pergerakan ke kanan
            indent = indent + 1
            if indent >= max_indent: # Menggunakan batas yang diotomasi (Fitur 3)
                indentIncreasing = False
                # Fitur 2: Ganti karakter saat berbalik
                current_char = random.choice([c for c in char_options if c != current_char]) 
        else:
            # Pergerakan ke kiri
            indent = indent - 1
            if indent <= 0: # Batas minimum tetap 0
                indentIncreasing = True
                # Fitur 2: Ganti karakter saat berbalik
                current_char = random.choice([c for c in char_options if c != current_char])
                # Jaga-jaga jika indent menjadi negatif karena perubahan max_indent yang ekstrem
                if indent < 0: indent = 0 
                
except KeyboardInterrupt:
    sys.exit()