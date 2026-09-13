from http.server import BaseHTTPRequestHandler
import json
import smtplib
from email.mime.text import MIMEText
import os
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            msg_type = data.get('type', 'otp')
            email_to = data.get('email')
            
            EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
            APP_PASSWORD = os.environ.get('APP_PASSWORD')
            SUPABASE_URL = os.environ.get('SUPABASE_URL')
            SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
            
            if not EMAIL_ADDRESS or not APP_PASSWORD:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': 'Missing Env Vars'}).encode('utf-8'))
                return

            if msg_type == 'admin_message':
                # Sending a message TO the admin FROM the user
                user_msg = data.get('message', '')
                
                msg = MIMEText(f"Message from Authenticated User ({email_to}):\n\n{user_msg}")
                msg["Subject"] = f"New Inquiry from {email_to}"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = EMAIL_ADDRESS # Sending to admin
                
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL_ADDRESS, APP_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
                server.quit()
                
            else:
                # OTP logic
                otp = data.get('otp')
                name = data.get('name')
                phone = data.get('phone')
                
                # 1. Save to Supabase (if variables exist and it's a registration)
                if SUPABASE_URL and SUPABASE_KEY and name and phone:
                    try:
                        headers = {
                            "apikey": SUPABASE_KEY,
                            "Authorization": f"Bearer {SUPABASE_KEY}",
                            "Content-Type": "application/json",
                            "Prefer": "return=minimal"
                        }
                        payload = json.dumps({"name": name, "phone": phone, "email": email_to}).encode('utf-8')
                        req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/students", data=payload, headers=headers, method="POST")
                        urllib.request.urlopen(req)
                    except Exception as e:
                        print(f"Supabase Error: {e}")

                # 2. Send the OTP Email
                msg = MIMEText(f"Your AirGen Aviation secure code is: {otp}")
                msg["Subject"] = "AirGen Secure Authentication"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = email_to
                
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL_ADDRESS, APP_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, email_to, msg.as_string())
                server.quit()
            
            # Success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))

