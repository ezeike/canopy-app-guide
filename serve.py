#!/usr/bin/env python3
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("0.0.0.0", 8081), handler)
print("serving at http://0.0.0.0:8081/article.html")
httpd.serve_forever()
