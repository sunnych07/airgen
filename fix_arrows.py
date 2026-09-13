with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('CLICK TO VIEW 4 MODULES ?', 'CLICK TO VIEW 4 MODULES &#8599;')
content = content.replace('CLICK TO VIEW 6 MODULES ?', 'CLICK TO VIEW 6 MODULES &#8599;')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed missing arrow icons in Journey cards.")
