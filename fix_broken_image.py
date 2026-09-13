with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('1626245389650-8b1b8606c117', '1569154941061-e231b4725ef1')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced broken Unsplash image ID with a working one.")
