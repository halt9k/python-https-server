import http.server
import os
import ssl

cur_dir = os.path.dirname(os.path.abspath(__file__)) + '\\'


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="..\\", **kwargs)


def start_server(host, port):
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, RequestHandlerClass=Handler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile=cur_dir + "cert.pem",
                                   keyfile=cur_dir + "key.pem",
                                   ssl_version=ssl.PROTOCOL_TLS
                                   )

    print("File Server started at https://" + server_address[0] + ":" + str(server_address[1]))
    httpd.serve_forever()


def main():
    try:
        start_server('localhost', 8000)
    except KeyboardInterrupt:
        print("\nFile Server Stopped!")


main()
