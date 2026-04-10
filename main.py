import requests
import random
import time
from groq import Groq

# --- KONFIGURASI ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def buat_artikel():
    # Daftar topik bervariasi
    kategori_topik = [
        "Analisis Harga Bitcoin dan Prediksi Crypto Market 2026",
        "Rumor Transfer Pemain Liga Inggris dan Klub Besar Eropa",
        "Manfaat Tanaman Herbal untuk Stamina Tubuh Alami",
        "Perkembangan Teknologi AI yang Mengubah Dunia Kerja",
        "Tips Investasi Saham Pemula agar Cuan Maksimal",
        "Destinasi Wisata Tersembunyi di Indonesia Tahun 2026",
        "Strategi SEO Terbaru agar Blog Muncul di Page One",
        "Review Fitur Canggih Smartphone Flagship Terbaru"
    ]
    
    topik = random.choice(kategori_topik)
    print(f"🤖 Sedang menulis artikel 300 kata: {topik}...")
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user", 
                    "content": f"Tuliskan artikel berita sebanyak 300 KATA tentang: {topik}. "
                               f"Gunakan Bahasa Indonesia yang padat dan jelas. "
                               f"WAJIB: Baris pertama JUDUL (KAPITAL). "
                               f"Gunakan jarak 2 baris (ENTER 2X) tiap paragraf. "
                               f"Jangan pakai simbol bintang (*) atau tanda tebal. Kirim teks polos saja."
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Gagal membuat artikel: {e}"

def kirim_ke_discord(teks):
    # Langsung kirim seluruh teks dalam satu pesan (Karena 300 kata < 2000 karakter)
    try:
        payload = {"content": teks}
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204 or response.status_code == 200:
            print("✅ BERHASIL! Artikel 300 kata dikirim dalam satu pesan.")
        else:
            print(f"❌ Gagal mengirim. Kode: {response.status_code}")
    except Exception as e:
        print(f"❌ Error pengiriman: {e}")

if __name__ == "__main__":
    # Jalankan proses
    artikel = buat_artikel()
    
    # Tambahkan pembatas tipis di atas judul
    header_kecil = "📌 **UPDATE ARTIKEL HARI INI**\n\n"
    
    kirim_ke_discord(header_kecil + artikel)
