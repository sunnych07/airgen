import re
with open(r'C:\airgen\auth_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole navbar h1 just to be 100% sure we get it
content = re.sub(
    r'<nav class=\"nav-header\" data-aos=\"fade-down\">\s*<h1.*?</h1>',
    '''<nav class=\"nav-header\" data-aos=\"fade-down\">
        <div style=\"display: flex; align-items: center; gap: 0.75rem; cursor: pointer;\" onclick=\"showPage('home')\">
            <img src=\"https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=150\" style=\"width: 32px; height: 32px; border-radius: 50%; object-fit: cover; border: 2px solid #38BDF8;\">
            <h1 style=\"font-size: 1.5rem; font-weight: 900; color: #38BDF8; letter-spacing: 2px; margin: 0;\">AIRGEN <span style=\"color:white; font-weight:300;\">AVIATION</span></h1>
        </div>''',
    content,
    flags=re.DOTALL
)

with open(r'C:\airgen\auth_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)
