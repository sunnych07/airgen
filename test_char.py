with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
match = re.search(r'CLICK TO VIEW 6 MODULES (.*?)</p>', content)
if match:
    print(f"Found character: {repr(match.group(1))}")
