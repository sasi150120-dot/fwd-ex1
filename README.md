# EX01 Developing a Simple Webserver
## Date:15/10/2026
## REG NUM:26018114
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Protocols</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            padding: 30px;
        }

        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 10px #cccccc;
        }

        h2 {
            text-align: center;
            color: #2563eb;
        }

        ul {
            list-style-type: square;
            padding-left: 25px;
        }

        li {
            padding: 10px;
            margin: 5px 0;
            background: #e8f0fe;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>List of Network Protocols</h2>

        <ul id="protocolList"></ul>
    </div>

    <script>
        const protocols = [
            "TCP",
            "IP",
            "HTTP",
            "HTTPS",
            "FTP",
            "DNS",
            "DHCP",
            "SMTP",
            "SSH",
            "TLS",
            "UDP",
            "IMAP"
        ];

        const list = document.getElementById("protocolList");

        protocols.forEach(function(protocol) {
            const item = document.createElement("li");
            item.textContent = protocol;
            list.appendChild(item);
        });
    </script>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',88)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
server script and check for errors.
~~~from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Protocols</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            padding: 30px;
        }

        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 10px #cccccc;
        }

        h2 {
            text-align: center;
            color: #2563eb;
        }

        ul {
            list-style-type: square;
            padding-left: 25px;
        }

        li {
            padding: 10px;
            margin: 5px 0;
            background: #e8f0fe;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>List of Network Protocols</h2>

        <ul id="protocolList"></ul>
    </div>

    <script>
        const protocols = [
            "TCP",
            "IP",
            "HTTP",
            "HTTPS",
            "FTP",
            "DNS",
            "DHCP",
            "SMTP",
            "SSH",
            "TLS",
            "UDP",
            "IMAP"
        ];

        const list = document.getElementById("protocolList");

        protocols.forEach(function(protocol) {
            const item = document.createElement("li");
            item.textContent = protocol;
            list.appendChild(item);
        });
    </script>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',88)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~
### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Protocols</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            padding: 30px;
        }

        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 10px #cccccc;
        }

        h2 {
            text-align: center;
            color: #2563eb;
        }

        ul {
            list-style-type: square;
            padding-left: 25px;
        }

        li {
            padding: 10px;
            margin: 5px 0;
            background: #e8f0fe;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>List of Network Protocols</h2>

        <ul id="protocolList"></ul>
    </div>

    <script>
        const protocols = [
            "TCP",
            "IP",
            "HTTP",
            "HTTPS",
            "FTP",
            "DNS",
            "DHCP",
            "SMTP",
            "SSH",
            "TLS",
            "UDP",
            "IMAP"
        ];

        const list = document.getElementById("protocolList");

        protocols.forEach(function(protocol) {
            const item = document.createElement("li");
            item.textContent = protocol;
            list.appendChild(item);
        });
    </script>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',88)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~



## OUTPUT:
![alt text](<Screenshot 2026-10-15 143126.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

