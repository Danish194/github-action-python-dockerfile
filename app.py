from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<h1>Hello Bro! My First Docker Container is Running!</h1>"
        )

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Server is running on port 5000", flush=True)
server.serve_forever()