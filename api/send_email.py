from http.server import BaseHTTPRequestHandler
import json
import smtplib
from email.mime.text import MIMEText
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            email_to = data.get('email')
            otp = data.get('otp')
            
            # Fetch credentials from Vercel Environment Variables
            EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
            APP_PASSWORD = os.environ.get('APP_PASSWORD')
            
            if not EMAIL_ADDRESS or not APP_PASSWORD:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': 'Missing Env Vars'}).encode('utf-8'))
                return

            msg = MIMEText(f"Your AirGen Aviation secure code is: {otp}")
            msg["Subject"] = "AirGen Secure Authentication"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email_to
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email_to, msg.as_string())
            server.quit()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))
