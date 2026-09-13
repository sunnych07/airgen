import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken emoji from previous powershell run
content = content.replace('<span style="font-size: 1.2rem;">??</span>', '<span style="font-size: 1.2rem;">&#128172;</span>')

# Make absolutely sure it's on top of everything
content = content.replace('z-index: 999; transition: 0.3s; display: flex;', 'z-index: 999999; transition: 0.3s; display: flex;')
content = content.replace('z-index: 999; overflow: hidden; flex-direction: column;', 'z-index: 999999; overflow: hidden; flex-direction: column;')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed chat button visibility and emoji.")
