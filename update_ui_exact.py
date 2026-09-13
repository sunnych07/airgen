import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_courses_pattern = r'<div id="courses".*?<!-- REGISTER PAGE -->'

new_courses = """<div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 4rem 2rem; max-width: 1400px; margin: 0 auto; background: #030712;">
            
            <!-- 3 Regulatory Cards -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                
                <!-- DGCA -->
                <div style="border-radius: 0.5rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; padding: 2rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">DGCA</span>
                        <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">India</span>
                    </div>
                    <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1.2rem; letter-spacing: -0.5px;">Domestic airline pathway</h3>
                    <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.7; font-weight: 300;">Full ATPL and CPL subject coverage designed for Indian airline recruitment, with the mental maths, radio telephony and scenario work selection actually rewards.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b;">
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Air Navigation & Flight Planning</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Aviation Meteorology & radar interpretation</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Air Regulations & ICAO annexes</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Technical General & aircraft systems</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">RTR(A) radio telephony exam preparation</div>
                    </div>
                </div>

                <!-- FAA -->
                <div style="border-radius: 0.5rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; padding: 2rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">FAA</span>
                        <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">United States</span>
                    </div>
                    <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1.2rem; letter-spacing: -0.5px;">Global fast-track pathway</h3>
                    <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.7; font-weight: 300;">Scenario-led training built around the FAA Airman Certification Standards, for rapid hour building in high-density US airspace.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b;">
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Private pilot ground & flight preparation</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Instrument rating under actual IMC</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Commercial multi-engine (CPL-ME)</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Oral exam & checkride scenario drills</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">DGCA licence conversion protocol</div>
                    </div>
                </div>

                <!-- EASA -->
                <div style="border-radius: 0.5rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; padding: 2rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">EASA</span>
                        <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">Europe</span>
                    </div>
                    <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1.2rem; letter-spacing: -0.5px;">Gold standard theory pathway</h3>
                    <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.7; font-weight: 300;">Rigorous 13-subject ATPL theory integrated with Area 100 KSA, which maps directly onto the ASK framework.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b;">
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">13 EASA ATPL theoretical subjects</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Area 100 KSA competency assessments</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Advanced high-altitude aerodynamics</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Performance-based navigation (PBN)</div>
                        <div style="padding: 1.2rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Assessment centre preparation</div>
                    </div>
                </div>

            </div>

            <!-- Inclusions Checklist -->
            <div style="border: 1px solid #1e293b; border-radius: 0.5rem; padding: 2rem; background: #020617; margin-top: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2.5rem;">
                    <h3 style="color: white; font-size: 1.2rem; font-weight: 700; margin: 0;">Included in every pathway</h3>
                    <div style="color: #64748b; font-weight: 700; font-family: monospace; font-size: 0.75rem; letter-spacing: 1px;">8 INCLUSIONS</div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">Live interactive virtual classrooms</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">24/7 access to recorded modules & notes</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">Adaptive CBT question bank engine</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">Mock examinations matching real patterns</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">Real-time weak-area performance analytics</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">1-on-1 mentorship with active airline pilots</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">DGCA Class 1 & 2 medical appointment guidance</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">DGCA computer number processing support</span>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 3rem;">
                <button onclick="toggleChat()" style="background: transparent; color: #f43f5e; border: 1px solid #f43f5e; padding: 0.8rem 3rem; border-radius: 3rem; font-weight: 800; cursor: pointer; transition: 0.3s;" onmouseover="this.style.background='#f43f5e'; this.style.color='#000'" onmouseout="this.style.background='transparent'; this.style.color='#f43f5e'">ENQUIRE ABOUT PATHWAYS ↗</button>
            </div>
        </div>
        <!-- REGISTER PAGE -->"""

content = re.sub(old_courses_pattern, new_courses, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Courses UI to match image precisely.")
