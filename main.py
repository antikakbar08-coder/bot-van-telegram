import requests
import random
import time
from groq import Groq

# --- DATA DISCORD & GROQ ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1492253373418700982/EztM0BJF8zJlnGGTa5DuyotmHNm-WK_d_mf2qxDT_nmlrYj2MhhGQZogG5o1TyBIEFru"
GROQ_API_KEY = "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"

def send_to_discord(text):
    chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
    for chunk in chunks:
        try:
            requests.post(WEBHOOK_URL, json={"content": chunk})
            time.sleep(2)
        except Exception as e:
            print(f"Gagal kirim: {e}")

def buat_artikel():
    # DAFTAR TOPIK YANG LEBIH BANYAK DAN BERAGAM
    kategori_topik = [
        "Analisis Harga Bitcoin dan Prediksi Crypto Market Minggu Ini",
        "Rumor Transfer Pemain Liga Inggris dan Drama Klub Besar Eropa",
        "Manfaat Temulawak dan Jahe untuk Kesehatan Jantung",
        "Perkembangan Teknologi AI Terbaru di Tahun 2026",
        "Tips Menabung dan Investasi Saham untuk Pemula",
        "Destinasi Wisata Tersembunyi di Indonesia yang Wajib Dikunjungi",
        "Resep Makanan Sehat Pengganti Nasi untuk Diet Alami",
        "Review Gadget Terbaru dan Fitur Canggih yang Akan Rilis",
        "Strategi Meningkatkan Traffic Blog dengan Teknik SEO 2026",
        "Kabar Terbaru Hasil Pertandingan Liga Champions Tadi Malam"
    ]
    
    topik_terpilih = random.choice(kategori_topik)
    
    print(f"🤖 Sedang menulis topik baru: {topik_terpilih}...")
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user", 
                    "content": f"Tuliskan artikel berita 600 KATA tentang: {topik_terpilih}. Gunakan Bahasa Indonesia profesional. WAJIB: Baris pertama JUDUL (KAPITAL). Berikan jarak 2 baris (ENTER 2X) tiap paragraf. Jangan pakai simbol bintang (*)."
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    try:
        artikel_hasil = buat_artikel()
        
        # Header lebih rapi dengan jarak ekstra
        header = "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        header += "📢 **ARSIP ARTIKEL TERBARU**\n"
        header += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n\n"
        
        send_to_discord(header + artikel_hasil)
        print("✅ Berhasil! Topik bervariasi sudah dikirim.")
    except Exception as e:
        print(f"❌ Error: {e}")
