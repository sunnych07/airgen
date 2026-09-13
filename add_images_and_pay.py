import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_courses_pattern = r'<div id="courses".*?<!-- REGISTER PAGE -->'

new_courses = """<div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 4rem 2rem; max-width: 1400px; margin: 0 auto; background: #030712;">
            
            <div style="text-align: center; margin-bottom: 4rem;">
                <h2 style="font-size: 3rem; color: white; font-weight: 900;" data-aos="fade-down">Regulatory <span style="color: #f43f5e;">Pathways</span></h2>
                <p style="color: #94A3B8; max-width: 600px; margin: 1rem auto;">Tailored pilot training programs designed around the exact regulatory authority you wish to fly under.</p>
            </div>

            <!-- 3 Regulatory Cards With Images and Razorpay -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
                
                <!-- DGCA -->
                <div style="border-radius: 0.8rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s;" onmouseover="this.style.borderColor='#f43f5e'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='#1e293b'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #1e293b;">
                    <div style="padding: 2rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                            <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">DGCA</span>
                            <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">India</span>
                        </div>
                        <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1rem; letter-spacing: -0.5px;">Domestic airline pathway</h3>
                        <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6; font-weight: 300;">Full ATPL and CPL subject coverage designed for Indian airline recruitment, with the mental maths, radio telephony and scenario work selection actually rewards.</p>
                        
                        <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b; margin-bottom: 2rem; flex-grow: 1;">
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Air Navigation & Flight Planning</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Aviation Meteorology & radar interpretation</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Air Regulations & ICAO annexes</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Technical General & aircraft systems</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">RTR(A) radio telephony exam preparation</div>
                        </div>

                        <button id="payBtn1" onclick="payWithRazorpay('DGCA Pathway', 35000, 'payBtn1')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 0.5rem; font-weight: 700; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#f43f5e'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Apply Now & Pay (₹35,000)</button>
                    </div>
                </div>

                <!-- FAA -->
                <div style="border-radius: 0.8rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s;" onmouseover="this.style.borderColor='#f43f5e'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='#1e293b'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #1e293b;">
                    <div style="padding: 2rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                            <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">FAA</span>
                            <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">United States</span>
                        </div>
                        <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1rem; letter-spacing: -0.5px;">Global fast-track pathway</h3>
                        <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6; font-weight: 300;">Scenario-led training built around the FAA Airman Certification Standards, for rapid hour building in high-density US airspace.</p>
                        
                        <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b; margin-bottom: 2rem; flex-grow: 1;">
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Private pilot ground & flight preparation</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Instrument rating under actual IMC</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Commercial multi-engine (CPL-ME)</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Oral exam & checkride scenario drills</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">DGCA licence conversion protocol</div>
                        </div>

                        <button id="payBtn2" onclick="payWithRazorpay('FAA Pathway', 50000, 'payBtn2')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 0.5rem; font-weight: 700; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#f43f5e'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Apply Now & Pay (₹50,000)</button>
                    </div>
                </div>

                <!-- EASA -->
                <div style="border-radius: 0.8rem; border: 1px solid #1e293b; background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s;" onmouseover="this.style.borderColor='#f43f5e'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='#1e293b'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1569154941061-e231b4725ef1?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid #1e293b;">
                    <div style="padding: 2rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                            <span style="color: #f43f5e; font-weight: 700; font-family: monospace; font-size: 0.9rem; letter-spacing: 1px;">EASA</span>
                            <span style="color: #64748b; font-weight: 500; font-family: monospace; font-size: 0.8rem;">Europe</span>
                        </div>
                        <h3 style="color: white; font-size: 1.5rem; font-weight: 500; margin-bottom: 1rem; letter-spacing: -0.5px;">Gold standard theory pathway</h3>
                        <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6; font-weight: 300;">Rigorous 13-subject ATPL theory integrated with Area 100 KSA, which maps directly onto the ASK framework.</p>
                        
                        <div style="display: flex; flex-direction: column; border-top: 1px solid #1e293b; margin-bottom: 2rem; flex-grow: 1;">
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">13 EASA ATPL theoretical subjects</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Area 100 KSA competency assessments</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Advanced high-altitude aerodynamics</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Performance-based navigation (PBN)</div>
                            <div style="padding: 1rem 0; border-bottom: 1px solid #1e293b; color: #cbd5e1; font-size: 0.85rem; font-weight: 300;">Assessment centre preparation</div>
                        </div>

                        <button id="payBtn3" onclick="payWithRazorpay('EASA Pathway', 45000, 'payBtn3')" style="background: white; color: black; padding: 1rem; border: none; border-radius: 0.5rem; font-weight: 700; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#f43f5e'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Apply Now & Pay (₹45,000)</button>
                    </div>
                </div>

            </div>

            <!-- Inclusions Checklist -->
            <div style="border: 1px solid #1e293b; border-radius: 0.8rem; padding: 3rem; background: #020617; margin-top: 2rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2.5rem;">
                    <h3 style="color: white; font-size: 1.5rem; font-weight: 700; margin: 0;">Included in every pathway</h3>
                    <div style="color: #64748b; font-weight: 700; font-family: monospace; font-size: 0.85rem; letter-spacing: 2px;">8 INCLUSIONS</div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">Live interactive virtual classrooms</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">24/7 access to recorded modules & notes</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">Adaptive CBT question bank engine</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">Mock examinations matching real patterns</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">Real-time weak-area performance analytics</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">1-on-1 mentorship with active airline pilots</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">DGCA Class 1 & 2 medical appointment guidance</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: #f43f5e; font-weight: bold; font-size: 1.2rem;">&#10003;</span>
                        <span style="color: #94a3b8; font-size: 1rem; font-weight: 300;">DGCA computer number processing support</span>
                    </div>
                </div>
            </div>
            
        </div>
        <!-- REGISTER PAGE -->"""

content = re.sub(old_courses_pattern, new_courses, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added Images and Razorpay Apply buttons back to the Courses page.")
