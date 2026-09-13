import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# requestOTP needs name and phone for Supabase
old_block = """async function requestOTP() {
            const name = document.getElementById('regName').value;
            const phone = document.getElementById('regPhone').value;
            const email = document.getElementById('regEmail').value;
            const terms = document.getElementById('regTerms').checked;

            if (!name || !phone || !email) { alert("Please fill all fields."); return; }
            if (!terms) { alert("Please accept the Terms & Conditions."); return; }

            currentEmail = email;
            generatedOTP = Math.floor(100000 + Math.random() * 900000).toString(); // Generate 6 digit OTP

            const btn = document.getElementById('regBtn');
            btn.innerText = "Authenticating...";
            btn.classList.add('btn-loading');
            btn.disabled = true;

            try {
                const res = await fetch('/api/send_email', { 
                    method: 'POST', 
                    body: JSON.stringify({ email: email, otp: generatedOTP }) 
                });"""

new_block = """async function requestOTP() {
            const name = document.getElementById('regName').value;
            const phone = document.getElementById('regPhone').value;
            const email = document.getElementById('regEmail').value;
            const terms = document.getElementById('regTerms').checked;

            if (!name || !phone || !email) { alert("Please fill all fields."); return; }
            if (!terms) { alert("Please accept the Terms & Conditions."); return; }

            currentEmail = email;
            generatedOTP = Math.floor(100000 + Math.random() * 900000).toString(); // Generate 6 digit OTP

            const btn = document.getElementById('regBtn');
            btn.innerText = "Authenticating...";
            btn.classList.add('btn-loading');
            btn.disabled = true;

            try {
                const res = await fetch('/api/send_email', { 
                    method: 'POST', 
                    body: JSON.stringify({ email: email, otp: generatedOTP, name: name, phone: phone }) 
                });"""

content = content.replace(old_block, new_block)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored name and phone to requestOTP payload.")
