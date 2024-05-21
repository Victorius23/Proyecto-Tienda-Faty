import serial
import time

def obtener_peso_de_bascula(puerto_serial, baud_rate, secuencia):
    try:
        ser = serial.Serial(port=puerto_serial, baudrate=baud_rate, timeout=1)
        ser.write(secuencia.encode())
        time.sleep(0.1)  # Esperar un momento para que la báscula responda
        peso = ser.readline().strip().decode()
        ser.close()
        return peso
    except Exception as e:
        return str(e)
        
