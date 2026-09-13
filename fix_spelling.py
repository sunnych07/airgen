with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken DARK button and wire it up to toggleTheme()
content = content.replace('&amp;#9728; DARK &amp;#9662;', '☀️ THEME 🌙')
content = content.replace('cursor: pointer;">☀️ THEME 🌙</button>', 'cursor: pointer;" onclick="toggleTheme()">☀️ THEME 🌙</button>')

# Fix the ENQUIRE button arrow
content = content.replace('ENQUIRE &amp;#8599;', 'ENQUIRE ↗')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed spelling and broken emojis in navbar.")
