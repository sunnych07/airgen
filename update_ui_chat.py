import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Chat Modal and Button UI right before the journey modal
chat_ui = """
    <!-- FLOATING CHAT BUTTON -->
    <div id="floatingChatBtn" onclick="toggleChat()" style="position: fixed; bottom: 30px; right: 30px; background: #38BDF8; color: #030712; padding: 1rem 1.5rem; border-radius: 30px; cursor: pointer; font-weight: 800; box-shadow: 0 10px 25px rgba(56,189,248,0.4); z-index: 999; transition: 0.3s; display: flex; align-items: center; gap: 0.5rem;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
        <span style="font-size: 1.2rem;">💬</span> For Details
    </div>

    <!-- CHAT MODAL -->
    <div id="chatModal" style="display: none; position: fixed; bottom: 90px; right: 30px; width: 350px; background: #0f172a; border: 1px solid rgba(56,189,248,0.3); border-radius: 1rem; box-shadow: 0 25px 50px rgba(0,0,0,0.5); z-index: 999; overflow: hidden; flex-direction: column;">
        <div style="background: rgba(56,189,248,0.1); padding: 1rem; border-bottom: 1px solid rgba(56,189,248,0.2); display: flex; justify-content: space-between; align-items: center;">
            <h4 style="color: white; margin: 0; font-weight: 700;">Message Admin</h4>
            <button onclick="toggleChat()" style="background: none; border: none; color: #94A3B8; cursor: pointer; font-size: 1.5rem; line-height: 1;">×</button>
        </div>
        <div style="padding: 1.5rem;">
            <textarea id="chatMessage" rows="4" placeholder="Type your message here..." style="width: 100%; background: rgba(0,0,0,0.3); border: 1px solid #334155; padding: 0.8rem; border-radius: 0.5rem; color: white; margin-bottom: 1rem; resize: none; font-family: 'Inter', sans-serif;"></textarea>
            <button id="sendChatBtn" onclick="sendAdminMessage()" class="btn-primary" style="width: 100%; padding: 0.8rem; font-size: 0.9rem;">Send Message</button>
        </div>
    </div>
"""

content = content.replace('<!-- JOURNEY MODAL -->', chat_ui + '\n    <!-- JOURNEY MODAL -->')

# 2. Add JS state and logic
js_vars = """
        let currentEmail = "";
        let generatedOTP = ""; // Store OTP in frontend for serverless
        let isLoggedIn = false;
        let loggedInEmail = "";
"""
content = content.replace('let currentEmail = "";\n        let generatedOTP = ""; // Store OTP in frontend for serverless', js_vars)

old_verify = """if (otp === generatedOTP) { 
                    showPage('success'); 
                } else {"""
new_verify = """if (otp === generatedOTP) { 
                    isLoggedIn = true;
                    loggedInEmail = currentEmail;
                    showPage('success'); 
                } else {"""
content = content.replace(old_verify, new_verify)

# 3. Add Chat Functions
chat_funcs = """
        function toggleChat() {
            if (!isLoggedIn) {
                alert("Please Login or Enquire first to contact the admin.");
                showPage('register');
                return;
            }
            const cm = document.getElementById('chatModal');
            cm.style.display = (cm.style.display === 'none' || cm.style.display === '') ? 'flex' : 'none';
        }

        async function sendAdminMessage() {
            const msg = document.getElementById('chatMessage').value;
            if (!msg.trim()) return;
            
            const btn = document.getElementById('sendChatBtn');
            btn.innerText = "Sending...";
            btn.disabled = true;

            try {
                const res = await fetch('/api/send_email', {
                    method: 'POST',
                    body: JSON.stringify({ type: 'admin_message', email: loggedInEmail, message: msg })
                });
                const data = await res.json();
                if (data.success) {
                    alert("Message sent securely to the Admin!");
                    document.getElementById('chatMessage').value = '';
                    toggleChat();
                } else {
                    alert("Failed to send message.");
                }
            } catch(e) {
                alert("Network error.");
            } finally {
                btn.innerText = "Send Message";
                btn.disabled = false;
            }
        }
"""
content = content.replace('function closeJourneyModal() {\n            document.getElementById(\'journeyModal\').style.display = \'none\';\n        }', 'function closeJourneyModal() {\n            document.getElementById(\'journeyModal\').style.display = \'none\';\n        }\n' + chat_funcs)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added UI and JS for Chat logic.")
