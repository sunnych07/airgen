import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_courses_pattern = r'<div id="courses".*?<!-- CADETS PAGE -->'

new_courses = """<div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1300px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 4rem;">
                <h2 style="font-size: 3rem; color: white; font-weight: 900;" data-aos="fade-down">Regulatory <span style="color: #E11D48;">Pathways</span></h2>
                <p style="color: #94A3B8; max-width: 600px; margin: 1rem auto;">Tailored pilot training programs designed around the exact regulatory authority you wish to fly under.</p>
            </div>

            <!-- 3 Regulatory Cards -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
                
                <!-- DGCA -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="100" style="border-radius: 1rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #070B14; display: flex; flex-direction: column; padding: 2.5rem; transition: 0.3s;" onmouseover="this.style.borderColor='rgba(225,29,72,0.5)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #E11D48; font-weight: 800; font-family: monospace; font-size: 1.1rem; letter-spacing: 2px;">DGCA</span>
                        <span style="color: #64748B; font-weight: 600; font-family: monospace; font-size: 0.85rem;">India</span>
                    </div>
                    <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin-bottom: 1rem; letter-spacing: -0.5px;">Domestic airline pathway</h3>
                    <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6;">Full ATPL and CPL subject coverage designed for Indian airline recruitment, with the mental maths, radio telephony and scenario work selection actually rewards.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid rgba(255,255,255,0.05); margin-bottom: 2.5rem; flex-grow: 1;">
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Air Navigation & Flight Planning</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Aviation Meteorology & radar interpretation</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Air Regulations & ICAO annexes</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Technical General & aircraft systems</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">RTR(A) radio telephony exam preparation</div>
                    </div>

                    <button id="payBtn1" onclick="payWithRazorpay('DGCA Pathway', 35000, 'payBtn1')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s; margin-bottom: 0.8rem;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enroll & Pay Advance (₹35,000)</button>
                    <button onclick="toggleChat()" style="background: transparent; color: #E11D48; border: 1px solid #E11D48; padding: 0.8rem; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%;">Enquire First</button>
                </div>

                <!-- FAA -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="300" style="border-radius: 1rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #070B14; display: flex; flex-direction: column; padding: 2.5rem; transition: 0.3s;" onmouseover="this.style.borderColor='rgba(225,29,72,0.5)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #E11D48; font-weight: 800; font-family: monospace; font-size: 1.1rem; letter-spacing: 2px;">FAA</span>
                        <span style="color: #64748B; font-weight: 600; font-family: monospace; font-size: 0.85rem;">United States</span>
                    </div>
                    <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin-bottom: 1rem; letter-spacing: -0.5px;">Global fast-track pathway</h3>
                    <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6;">Scenario-led training built around the FAA Airman Certification Standards, for rapid hour building in high-density US airspace.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid rgba(255,255,255,0.05); margin-bottom: 2.5rem; flex-grow: 1;">
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Private pilot ground & flight preparation</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Instrument rating under actual IMC</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Commercial multi-engine (CPL-ME)</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Oral exam & checkride scenario drills</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">DGCA licence conversion protocol</div>
                    </div>

                    <button id="payBtn2" onclick="payWithRazorpay('FAA Pathway', 50000, 'payBtn2')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s; margin-bottom: 0.8rem;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enroll & Pay Advance (₹50,000)</button>
                    <button onclick="toggleChat()" style="background: transparent; color: #E11D48; border: 1px solid #E11D48; padding: 0.8rem; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%;">Enquire First</button>
                </div>

                <!-- EASA -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="500" style="border-radius: 1rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #070B14; display: flex; flex-direction: column; padding: 2.5rem; transition: 0.3s;" onmouseover="this.style.borderColor='rgba(225,29,72,0.5)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                        <span style="color: #E11D48; font-weight: 800; font-family: monospace; font-size: 1.1rem; letter-spacing: 2px;">EASA</span>
                        <span style="color: #64748B; font-weight: 600; font-family: monospace; font-size: 0.85rem;">Europe</span>
                    </div>
                    <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin-bottom: 1rem; letter-spacing: -0.5px;">Gold standard theory pathway</h3>
                    <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6;">Rigorous 13-subject ATPL theory integrated with Area 100 KSA, which maps directly onto the ASK framework.</p>
                    
                    <div style="display: flex; flex-direction: column; border-top: 1px solid rgba(255,255,255,0.05); margin-bottom: 2.5rem; flex-grow: 1;">
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">13 EASA ATPL theoretical subjects</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Area 100 KSA competency assessments</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Advanced high-altitude aerodynamics</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Performance-based navigation (PBN)</div>
                        <div style="padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; font-size: 0.9rem;">Assessment centre preparation</div>
                    </div>

                    <button id="payBtn3" onclick="payWithRazorpay('EASA Pathway', 45000, 'payBtn3')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s; margin-bottom: 0.8rem;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enroll & Pay Advance (₹45,000)</button>
                    <button onclick="toggleChat()" style="background: transparent; color: #E11D48; border: 1px solid #E11D48; padding: 0.8rem; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%;">Enquire First</button>
                </div>

            </div>

            <!-- Inclusions Checklist -->
            <div data-aos="fade-up" data-aos-delay="600" style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 1rem; padding: 3rem;">
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

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Courses Page with DGCA, FAA, EASA Pathways")
