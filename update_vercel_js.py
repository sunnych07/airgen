import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the JS script portion to handle Serverless OTP logic
js_replacement = '''
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init();
        let currentEmail = "";
        let generatedOTP = ""; // Store OTP in frontend for serverless

        function showPage(pageId) {
            document.querySelectorAll('.page-section').forEach(el => {
                el.classList.add('hidden-section');
                el.classList.remove('fade-in');
            });
            const target = document.getElementById(pageId);
            target.classList.remove('hidden-section');
            void target.offsetWidth;
            target.classList.add('fade-in');
            document.getElementById('otpInput').value = '';
        }

        async function requestOTP() {
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
                });
                const data = await res.json();
                if (data.success) { showPage('otp'); } else { alert("Failed to send email. Ensure Vercel Env Vars are set."); }
            } catch(e) {
                alert("Network error. Is the Vercel API running?");
            } finally {
                btn.innerText = "Verify Email";
                btn.classList.remove('btn-loading');
                btn.disabled = false;
            }
        }

        async function requestLoginOTP() {
            const email = document.getElementById('loginEmail').value;
            if (!email) { alert("Please enter your email."); return; }
            currentEmail = email;
            generatedOTP = Math.floor(100000 + Math.random() * 900000).toString();
            
            const btn = document.getElementById('loginBtn');
            btn.innerText = "Establishing Link...";
            btn.classList.add('btn-loading');
            btn.disabled = true;

            try {
                const res = await fetch('/api/send_email', { 
                    method: 'POST', 
                    body: JSON.stringify({ email: email, otp: generatedOTP }) 
                });
                const data = await res.json();
                if (data.success) { showPage('otp'); } else { alert("Failed to send email."); }
            } catch(e) {
                alert("Network error.");
            } finally {
                btn.innerText = "Send Secure OTP";
                btn.classList.remove('btn-loading');
                btn.disabled = false;
            }
        }

        function verifyOTP() {
            const otp = document.getElementById('otpInput').value;
            if (!otp) { alert("Enter the 6-digit OTP."); return; }

            const btn = document.getElementById('verifyBtn');
            btn.innerText = "Verifying...";
            btn.disabled = true;

            setTimeout(() => {
                if (otp === generatedOTP) { 
                    showPage('success'); 
                } else { 
                    alert("Invalid OTP. Try again."); 
                }
                btn.innerText = "Authenticate";
                btn.disabled = false;
            }, 500); // Fake small delay for realistic UX
        }
    </script>
</body>
'''

content = re.sub(r'<script src=\"https://unpkg\.com/aos@2\.3\.1/dist/aos\.js\"></script>.*?</body>', js_replacement, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
