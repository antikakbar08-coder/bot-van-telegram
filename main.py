import os
import requests
import random
import google.generativeai as genai
import time

# --- KONFIGURASI DISCORD & GEMINI ---
# Menggunakan Webhook URL yang kamu berikan
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GEMINI_KEY = "AIzaSyAWILUhe_XidZOAdz_UNI_OAQnIiFenntY"

# Inisialisasi AI
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def send_to_discord(text):
    """Mengirim teks panjang ke Discord dengan membaginya per 2000 karakter"""
    chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
    
    for chunk in chunks:
        payload = {"content": chunk}
        response = requests.post(DISCORD_WEBHOOK, json=payload)
        if response.status_code == 429: # Jika kena rate limit Discord
            time.sleep(5)
            requests.post(DISCORD_WEBHOOK, json=payload)
        time.sleep(1) # Jeda aman

def buat_artikel():
    """Gemini menulis artikel panjang dengan format rapi"""
    topik = random.choice([
        "Analisis Pasar Crypto dan Strategi Investasi Bitcoin",
        "Update Transfer Pemain Sepakbola dan Hasil Pertandingan",
        "Panduan Kesehatan Herbal: Manfaat Rempah Alami untuk Tubuh",
        "Teknologi Terbaru dan Gadget yang Akan Rilis Tahun Ini"
    ])
    
    prompt = f"""
    Tuliskan artikel berita mendalam tentang {topik}.
    
    ATURAN KHUSUS:
    1. Panjang artikel MINIMAL 1000 KATA.
    2. Baris pertama adalah JUDUL (Gunakan Huruf Kapital).
    3. WAJIB: Berikan JARAK 2 BARIS (Double Enter) di setiap pergantian paragraf agar mudah disalin.
    4. Bahasa Indonesia santai, informatif, dan bikin pembaca betah.
    5. JANGAN gunakan banyak simbol bintang (*). Fokus pada kualitas teks.
    """
    
    print(f"🤖 Sedang meracik artikel 1000 kata untuk Discord...")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    try:
        artikel_konten = buat_artikel()
        
        # Header untuk menandai artikel baru
        header = "━━━━━━━━━━━━━━━━━━━━━━━━━━\n🚀 **ARTIKEL BARU SIAP POSTING!** 🚀\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        send_to_discord(header + artikel_konten)
        print("✅ Sukses! Silakan cek server Discord kamu.")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
