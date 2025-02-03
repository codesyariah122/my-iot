from machine import Pin
import time
import urequests

# Pin A4988
STEP_PIN = Pin(2, Pin.OUT)
DIR_PIN = Pin(3, Pin.OUT)

# Pin Sensor Ultrasonik
TRIG = Pin(16, Pin.OUT)
ECHO = Pin(17, Pin.IN)

# Fungsi untuk mengukur jarak dengan HC-SR04
def get_distance():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # Mengukur durasi pulsa menggunakan time_pulse_us dari modul machine
    pulse_duration = time.pulse_time(ECHO)  # Menggunakan time.pulse_time untuk durasi pulsa
    distance = (pulse_duration * 0.0343) / 2  # Konversi ke cm
    return distance

# Fungsi untuk menggerakkan motor stepper (A4988)
def move_stepper(steps, direction, delay=0.001):
    DIR_PIN.value(direction)  # 1 = maju, 0 = mundur
    for _ in range(steps):
        STEP_PIN.value(1)
        time.sleep(delay)
        STEP_PIN.value(0)
        time.sleep(delay)

while True:
    distance = get_distance()
    print("Jarak:", distance, "cm")

    if distance < 10:  # Jika kendaraan terdeteksi
        print("Kendaraan terdeteksi! Membuka palang...")
        move_stepper(200, 1)  # Putar 1 putaran (200 langkah)
        time.sleep(3)
        move_stepper(200, 0)  # Tutup kembali
        
        # Kirim status ke API
        try:
            response = urequests.post("http://192.168.1.100:5000/update", json={"status": "occupied"})
            print("Response:", response.text)
            response.close()
        except Exception as e:
            print("Error saat mengirimkan data ke API:", e)
    else:
        # Kirim status kosong ke API
        try:
            response = urequests.post("http://192.168.1.100:5000/update", json={"status": "empty"})
            print("Response:", response.text)
            response.close()
        except Exception as e:
            print("Error saat mengirimkan data ke API:", e)

    time.sleep(1)
