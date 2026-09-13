import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Courses Section
old_courses_pattern = r'<div id="courses".*?<!-- CADETS PAGE -->'

new_courses = """<div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1200px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 3rem;">
                <h2 style="font-size: 3rem; color: white; font-weight: 900;" data-aos="fade-down">Training <span style="color: #E11D48;">Pathways</span></h2>
                <p style="color: #94A3B8; max-width: 600px; margin: 1rem auto;">Comprehensive aviation training programs designed to take you from zero experience to the right-hand seat of a commercial airliner.</p>
            </div>

            <!-- Course Cards with Images -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
                <!-- Card 1 -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="100" style="border-radius: 1rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #0f172a; display: flex; flex-direction: column;">
                    <img src="https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=800" style="width: 100%; height: 250px; object-fit: cover;">
                    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="color: #E11D48; font-size: 0.8rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.5rem;">INTEGRATED</div>
                        <h3 style="color: white; font-size: 1.8rem; font-weight: 800; margin-bottom: 1rem;">Zero to CPL Pathway</h3>
                        <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 2rem; flex-grow: 1; line-height: 1.6;">The complete package. From day one ground school to your final Commercial Pilot Licence flight test. We handle everything.</p>
                        <button onclick="toggleChat()" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enquire Now</button>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="300" style="border-radius: 1rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #0f172a; display: flex; flex-direction: column;">
                    <img src="https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=800" style="width: 100%; height: 250px; object-fit: cover;">
                    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="color: #38BDF8; font-size: 0.8rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.5rem;">MODULAR</div>
                        <h3 style="color: white; font-size: 1.8rem; font-weight: 800; margin-bottom: 1rem;">Type Rating & MCC</h3>
                        <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 2rem; flex-grow: 1; line-height: 1.6;">For existing CPL holders. Transition to multi-crew jet operations, master swept-wing aerodynamics, and get airline-ready.</p>
                        <button onclick="toggleChat()" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#38BDF8'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enquire Now</button>
                    </div>
                </div>
            </div>

            <!-- Inclusions Checklist -->
            <div data-aos="fade-up" data-aos-delay="500" style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 1rem; padding: 3rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1.5rem; margin-bottom: 2.5rem;">
                    <h3 style="color: white; font-size: 1.5rem; font-weight: 800; margin: 0;">Included in every pathway</h3>
                    <div style="color: #64748B; font-weight: 800; letter-spacing: 2px; font-size: 0.8rem;">8 INCLUSIONS</div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">Live interactive virtual classrooms</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">24/7 access to recorded modules & notes</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">Adaptive CBT question bank engine</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">Mock examinations matching real patterns</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">Real-time weak-area performance analytics</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">1-on-1 mentorship with active airline pilots</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">DGCA Class 1 & 2 medical appointment guidance</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #E11D48; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #cbd5e1; font-size: 1rem;">DGCA computer number processing support</span>
                    </div>
                </div>
            </div>
        </div>
        <!-- CADETS PAGE -->"""

content = re.sub(old_courses_pattern, new_courses, content, flags=re.DOTALL)

# 2. Add Dark/Light Mode Filter CSS
css_injection = """
    <style>
        .light-mode {
            filter: invert(1) hue-rotate(180deg);
            background: #ffffff;
        }
        .light-mode img, 
        .light-mode .glass-card div[style*="background: url"], 
        .light-mode #modalBg { 
            filter: invert(1) hue-rotate(180deg); 
        }
    </style>
</head>"""
content = content.replace('</head>', css_injection)

# 3. Add Theme Toggle Button to Nav and JS
nav_old = '<a href="#" onclick="showPage(\'login\'); return false;" class="btn-primary">Login</a>'
nav_new = '<a href="#" onclick="toggleTheme(); return false;" style="color: white; font-size: 1.2rem; text-decoration: none; margin-right: 1rem;">&#127542;</a>' + nav_old
content = content.replace(nav_old, nav_new)

js_injection = """
        function toggleTheme() {
            document.documentElement.classList.toggle('light-mode');
        }
"""
content = content.replace('function toggleChat() {', js_injection + '\n        function toggleChat() {')

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Courses and Theme Toggle.")
