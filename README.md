# Stream CCTV dengan Deteksi Objek YOLOv8

Aplikasi web Flask untuk streaming CCTV dengan kemampuan deteksi objek menggunakan YOLOv8. Aplikasi ini dapat menampilkan video stream dari kamera RTSP dan melakukan deteksi objek secara real-time.

## Fitur

- Streaming video CCTV melalui protokol RTSP
- Deteksi objek real-time menggunakan YOLOv8
- Antarmuka web sederhana
- Visualisasi hasil deteksi objek

## Persyaratan Sistem

- Python 3.9 atau lebih baru
- Sistem operasi: Windows/Linux/MacOS
- RAM minimal 4GB (direkomendasikan 8GB)
- GPU opsional (untuk performa lebih baik)

## Instalasi

1. Clone repositori ini:
```bash
git clone https://github.com/yourusername/Stream-CCTV.git
cd Stream-CCTV
```

2. Buat virtual environment (opsional tapi direkomendasikan):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# atau
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Konfigurasi

1. Buka file `app.py`
2. Sesuaikan URL RTSP pada variabel `rtsp_url` dengan kamera CCTV Anda:
```python
rtsp_url = 'rtsp://username:password@ip-address:port/stream'
```

## Penggunaan

1. Jalankan aplikasi:
```bash
python app.py
```

2. Buka browser dan akses:
```
http://localhost:5000
```

## Menggunakan Docker

1. Build image:
```bash
docker build -t stream-cctv .
```

2. Jalankan container:
```bash
docker run -p 5000:5000 stream-cctv
```

## Troubleshooting

### Error libGL.so.1
Jika menggunakan Docker dan mendapat error `libGL.so.1`, install package yang diperlukan:
```bash
apt-get update && apt-get install -y libgl1-mesa-glx
```

### Error Loading Model
Pastikan file model YOLOv8 (`yolov8n.pt`) sudah ada di direktori yang sama dengan `app.py`. Model akan didownload otomatis saat pertama kali dijalankan.

## Teknologi yang Digunakan

- Flask: Web framework
- OpenCV: Image processing dan video streaming
- YOLOv8: Object detection
- NumPy: Array processing

## Lisensi

[MIT License](LICENSE)

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau laporkan issue jika menemukan bug.

## Catatan Keamanan

- Pastikan untuk mengamankan kredensial RTSP Anda
- Gunakan HTTPS jika digunakan di production
- Batasi akses ke aplikasi menggunakan autentikasi jika diperlukan 