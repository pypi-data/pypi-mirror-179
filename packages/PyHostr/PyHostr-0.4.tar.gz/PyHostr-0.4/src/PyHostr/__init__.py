from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


routes = []


class PyHostr():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    class Handler(BaseHTTPRequestHandler):

        def do_GET(self):
            print("Current path: " + self.path)
            # Handle GET requests, using objects in routes
            for obj in routes:
                if self.path == obj["route"] and str(obj["method"]).lower() == "get":
                    self.send_response(200)
                    # Send headers
                    for key, value in obj["response_headers"].items():
                        self.send_header(key, value)
                    self.end_headers()
                    self.wfile.write(
                        bytes(obj["response"], "utf8"))
                    return

            self.send_response(404)

        def do_POST(self):
            for obj in routes:
                if self.path == obj["route"] and str(obj["method"]).lower() == "post":
                    self.send_response(200)
                    # Send headers
                    self.end_headers()
                    # Send custom reply and parse into JSON
                    data = self.rfile.read(
                        int(self.headers['Content-Length']))\
                        .decode("utf-8")\
                        .split("&")
                    data = {x.split("=")[0]: x.split("=")[1] for x in data}
                    data = json.dumps(data)
                    # data = self.rfile.read(
                    # int(self.headers["Content-Length"])).decode("utf-8")
                    self.wfile.write(bytes(obj["handler"](data), "utf8"))

                    return

    def warn(self, message):
        print(bcolors.WARNING + "WARNING:\t" + message + bcolors.ENDC)

    def error(self, message):
        print(bcolors.FAIL + "ERROR:\t" + message + bcolors.ENDC)

    def success(self, message):
        print(bcolors.OKGREEN + "SUCCESS:\t" + message + bcolors.ENDC)

    def msg(self, message):
        print("MSG:\t" + message)

    def get(self, route, response="<h1>Default Response</h1>", response_headers={"Content-type": "text/html"}):
        # Add route to routes
        routes.append({
            "method": "GET",
            "route": route,
            # The HTML response
            "response": response,
            "response_headers": response_headers
        })

    def post(self, route, response_headers, handler):
        # Handle POST requests, using objects in routes
        routes.append({
            "method": "POST",
            "route": route,
            "response": response_headers,
            # Handler is a function that handles the POST request
            "handler": handler
        })

    def serve(self):
        # Start server
        server = HTTPServer((self.host, self.port), PyHostr.Handler)
        self.success("Server started http://%s:%s" %
                     (self.host, self.port))

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            self.warn("Stopping server...")
            self.success("Server stopped")
        server.server_close()
        print("Server stopped.")


def handler_func(args):
    return str(args).upper()


if __name__ == "__main__":
    server = PyHostr("localhost", 8080)
    server.get(route="/", response_headers={"Content-type": "text/html"},
               response="<h2>INDEX PAGE</h2>")
    server.get(route="/test", response_headers={"Content-type": "text/html"},
               response="<h2>TEST PAGE</h2>")
    server.post(
        route="/post", response_headers={"Content-type": "application/json"}, handler=handler_func)
    server.serve()
