"""ABP Ejercicio Individual 6.1 - Servidor"""

# Levantar un servidor en python con http.server

import http.server
import socketserver
import datetime


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Clase que maneja las solicitudes al servidor"""

    def do_GET(self):
        # Configurar el código de respuesta y las cabeceras
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        message = f"<h1>Bienvenido</h1>"
        message += f"<p>Fecha y hora actual: {now}</p>"

        # Enviar el mensaje de respuesta al navegador
        self.wfile.write(bytes(message, "utf8"))


def main():
    """Función principal del programa"""
    # Configurar la dirección IP y el puerto en el que se ejecutará el servidor
    host = "localhost"
    port = 8000

    # Crear el objeto de servidor y especificar el manejador de solicitudes
    with socketserver.TCPServer((host, port), MyHandler) as server:
        print(f"Servidor iniciado en {host}:{port}")

        # Permitir que el servidor siga en ejecución hasta que se interrumpa
        server.serve_forever()


if __name__ == "__main__":
    main()
