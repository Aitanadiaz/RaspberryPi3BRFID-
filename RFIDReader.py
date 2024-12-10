import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

print("Waiting for RFID data...")
while True:
    data = ser.readline().decode('utf-8').strip()
    if data:
        print(f"RFID Data: {data}")
