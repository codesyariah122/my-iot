# My IoT

My IoT adalah aplikasi yang dirancang untuk mengelola dan memantau perangkat Internet of Things (IoT) menggunakan Python. Proyek ini memanfaatkan FastAPI untuk menyediakan API yang responsif dan efisien.

## Fitur Utama

- **API untuk Perangkat IoT:** Menyediakan endpoint untuk menghubungkan dan mengelola perangkat IoT.
- **Pengolahan Data:** Mengumpulkan dan memproses data dari perangkat IoT untuk analisis lebih lanjut.
- **Dokumentasi API:** Tersedia dokumentasi interaktif untuk API yang dapat diakses di `http://127.0.0.1:8000/docs` setelah server dijalankan.

## Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/codesyariah122/my-iot.git
   cd my-iot
   ```
2. Install dependencies:
   ```
   pip install fastapi uvicorn
   ```
3. Jalankan server:
   ```
   uvicorn server:app --reload
   ```

Struktur Folder

    main.py - File utama untuk menjalankan aplikasi.
    server.py - File yang berisi logika server dan API.
    testing.py - File untuk pengujian aplikasi.
    urequest.py - File untuk mengelola permintaan dari perangkat IoT.
    diagram.json - File yang berisi diagram atau struktur data.

Lisensi

Proyek ini berada di bawah lisensi yang sesuai. Silakan periksa file LICENSE untuk informasi lebih lanjut.
[FastAPI Documentation](https://fastapi.tiangolo.com/)
