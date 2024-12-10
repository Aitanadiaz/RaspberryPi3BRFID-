import serial

try:
    ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

    print("Waiting for RFID data...")
    while True:
        try:
            data = ser.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"RFID Data: {data}")
        except Exception as e:
            print(f"Error reading data: {e}")
except serial.SerialException as e:
    print(f"Serial port error: {e}")
