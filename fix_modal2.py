import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the faulty loop entirely
pattern = r'data\.modules\.forEach\(mod => \{.*?modulesContainer\.appendChild\(div\);\s*\}\);'

fixed_loop = """data.modules.forEach(mod => {
                const div = document.createElement('div');
                div.style.background = 'rgba(255,255,255,0.02)';
                div.style.padding = '1.5rem';
                div.style.borderRadius = '0.5rem';
                div.style.borderLeft = '3px solid ' + data.color;
                div.innerHTML = '<div style="color: ' + data.color + '; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE ' + mod.id + '</div><h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;">' + mod.title + '</h4><p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;">' + mod.desc + '</p>';
                modulesContainer.appendChild(div);
            });"""

content = re.sub(pattern, fixed_loop, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Regex replace complete.")
