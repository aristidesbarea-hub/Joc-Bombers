import http.server
import socketserver
import webbrowser
import os

# Configuración
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Cambiar al directorio donde está el script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Sirviendo archivos en http://localhost:{PORT}")
print("Presiona Ctrl+C para detener el servidor.")

# Abrir el navegador automáticamente
webbrowser.open(f"http://localhost:{PORT}")

# Iniciar el servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        httpd.server_close()