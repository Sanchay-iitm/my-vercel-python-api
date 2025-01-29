import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Marks data for different names
marks_data = {
    "X": 10,
    "Y": 20
}

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_components = urllib.parse.parse_qs(self.path[2:])
        names = query_components.get('name', [])
        
        marks = []
        
        # Fetch marks for each name
        for name in names:
            marks.append(marks_data.get(name, 0))  # Default 0 if name not found
        
        response = {
            "marks": marks
        }

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # CORS enabled for all origins
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=MyHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
