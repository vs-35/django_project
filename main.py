from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def __get_html_content(self):
        html_file = 'homework.html'
        with open(html_file, "r", encoding="utf-8") as file:
            html_content = file.read()
            return html_content