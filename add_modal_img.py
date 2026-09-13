import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will add an <img> tag to the top of the modal, using data.img.
old_modal_start = """              <div style="max-width: 900px; margin: 2rem auto; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); border-radius: 1.5rem; overflow: hidden; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8);">
                  
                  <!-- Glow Effect -->
                  <div style="position: absolute; top: -100px; left: -100px; width: 300px; height: 300px; background: ${data.color}; filter: blur(150px); opacity: 0.15; z-index: 0; pointer-events: none;"></div>
  
                  <div style="padding: 4rem; position: relative; z-index: 1;">"""

new_modal_start = """              <div style="max-width: 900px; margin: 2rem auto; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); border-radius: 1.5rem; overflow: hidden; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8);">
                  
                  <!-- Hero Image for Modal -->
                  <img src="${data.img}" style="width: 100%; height: 250px; object-fit: cover; border-bottom: 1px solid rgba(255,255,255,0.1);">

                  <!-- Glow Effect -->
                  <div style="position: absolute; top: 150px; left: -100px; width: 300px; height: 300px; background: ${data.color}; filter: blur(150px); opacity: 0.15; z-index: 0; pointer-events: none;"></div>
  
                  <div style="padding: 4rem; position: relative; z-index: 1;">"""

content = content.replace(old_modal_start, new_modal_start)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added hero image to the journey modal.")
