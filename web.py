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
