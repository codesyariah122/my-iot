from machine import Pin
import time

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

    # Menggunakan time_pulse_us untuk mengukur durasi pulsa
    pulse_duration = machine.time_pulse_us(ECHO, 1)  # 1 untuk menunggu pulsa HIGH
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
    else:
        print("Tidak ada kendaraan. Palang tetap tertutup.")

    time.sleep(1)
