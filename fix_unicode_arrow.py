with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\u2197', '&#8599;')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced raw arrow unicode with HTML entity.")
