✋ Gesture Recognition + Suara (GTTS) – Panduan Lengkap

 1. Persiapan Awal: Install Python

1. Download Python terbaru (3.10 atau 3.11) dari:
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Saat instalasi:

   * Centang **Add Python to PATH**
   * Pilih **Install Now**

3. Cek instalasi di **CMD / PowerShell**:

```bash
python --version
```

atau

```bash
py -3 --version
```

Contoh output:

```
Python 3.11.7
```

---

2. Buat Folder Project

1. Buka **PowerShell / CMD**:

```bash
mkdir GestureRecognition-GTTS
cd GestureRecognition-GTTS
```

2. Folder akan berisi:

* File kode utama (`finger_gesture.py`)
* Daftar library (`requirements.txt`)
* Dokumentasi (`README.md`)
* (Opsional) Virtual environment (`venv/`)

---

 3. Virtual Environment (Opsional tapi disarankan)

```bash
python -m venv venv
```

Aktifkan:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

> Virtual environment menjaga agar library project tidak bercampur dengan Python global.

---

4. Install Library

Buat file `requirements.txt` dan isi library yang dibutuhkan:

```
opencv-python
mediapipe
gTTS
playsound==1.2.2
```

Install semua library:

```bash
pip install -r requirements.txt
```

---
5. Jalankan Program

Di folder project:

```bash
py -3 finger_gesture.py
```

atau

```bash
python finger_gesture.py
```

> Tekan **ESC** untuk keluar.

---

 6. Gesture dan Pesan Suara

 Gesture                 Pesan                          

☝️ ONE (telunjuk)      Halo!                           
✌️ TWO (peace sign)     Perkenalkan, saya Firamawaty Hia 
✋ FIVE (telapak terbuka) Terimakasih                  
✊ FIST (kepalan)        Salam kenal                    
---

7. Tips Agar Stabil

* Pastikan **cahaya cukup**
* Gunakan **background polos**
* Jangan terlalu cepat menggerakkan tangan
* Webcam harus **aktif dan dikenali**

---

 8. Troubleshooting

* **ModuleNotFoundError** → Pastikan install library sesuai `requirements.txt`
* **Camera tidak muncul** → Cek webcam aktif, tutup aplikasi lain yang pakai webcam
* **Suara tidak keluar** → Pastikan speakers/headphones aktif, gunakan versi `playsound==1.2.2`

---

9. Ide Konten Channel

1. Demo **AI Gesture Recognition** langsung live
2. Tutorial **Membuat Robot Suara dengan Python**
3. Edukasi **Belajar Python + MediaPipe**
4. Challenge **Tebak Gesture & Suara** interaktif
5. Komparasi **Google TTS vs Text-to-Speech lain**
