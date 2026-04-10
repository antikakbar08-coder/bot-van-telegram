import requests
import random
import time
from groq import Groq

# --- DATA DISCORD & GROQ ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def buat_artikel():
    kategori_topik = [
        "Analisis Harga Bitcoin dan Masa Depan Crypto 2026",
        "Update Bursa Transfer Pemain Liga Inggris Musim Depan",
        "Rahasia Kesehatan Jantung dengan Konsumsi Herbal Alami",
        "Perkembangan Kecerdasan Buatan (AI) yang Mengubah Dunia",
        "Tips Investasi Saham dan Reksa Dana untuk Pemula",
        "Destinasi Wisata Paling Hits di Indonesia Tahun 2026",
        "Strategi SEO Terbaru 2026 agar Blog Ramai Pengunjung"
    ]
    topik = random.choice(kategori_topik)
    client = Groq(api_key=GROQ_API_KEY)
    
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Tulis artikel berita 300 kata tentang {topik}. Judul di baris pertama (KAPITAL). Jarak 2 baris antar paragraf. Tanpa simbol bintang (*)."}],
        model="llama-3.3-70b-versatile",
    )
    return completion.choices[0].message.content

def kirim_ke_discord(teks):
    # 1. KIRIM PEMBATAS DULU (Agar kamu tahu ada artikel baru)
    pembatas = "🔴🟡🟢 ** ARTIKEL BARU DI BAWAH INI ** 🔴🟡🟢"
    requests.post(WEBHOOK_URL, json={"content": pembatas})
    
    # Jeda 2 detik agar tidak tertukar
    time.sleep(2)
    
    # 2. KIRIM ARTIKELNYA SAJA (Pesannya bersih, tinggal salin)
    payload = {"content": teks}
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    try:
        artikel = buat_artikel()
        kirim_ke_discord(artikel)
        print("✅ Berhasil! Artikel sudah bisa langsung disalin tanpa gangguan.")
    except Exception as e:
        print(f"❌ Error: {e}")
