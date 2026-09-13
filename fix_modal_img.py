import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_line = "document.getElementById('modalBg').style.backgroundImage = url('');"
good_line = "document.getElementById('modalBg').style.backgroundImage = \"url('\" + data.img + \"')\";"

content = content.replace(bad_line, good_line)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed background image JS bug.")
