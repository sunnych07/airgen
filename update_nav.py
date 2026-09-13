import re

with open(r'C:\airgen\auth_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_navbar = '''
    <style>
        .nav-link { color: #94A3B8; text-decoration: none; transition: 0.3s; }
        .nav-link:hover { color: white; }
        
        .logo-svg { width: 35px; height: 35px; margin-right: 12px; }
        .logo-wing-w1 { fill: white; }
        .logo-wing-r { fill: #E11D48; }
        .logo-wing-w2 { fill: white; }
    </style>
    
    <nav class="nav-header" data-aos="fade-down" style="padding: 1rem 4%; background: #030712; border-bottom: 1px solid rgba(255,255,255,0.05);">
        <!-- Logo -->
        <div style="display: flex; align-items: center; cursor: pointer;" onclick="showPage('home')">
            <svg class="logo-svg" viewBox="0 0 100 100">
                <polygon points="20,80 80,20 80,35 35,80" class="logo-wing-w1" />
                <polygon points="10,60 50,20 50,35 25,60" class="logo-wing-r" />
                <polygon points="10,95 95,10 95,25 25,95" class="logo-wing-r" />
            </svg>
            <div style="line-height: 1;">
                <div style="font-size: 1.8rem; font-weight: 800; letter-spacing: -0.5px;">
                    <span style="color: white;">Air</span><span style="color: #E11D48;">Gen</span>
                </div>
                <div style="font-size: 0.65rem; color: white; letter-spacing: 0.4em; margin-top: 2px;">AVIATION</div>
            </div>
        </div>

        <!-- Center Links -->
        <div style="display: flex; gap: 2.5rem; font-size: 0.8rem; font-weight: 600; letter-spacing: 1.5px;">
            <a href="#" onclick="showPage('about')" class="nav-link">ABOUT</a>
            <a href="#" onclick="showPage('journey')" class="nav-link">JOURNEY</a>
            <a href="#" onclick="showPage('cadets')" class="nav-link">CADETS</a>
            <a href="#" onclick="showPage('founders')" class="nav-link">FOUNDERS</a>
            <a href="#" onclick="showPage('courses')" class="nav-link">COURSES</a>
        </div>

        <!-- Right Buttons -->
        <div style="display: flex; gap: 1rem; align-items: center;">
            <button style="border: 1px solid #334155; background: transparent; padding: 0.5rem 1rem; border-radius: 20px; color: white; font-size: 0.75rem; font-weight: 600; cursor: pointer;">&amp;#9728; DARK &amp;#9662;</button>
            <button onclick="showPage('register')" style="border: 1px solid #E11D48; background: rgba(225,29,72,0.05); padding: 0.6rem 1.5rem; border-radius: 8px; color: white; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; cursor: pointer; transition: 0.3s;" onmouseover="this.style.background='#E11D48'" onmouseout="this.style.background='rgba(225,29,72,0.05)'">ENQUIRE &amp;#8599;</button>
        </div>
    </nav>
'''

content = re.sub(r'<nav class=\"nav-header\".*?</nav>', new_navbar, content, flags=re.DOTALL)

placeholder_pages = '''
        <!-- ABOUT PAGE -->
        <div id="about" class="page-section hidden-section fade-in" style="width: 100%; padding: 1rem; text-align: center;">
            <div class="glass-card"><h2 style="font-size: 2rem; color: white; font-weight: 800;">About AirGen</h2><p style="color: #94A3B8; margin-top: 1rem;">Information about the academy will go here.</p></div>
        </div>
        <!-- JOURNEY PAGE -->
        <div id="journey" class="page-section hidden-section fade-in" style="width: 100%; padding: 1rem; text-align: center;">
            <div class="glass-card"><h2 style="font-size: 2rem; color: white; font-weight: 800;">The Pilot Journey</h2><p style="color: #94A3B8; margin-top: 1rem;">18-month roadmap details go here.</p></div>
        </div>
        <!-- CADETS PAGE -->
        <div id="cadets" class="page-section hidden-section fade-in" style="width: 100%; padding: 1rem; text-align: center;">
            <div class="glass-card"><h2 style="font-size: 2rem; color: white; font-weight: 800;">Our Cadets</h2><p style="color: #94A3B8; margin-top: 1rem;">Hall of Wings and alumni placement details go here.</p></div>
        </div>
        <!-- FOUNDERS PAGE -->
        <div id="founders" class="page-section hidden-section fade-in" style="width: 100%; padding: 1rem; text-align: center;">
            <div class="glass-card"><h2 style="font-size: 2rem; color: white; font-weight: 800;">Founders</h2><p style="color: #94A3B8; margin-top: 1rem;">Captain Manas Teja & Leadership team details go here.</p></div>
        </div>
        <!-- COURSES PAGE -->
        <div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 1rem; text-align: center;">
            <div class="glass-card"><h2 style="font-size: 2rem; color: white; font-weight: 800;">Training Courses</h2><p style="color: #94A3B8; margin-top: 1rem;">CPL, Ground Classes, and Type Rating details go here.</p></div>
        </div>
        <!-- REGISTER PAGE -->
'''

content = content.replace('<!-- REGISTER PAGE -->', placeholder_pages)

with open(r'C:\airgen\auth_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)
