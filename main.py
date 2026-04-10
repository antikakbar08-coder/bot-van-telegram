import requests
import random
import time
import sys
from groq import Groq

# --- KONFIGURASI UTAMA ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def send_to_discord(text, is_header=False):
    """Mengirim pesan ke Discord. Header dikirim sekali, artikel dikirim per bagian."""
    if is_header:
        requests.post(WEBHOOK_URL, json={"content": text})
    else:
        # Kirim per 1900 karakter agar tidak kena limit Discord
        chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
        for chunk in chunks:
            try:
                requests.post(WEBHOOK_URL, json={"content": chunk})
                time.sleep(2) # Jeda agar tidak dianggap spam
            except Exception as e:
                print(f"Gagal kirim bagian artikel: {e}")

def buat_artikel():
    """Membuat artikel 600 kata dengan topik acak yang banyak"""
    
    # BANK TOPIK (Kamu bisa tambah sendiri di sini)
    kategori_topik = [
        "Analisis Harga Bitcoin dan Masa Depan Crypto 2026",
        "Update Bursa Transfer Pemain Liga Inggris Musim Depan",
        "Rahasia Kesehatan Jantung dengan Konsumsi Herbal Alami",
        "Perkembangan Kecerdasan Buatan (AI) yang Mengubah Dunia",
        "Tips Investasi Saham dan Reksa Dana untuk Pemula",
        "Destinasi Wisata Paling Hits di Indonesia Tahun 2026",
        "Cara Mengatur Keuangan Keluarga di Tengah Inflasi",
        "Manfaat Olahraga Lari Pagi untuk Kesehatan Mental",
        "Strategi SEO Terbaru 2026 agar Blog Ramai Pengunjung",
        "Review Gadget Terbaru: Fitur dan Keunggulan Produk Flagship"
    ]
    
    topik_terpilih = random.choice(kategori_topik)
    
    print(f"🤖 Sedang menulis artikel tentang: {topik_terpilih}...")
    
    try:
        client = Groq(api_key=GRO
