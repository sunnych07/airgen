import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken template literal
broken_js = """                div.innerHTML = `
                    <div style="color: ; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE </div>
                    <h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;"></h4>
                    <p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;"></p>
                `;"""

fixed_js = """                div.innerHTML = '<div style="color: ' + data.color + '; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE ' + mod.id + '</div><h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;">' + mod.title + '</h4><p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;">' + mod.desc + '</p>';"""

content = content.replace(broken_js, fixed_js)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
