# Este archivo es para pruebas solamente. No contiene nada relevante de por sí

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class Controlador(BaseHTTPRequestHandler):

    def do_GET(self):
        parametros = parse_qs(urlparse(self.path).query)
        cliente = self.client_address
        fecha = self.date_time_string()

        self.send_response(200)
        self.send_header("Content-Type", "text/html;charset=UTF-8")
        self.end_headers()
        data = f'''
        <html>
            <head>
                <title>Mi HTTP Personalizado</title>
            </head>
            <body>
                <h1>{cliente}</h1>
                <h2>{fecha}</h2>
                <h3>{parametros}</h3>
            </body
        </html>
        '''
        self.wfile.write(data.encode())

if __name__ == '__main__':
    server = HTTPServer(("0.0.0.0", 8080), Controlador)
    server.serve_forever()

