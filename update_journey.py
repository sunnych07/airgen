import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_journey = '''
        <!-- JOURNEY PAGE -->
        <div id="journey" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1200px; margin: 0 auto; text-align: center;">
            <div style="display: inline-block; padding: 0.4rem 1rem; border-radius: 2rem; background: rgba(225,29,72,0.1); color: #E11D48; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 1rem;" data-aos="fade-down">ROADMAP</div>
            <h2 style="font-size: 3rem; color: white; font-weight: 900; margin-bottom: 3rem;" data-aos="fade-down" data-aos-delay="100">The Flightpath</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                
                <!-- Box 1: Thinking Stage -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="200" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(225,29,72,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #E11D48; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">01</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 1rem; line-height: 1.1;">Thinking<br>Stage</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">Career discovery, medical guidance, and cost planning. We establish if aviation is exactly right for you before a single rupee is spent.</p>
                    </div>
                </div>

                <!-- Box 2: Training Stage -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="400" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(56,189,248,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #38BDF8; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">02</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 1rem; line-height: 1.1;">Training<br>Stage</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">DGCA ground school, CBT modules, and 200+ hours of international flight training to transform aerodynamic theory into precise handling.</p>
                    </div>
                </div>

                <!-- Box 3: Job Stage -->
                <div class="glass-card" data-aos="fade-up" data-aos-delay="600" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(16,185,129,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #10B981; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">03</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 1rem; line-height: 1.1;">Command<br>& Job</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">Type rating, airline readiness assessment, and multi-crew cooperation. We prepare you for the right-hand seat of a commercial jet.</p>
                    </div>
                </div>
                
            </div>
        </div>
'''

start_marker = "<!-- JOURNEY PAGE -->"
end_marker = "<!-- CADETS PAGE -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_journey + "\n        " + content[end_idx:]
    with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Journey section replaced successfully.")
else:
    print("Could not find markers.")
