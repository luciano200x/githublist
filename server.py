import http.server
import socketserver

PORT = 8115
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Access your file at http://localhost:{PORT}/github_ips.txt")
    httpd.serve_forever()