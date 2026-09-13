with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix ReferenceError in requestLoginOTP
old_login_js = "body: JSON.stringify({ email: email, otp: generatedOTP, name: name, phone: phone })"
new_login_js = "body: JSON.stringify({ email: email, otp: generatedOTP })"
content = content.replace(old_login_js, new_login_js, 1) # Only replace the first match if there are multiple, but actually we want to replace the one in requestLoginOTP. Wait, it is in requestOTP as well. 

# Actually, let's be more precise
content = content.replace('body: JSON.stringify({ email: email, otp: generatedOTP, name: name, phone: phone }) \n                });', 'body: JSON.stringify({ email: email, otp: generatedOTP }) \n                });')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
