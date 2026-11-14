
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        with open("templates/contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(html_content.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")

        form_data = parse_qs(post_data)

        print("Получены данные от пользователя:")
        print(form_data)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        response = "<h1>Данные успешно получены!</h1>"
        self.wfile.write(response.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyServer)
    print("Сервер запущен: http://localhost:8000")
    server.serve_forever()
