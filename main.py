import requests
import random
import time
from groq import Groq

# --- DATA DISCORD & GROQ ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def send_to_discord(text):
    """Kirim ke Discord per 1900 karakter agar tidak error"""
    chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
    for chunk in chunks:
        requests.post(WEBHOOK_URL, json={"content": chunk})
        time.sleep(2)

def buat_artikel():
    topik = random.choice([
        "Update Masa Depan Crypto dan Bitcoin 2026", 
        "Info Bursa Transfer Pemain Bola Terkini", 
        "Rahasia Sehat dengan Herbal Alami Indonesia"
    ])
    
    print(f"🤖 Groq sedang menulis artikel: {topik}...")
    client = Groq(api_key=GROQ_API_KEY)
    
    # MENGGUNAKAN MODEL TERBARU: llama-3.3-70b-versatile
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Tulis artikel berita mendalam 1000 kata tentang {topik} dalam Bahasa Indonesia yang santai. WAJIB: Gunakan jarak 2 baris antar paragraf. Jangan pakai simbol bintang (*)."}],
        model="llama-3.3-70b-versatile",
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    try:
        artikel = buat_artikel()
        header = "━━━━━━━━━━━━━━━━━━━━━━━━━━\n🚀 **ARTIKEL BARU SIAP COPAS** 🚀\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        send_to_discord(header + artikel)
        print("✅ SUKSES TOTAL! Silakan cek Discord kamu.")
    except Exception as e:
        print(f"❌ ERROR: {e}")
