import board
import mfrc522
import wifi
import adafruit_requests as requests
import binascii
from time import sleep
from ideaboard import IdeaBoard
from adafruit_motor import motor
import socketpool

# Instanciar IdeaBoard
ib = IdeaBoard()

# Configura el cliente HTTP
wifi.radio.connect("Visitas", "UC-22Visitas")
pool = socketpool.SocketPool(wifi.radio)
requests = requests.Session(pool)

# URL del servidor
server_url = "http://192.168.51.174:3000/send-url"  # Usa la IP local de tu computadora

# Funciones de movimiento
def stop():
    ib.pixel = (0, 0, 0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

def move_forward(speed):
    ib.pixel = (0, 255, 0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed

def move_backward(speed):
    ib.pixel = (150, 255, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed

def move_left(speed):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed

def move_right(speed):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed

def send_url(url):
    try:
        response = requests.post(server_url, json={'url': url})
        print(f"URL enviada, respuesta: {response.text}")
    except Exception as e:
        print(f"Error al enviar URL: {e}")

def read_rfid_and_send():
    lector = mfrc522.MFRC522(
        board.SCK,  # Pin SCK
        board.MOSI,  # Pin MOSI
        board.MISO,  # Pin MISO
        board.IO4,   # Pin RST
        board.IO5,   # Pin SDA
    )

    lector.set_antenna_gain(0x07 << 4)

    print("Acérquese la tarjeta al lector para leer datos")

    try:
        while True:
            estado, tipo_tarjeta = lector.request(lector.REQIDL)

            if estado == lector.OK:
                estado, uid = lector.anticoll()

                if estado == lector.OK:
                    uid_hex = binascii.hexlify(bytes(uid)).decode()
                    print(f"UID: {uid_hex}")

                    if lector.select_tag(uid) == lector.OK:
                        clave = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                        if lector.auth(lector.AUTHENT1A, 8, clave, uid) == lector.OK:
                            bloques_a_leer = 4  # Leer 4 bloques (64 bytes)

                            datos_leidos = b''

                            for i in range(bloques_a_leer):
                                bloque = 8 + i  # Comenzar a leer desde el bloque 8
                                datos = lector.read(bloque)
                                datos_leidos += bytes(datos)  # Asegúrate de que 'datos' sea un objeto bytes

                            lector.stop_crypto1()

                            # Convierte los datos leídos de bytes a una cadena de texto
                            datos_str = ''.join(chr(byte) for byte in datos_leidos).strip()

                            print(f"Datos de los bloques 8 a {8+bloques_a_leer-1}: {datos_str}")

                            # Asume que los datos leídos contienen una URL y la envía
                            send_url(datos_str)  # Enviar la URL leída al servidor
                            process_data(datos_str)  # Procesar los datos leídos

                            # Detener por 20 segundos
                            print("Esperando 20 segundos...")
                            sleep(20)
                        else:
                            print("Error de autenticación")
                    else:
                        print("Error al seleccionar la tarjeta")

            sleep(0.5)  # Ajusta el tiempo de espera según sea necesario

    except KeyboardInterrupt:
        print("Detenido por Ctrl+C")

def process_data(data):
    # Procesar los datos y mover el `IdeaBoard` basado en la información recibida
    if 'movimiento' in data:
        direction = data.split('movimiento:')[1].strip()
        if direction == 'Centre':
            stop()
        elif direction == 'South':
            move_backward(0.5)
        elif direction == 'West':
            move_left(0.5)
        elif direction == 'North':
            move_forward(0.5)
        elif direction == 'East':
            move_right(0.5)

# Llama a la función de lectura RFID
read_rfid_and_send()

