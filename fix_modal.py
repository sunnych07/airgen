import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix modal icons
content = content.replace('<span style="font-size: 1.2rem;">??</span> DURATION', '<span style="font-size: 1.2rem;">&#9201;</span> DURATION')
content = content.replace('<span style="font-size: 1.2rem;">??</span> YOU ENTER WITH', '<span style="font-size: 1.2rem;">&#127891;</span> YOU ENTER WITH')
content = content.replace('<span style="font-size: 1.2rem;">??</span> YOU LEAVE WITH', '<span style="font-size: 1.2rem;">&#128188;</span> YOU LEAVE WITH')
content = content.replace('<span style="font-size: 1.2rem;">??</span> GATE', '<span style="font-size: 1.2rem;">&#128682;</span> GATE')

# Fix modal button arrow
content = content.replace('ASK ABOUT ${data.title.toUpperCase()} ?', 'ASK ABOUT ${data.title.toUpperCase()} &#8599;')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed modal question marks to beautiful emojis.")
