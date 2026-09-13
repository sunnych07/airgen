from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import base64
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            amount = data.get('amount', 500000) # Default 5000 INR in paise
            
            # Using the hardcoded keys provided by the user for the hackathon prototype
            KEY_ID = "rzp_live_TZ4lxunOpCOa6H"
            KEY_SECRET = "62QIVSOqF7jgxLDiNCTYFrkq"
            
            auth_string = f"{KEY_ID}:{KEY_SECRET}"
            auth_bytes = auth_string.encode('ascii')
            base64_bytes = base64.b64encode(auth_bytes)
            base64_string = base64_bytes.decode('ascii')
            
            payload = json.dumps({
                "amount": amount,
                "currency": "INR",
                "receipt": "airgen_course_enrollment"
            }).encode('utf-8')
            
            req = urllib.request.Request("https://api.razorpay.com/v1/orders", data=payload, method="POST")
            req.add_header("Authorization", f"Basic {base64_string}")
            req.add_header("Content-Type", "application/json")
            
            response = urllib.request.urlopen(req)
            resp_data = json.loads(response.read().decode('utf-8'))
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'order_id': resp_data['id']}).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))
