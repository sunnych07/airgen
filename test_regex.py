with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
old_courses_pattern = r'<div id="courses".*?<!-- CADETS PAGE -->'

match = re.search(old_courses_pattern, content, flags=re.DOTALL)
if match:
    print("Found old courses")
else:
    print("Did not find old courses")

