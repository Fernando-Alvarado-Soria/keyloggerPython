la version de python que estoy utilizando es una de las modernas es  la 3.13.3
las librerias que vas a necesitar es: pynput y en su caso pywin32 esta ultima no es tan necesaria pero si te la pide instalala te dejo codigo:
-- pip install pynput 
-- pip install pywin32
las otras que ves en el codigo esas vienen por defecto en python

Ahora para al correo que quieres que te llegue lo que el usuario escriba hay 2 factores que debes de tomar en cuernta para esto.
si te fijas en la funcion crearEmail estoy utilizando el metodo SMTP que es por gmail, las versiones de gmail recientes quito la opcion de activar la funcion de "acceso de apps menos seguras"
asi que tendras que quitar las llaves de acceso que tienes y tendras que crear una contraseña por aplicacion para te llegue el correo con lo que el usuario creo porque si no haces esto no te llegara nada.
una vez que no tengas ninguna llave de acceso ve a este link https://myaccount.google.com/apppasswords aqui crearas la aplicacion le pondras un nombre y al darle al boton de "crear" te saldra una contraseña
esa es la contraseña que pondras en la funcion de "EnviarEmail" buscas la parte que dice passw='tu_contraseña_de_aplicación' pones la contraseña de tu aplicacion sin espacios y listo ya te llegaran

por obvias razones no te enseñare a como infectar a otra persona ni como hacer un ejecutable ni los metodos de inyeccion, este scrip esta hecho con fines educativos si lo pruebas funciona en tu computadora.
--gracias por leer:D
