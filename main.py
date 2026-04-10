import requests
import random
import time
import sys
from groq import Groq

# --- KONFIGURASI BOT ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def send_to_discord(text):
    """Kirim teks ke Discord per 1900 karakter agar aman dari limit"""
    chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
    for chunk in chunks:
        try:
            payload = {"content": chunk}
            requests.post(WEBHOOK_URL, json=payload)
            time.sleep(2) # Jeda wajib agar tidak di-banned Discord
        except Exception as e:
            print(f"Gagal kirim ke Discord: {e}")

def buat_artikel():
    """Membuat artikel kualitas tinggi menggunakan Llama 3 via Groq"""
    topik = random.choice([
        "Analisis Mendalam Masa Depan Bitcoin dan Crypto Tahun 2026",
        "Strategi Diet Sehat Berbasis Herbal untuk Stamina Sepanjang Hari",
        "Update Bursa Transfer Sepakbola Eropa dan Prediksi Musim Depan",
        "Tips Optimasi Blog Agar Cepat Masuk Google Page One 2026"
    ])
    
    prompt = f"""
    Bertindaklah sebagai Penulis Artikel Profesional. Tulis artikel berita mendalam tentang: {topik}.
    
    ATURAN PENULISAN:
    1. Panjang artikel MINIMAL 1000 KATA.
    2. Baris pertama adalah JUDUL UTAMA (HURUF KAPITAL SEMUA).
    3. WAJIB: Gunakan jarak 2 baris (ENTER 2X) di setiap pergantian paragraf agar rapi.
    4. Bahasa Indonesia yang mengalir, profesional, dan informatif.
    5. HAPUS SEMUA simbol bintang (*) atau tanda tebal. Berikan teks bersih saja.
    """
    
    print(f"🤖 Groq sedang memproses artikel: {topik}...")
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        # Menggunakan model Llama-3-70b (Model terkuat di Groq)
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-70b-8192",
            temperature=0.7,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error Generate: {str(e)}"

def main():
    print("🚀 Bot Groq Aktif...")
    artikel = buat_artikel()
    
    if "Error" in artikel:
        print(f"❌ {artikel}")
        return

    # Header Postingan agar rapi di Discord
    header = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n📌 **ARTIKEL BARU SIAP POSTING**\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    
    send_to_discord(header + artikel)
    print("✅ Berhasil! Cek Channel Discord kamu sekarang, Van.")

if __name__ == "__main__":
    main()
