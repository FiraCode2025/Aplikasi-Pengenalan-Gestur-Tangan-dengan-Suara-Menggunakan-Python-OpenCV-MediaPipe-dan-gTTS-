# Gesture Recognition with Voice (GTTS + MediaPipe)

Proyek ini adalah aplikasi Python sederhana yang dapat mengenali gesture tangan menggunakan **MediaPipe**, 
kemudian mengubahnya menjadi suara menggunakan **gTTS (Google Text-to-Speech)**.

## Demo
Ketika Anda mengangkat tangan dengan gesture tertentu, kamera akan mendeteksi dan otomatis mengeluarkan suara.

## ⚙️ Instalasi

1. Clone repository atau download folder ini.
2. Masuk ke folder proyek:
   ```bash
   cd GestureRecognition-GTTS
   ```
3. Buat dan aktifkan virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```
4. Install semua dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Menjalankan Program
Jalankan perintah berikut:
```bash
python finger_gesture.py
```

## 🤚 Gesture yang Didukung
- ✋ FIVE → "Terimakasih"
- ☝️ ONE → "Halo!"
- ✌️ TWO → "Perkenalkan, saya Fira"
- ✊ FIST → "Salam kenal"

## 🛠 Troubleshooting
- Jika `ModuleNotFoundError: No module named mediapipe`, jalankan:
  ```bash
  pip install mediapipe opencv-python gTTS playsound
  ```
- Jika kamera tidak terbuka, pastikan tidak sedang dipakai aplikasi lain.

---
Dibuat dengan menggunakan **Python, MediaPipe, dan gTTS**.
