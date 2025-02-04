from machine import Pin
import time
import urequests

# Pin A4988
STEP_PIN = Pin(2, Pin.OUT)
DIR_PIN = Pin(3, Pin.OUT)

# Pin Sensor Ultrasonik
TRIG = Pin(16, Pin.OUT)
ECHO = Pin(17, Pin.IN)

def get_distance():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    pulse_duration = time.pulse_time(ECHO)
    distance = (pulse_duration * 0.0343) / 2
    return distance

def move_stepper(steps, direction, delay=0.001):
    DIR_PIN.value(direction)
    for _ in range(steps):
        STEP_PIN.value(1)
        time.sleep(delay)
        STEP_PIN.value(0)
        time.sleep(delay)

while True:
    distance = get_distance()
    print("Jarak:", distance, "cm")

    if distance < 10:
        print("Kendaraan terdeteksi! Membuka palang...")
        move_stepper(200, 1)
        time.sleep(3)
        move_stepper(200, 0)
        
        try:
            response = urequests.post("http://192.168.1.100:5000/update", json={"status": "occupied"})
            print("Response:", response.text)
            response.close()
        except Exception as e:
            print("Error saat mengirimkan data ke API:", e)
    else:
        try:
            response = urequests.post("http://192.168.1.100:5000/update", json={"status": "empty"})
            print("Response:", response.text)
            response.close()
        except Exception as e:
            print("Error saat mengirimkan data ke API:", e)

    time.sleep(1)
