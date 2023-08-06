#
# Tina4 - This is not a 4ramework.
# Copy-right 2007 - current Tina4
# License: MIT https://opensource.org/licenses/MIT
#
from tina4_python.Debug import Debug
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl
import cgi


class Webserver(BaseHTTPRequestHandler):

    def get_response(self, method):
        params = dict(parse_qsl(urlparse(self.path).query, keep_blank_values=True))
        request = {"params": params, "raw": self.request}
        response = self.server.router_handler.resolve(method, self.path, request, self.headers)
        self.send_response(response["http_code"])
        self.send_header("Content-type", response["content_type"])
        self.end_headers()
        if type(response["content"]) == str:
            self.wfile.write(bytes(response["content"], "utf-8"))
        else:
            self.wfile.write(bytes(response["content"]))

    def do_GET(self):
        Debug("GET " + self.path)
        self.get_response("GET")

    def do_POST(self):
        Debug("POST " + self.path)
        self.get_response("POST")

    def do_OPTIONS(self):
        if self.protocol_version.count("HTTPS"):
            host_name = f"https://{self.server.server_address[0]}:{self.server.server_address[1]}"
        else:
            host_name = f"http://{self.server.server_address[0]}:{self.server.server_address[1]}"
        print("Allow", host_name)
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', host_name)
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE, PATCH, PUT')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
        self.end_headers()
