import requests
import random
import time
from groq import Groq

# --- DATA DISCORD & GROQ ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def send_to_discord(text):
    """Mengirim artikel ke Discord dengan pembagian per 1900 karakter"""
    chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
    for chunk in chunks:
        try:
            requests.post(WEBHOOK_URL, json={"content": chunk})
            time.sleep(2) # Jeda agar Discord tidak memblokir
        except Exception as e:
            print(f"Gagal kirim: {e}")

def buat_artikel():
    """Membuat artikel 600 kata menggunakan model terbaru Groq"""
    topik = random.choice([
        "Update Masa Depan Crypto dan Bitcoin 2026", 
        "Analisis Bursa Transfer Pemain Sepakbola Dunia", 
        "Panduan Hidup Sehat dengan Ramuan Herbal Alami"
    ])
    
    print(f"🤖 Sedang meracik artikel 600 kata: {topik}...")
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        # Menggunakan model 'llama-3.3-70b-versatile' yang paling stabil
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user", 
                    "content": f"Tuliskan artikel berita mendalam sebanyak 600 KATA tentang {topik}. Gunakan Bahasa Indonesia yang profesional. WAJIB: Gunakan jarak 2 baris (ENTER 2X) antar paragraf. JANGAN pakai simbol bintang (*)."
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Terjadi kesalahan mesin: {str(e)}"

if __name__ == "__main__":
    try:
        artikel_hasil = buat_artikel()
        
        # Header untuk mempercantik tampilan di Discord
        header = "━━━━━━━━━━━━━━━━━━━━━━━━━━\n🚀 **ARTIKEL BARU (600 KATA) SIAP**\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        send_to_discord(header + artikel_hasil)
        print("✅ BERHASIL! Artikel 600 kata sudah dikirim ke Discord.")
        
    except Exception as e:
        print(f"❌ Error Utama: {e}")
