# TelegramExtractor
Sirve para extraer todos los mensajes con el texto buscado.

# Notas
Se necesita un api_id y un api_hash que podrás obtener en https://my.telegram.org
y que tendrás que poner en el código main.py:
api_id = <TU API_ID>
api_hash = <TU API HASH>

# Instalación
```bash
pip3 install -r requirements
```
# Ejecución
```bash
python3 main.py
```

# Notas de ejecución
Como es una aplicación de telegram, te pedirá: el número de telefono, y luego te llegará un código para vincularla y poder realizar la búsqueda en tus chats. (se creará un fichero en la carpeta de trabajo llamada extractorApp.session)
Como es información sensible, después de terminar con las búsquedas deberías borrar el acceso a la misma desde:
* Ajustes/privacidad y seguridad/Sesiones activas
* Borrar el archivo extractorApp.session
