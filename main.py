import os
import google.generativeai as genai
import requests
import random

# CONFIG
GEMINI_API_KEY = os.getenv("AIzaSyAWILUhe_XidZOAdz_UNI_OAQnIiFenntY")
TELEGRAM_TOKEN = os.getenv("8271284602:AAEYxg7YK1ncHHHOyxzeu0agBdx0u3Czb34")
TELEGRAM_CHAT_ID = "7222492037"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # Kirim per 4000 karakter agar tidak terpotong
    for i in range(0, len(text), 4000):
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text[i:i+4000]})

def generate():
    topik = random.choice(["Crypto Terbaru", "Berita Olahraga Hot", "Hal Unik & Herbal"])
    prompt = f"Tulis artikel berita {topik} minimal 600 kata bahasa Indonesia yang santai. Berikan judul di awal."
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    artikel = generate()
    send_to_telegram("📝 ARTIKEL BARU:\n\n" + artikel)
