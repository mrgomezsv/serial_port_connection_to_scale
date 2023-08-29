import serial

def capturar_datos_bascula(puerto_serial):
    try:
        with serial.Serial(puerto_serial, baudrate=9600, timeout=1) as ser:
            print(f"Capturando datos de la báscula en el puerto {puerto_serial}...")
            while True:
                dato = ser.readline().decode().strip()
                print(f"Dato recibido: {dato}")
    except Exception as e:
        print(f"Error en la comunicación con la báscula: {e}")

if __name__ == "__main__":
    puerto_com = "COM1"  
    capturar_datos_bascula(puerto_com)
