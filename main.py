import os
import requests
import random
from google import genai

# --- DATA KAMU ---
GEMINI_KEY = "AIzaSyAWILUhe_XidZOAdz_UNI_OAQnIiFenntY"
BOT_TOKEN = "8271284602:AAEYxg7YK1ncHHHOyxzeu0agBdx0u3Czb34"
CHAT_ID = "7222492037"

# Inisialisasi Client Baru (Sesuai update Google)
client = genai.Client(api_key=GEMINI_KEY)

def kirim_ke_telegram(teks):
    """Fungsi kirim pesan ke Telegram Van"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    # Bagi teks jika lebih dari 4000 karakter agar tidak error
    for i in range(0, len(teks), 4000):
        requests.post(url, data={"chat_id": CHAT_ID, "text": teks[i:i+4000]})

def buat_artikel():
    """Gemini meracik artikel FYP"""
    topik = random.choice([
        "Update Crypto & Analisis Bitcoin Hari Ini",
        "Berita Olahraga Dunia & Sepakbola Paling Hot",
        "Rahasia Kesehatan Herbal & Hal Unik Dunia"
    ])
    
    prompt = f"Tuliskan artikel berita tentang {topik} minimal 600 kata dalam Bahasa Indonesia yang santai. Berikan judul di baris pertama."
    
    # Memakai model terbaru gemini-2.0-flash
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    try:
        print("🤖 Bot sedang meracik artikel terbaru...")
        hasil_artikel = buat_artikel()
        
        header = "📢 **ARTIKEL BARU SIAP COPAS!** 📢\n\n"
        kirim_ke_telegram(header + hasil_artikel)
        
        print("✅ Sukses! Artikel sudah mendarat di Telegram.")
    except Exception as e:
        print(f"⚠️ Waduh, ada kendala: {e}")
