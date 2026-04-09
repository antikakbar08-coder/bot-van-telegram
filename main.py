import os
import requests
import random
from google import genai

# --- KONFIGURASI DATA ---
# Langsung masukkan token kamu di sini supaya aman
GEMINI_KEY = "AIzaSyAWILUhe_XidZOAdz_UNI_OAQnIiFenntY"
BOT_TOKEN = "8271284602:AAEYxg7YK1ncHHHOyxzeu0agBdx0u3Czb34"
CHAT_ID = "7222492037"

# Inisialisasi AI
client = genai.Client(api_key=GEMINI_KEY)

def kirim_ke_telegram(teks):
    """Fungsi kirim pesan panjang tanpa terpotong"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    # Telegram limit 4096 karakter, kita bagi per 4000
    if len(teks) > 4000:
        for i in range(0, len(teks), 4000):
            payload = {"chat_id": CHAT_ID, "text": teks[i:i+4000]}
            requests.post(url, data=payload)
    else:
        payload = {"chat_id": CHAT_ID, "text": teks}
        requests.post(url, data=payload)

def buat_artikel():
    """Proses pembuatan artikel oleh Gemini"""
    topik_list = [
        "Update Crypto & Bitcoin Hari Ini",
        "Berita Olahraga Dunia Terkini & Sepakbola",
        "Tips Kesehatan Herbal & Hal Unik Dunia"
    ]
    topik = random.choice(topik_list)
    
    prompt = f"""
    Tuliskan sebuah artikel berita lengkap tentang {topik}.
    Ketentuan:
    1. Panjang minimal 600 kata.
    2. Baris pertama adalah JUDUL yang menarik.
    3. Gunakan Bahasa Indonesia yang santai tapi berbobot.
    4. Artikel harus mendalam dan diakhiri dengan Kesimpulan.
    5. Tanpa tag HTML, tanpa simbol bintang (*) berlebihan. 
    """
    
    print(f"🤖 Sedang menulis artikel: {topik}...")
    
    # Memakai model terbaru gemini-2.0-flash
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

def main():
    try:
        # 1. Buat artikel
        artikel = buat_artikel()
        
        # 2. Tambahkan header pengumuman
        pesan_final = f"📢 ARTIKEL FYP BARU SIAP COPAS! 📢\n\n{artikel}"
        
        # 3. Kirim
        kirim_ke_telegram(pesan_final)
        print("✅ Berhasil! Artikel sudah terkirim ke Telegram.")
        
    except Exception as e:
        error_msg = f"⚠️ Ada Error: {str(e)}"
        print(error_msg)
        # Kirim info error ke Telegram agar kamu tahu
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                      data={"chat_id": CHAT_ID, "text": error_msg})

if __name__ == "__main__":
    main()
