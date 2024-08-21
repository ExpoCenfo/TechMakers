import board
import mfrc522

def escribir_tarjeta():
    lector = mfrc522.MFRC522(
        board.SCK,  # Pin SCK
        board.MOSI,  # Pin MOSI
        board.MISO,  # Pin MISO
        board.IO4,   # Pin RST
        board.IO5,   # Pin SDA
    )

    lector.set_antenna_gain(0x07 << 4)

    print('')
    print("Acérquese la tarjeta al lector para escribir datos")
    print('')

    try:
        while True:
            estado, tipo_tarjeta = lector.request(lector.REQIDL)

            if estado == lector.OK:
                estado, uid = lector.anticoll()

                if estado == lector.OK:
                    print("Nueva tarjeta detectada")
                    print("  - Tipo de tarjeta: 0x%02x" % tipo_tarjeta)
                    print("  - UID: 0x%02x%02x%02x%02x" % (uid[0], uid[1], uid[2], uid[3]))
                    print('')

                    if lector.select_tag(uid) == lector.OK:
                        clave = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                        if lector.auth(lector.AUTHENT1A, 8, clave, uid) == lector.OK:
                            datos_a_escribir = b"https://expocenfo.github.io/Games/"  # Ejemplo de datos largos

                            bloques_necesarios = (len(datos_a_escribir) + 15) // 16

                            for i in range(bloques_necesarios):
                                bloque = 8 + i  # Comenzar a escribir desde el bloque 8
                                segmento = datos_a_escribir[i*16:(i+1)*16]

                                # Si el segmento es menor de 16 bytes, completarlo con ceros
                                if len(segmento) < 16:
                                    segmento += b'\x00' * (16 - len(segmento))

                                estado = lector.write(bloque, segmento)
                                
                                if estado != lector.OK:
                                    print(f"Error al escribir en el bloque {bloque}")
                                    break

                            lector.stop_crypto1()

                            if estado == lector.OK:
                                print("Datos escritos correctamente en la tarjeta")
                            else:
                                print("Error al escribir todos los datos en la tarjeta")
                        else:
                            print("Error de autenticación")
                    else:
                        print("Error al seleccionar la tarjeta")

    except KeyboardInterrupt:
        print("Detenido por Ctrl+C")

while True:
    escribir_tarjeta()
