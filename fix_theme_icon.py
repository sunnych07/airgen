with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('&#127542;', '&#127769;')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
