import re

with open('c:/airgen/bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

sentences = set(re.findall(r'>([^<>{}\n]{15,120})<', text))
quoted = set(re.findall(r'"([^"\\{\}\n]{20,120})"', text))

all_text = sorted(list(sentences | quoted))
print(f"Total extracted strings: {len(all_text)}")
with open('c:/airgen/extracted_strings.txt', 'w', encoding='utf-8') as out:
    for item in all_text:
        out.write(item + '\n')

print("Sample matching aviation:")
for item in all_text:
    if any(k in item.lower() for k in ['pilot', 'dgca', 'cpl', 'airgen', 'train', 'flight', 'student', 'hour', 'course', 'ground', 'license', 'airline', 'career', 'cadet', 'mentor']):
        print('-', item)
