import re

with open(r'C:\airgen\api\send_email.py', 'r', encoding='utf-8') as f:
    content = f.read()

bad_str = """msg = MIMEText(f"Message from Authenticated User ({email_to}):

{user_msg}")"""

good_str = 'msg = MIMEText(f"Message from Authenticated User ({email_to}):\\n\\n{user_msg}")'

content = content.replace(bad_str, good_str)

with open(r'C:\airgen\api\send_email.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed syntax error in send_email.py")
