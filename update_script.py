import re

with open(r'C:\airgen\auth_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: The 'Enter Dashboard' button routing
content = content.replace(
    'onclick=\"showPage(''home'')\" class=\"btn-primary\" style=\"background: #10B981; box-shadow: 0 10px 20px rgba(16, 185, 129, 0.3); color: white;\">Enter Dashboard',
    'onclick=\"window.location.href=''https://version-1-s4z5.onrender.com/''\" class=\"btn-primary\" style=\"background: #10B981; box-shadow: 0 10px 20px rgba(16, 185, 129, 0.3); color: white;\">Enter Dashboard'
)

# Fix 2: Replace broken '?' emoji in Success box
content = re.sub(
    r'<div style=\"font-size: 5rem; margin-bottom: 1rem; animation: bounceIn 1s;\">\?</div>',
    '''<div style=\"margin-bottom: 1.5rem; display: flex; justify-content: center;\">
            <img src=\"https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=400\" style=\"width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid #10B981; box-shadow: 0 0 20px rgba(16,185,129,0.4);\">
       </div>''',
    content
)

# Fix 3: Replace broken '?' logo in Navbar
content = re.sub(
    r'<h1 onclick=\"showPage\(''home''\)\"[^>]*>\s*\?\s*AIRGEN[^<]*<span[^>]*>AVIATION</span>\s*</h1>',
    '''<div style=\"display: flex; align-items: center; gap: 0.75rem; cursor: pointer;\" onclick=\"showPage('home')\">
            <img src=\"https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=150\" style=\"width: 32px; height: 32px; border-radius: 50%; object-fit: cover; border: 2px solid #38BDF8;\">
            <h1 style=\"font-size: 1.5rem; font-weight: 900; color: #38BDF8; letter-spacing: 2px; margin: 0;\">AIRGEN <span style=\"color:white; font-weight:300;\">AVIATION</span></h1>
        </div>''',
    content
)

with open(r'C:\airgen\auth_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)
