with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="intro.mp4"', 'src="/intro.mp4"')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated video src to absolute path.")
