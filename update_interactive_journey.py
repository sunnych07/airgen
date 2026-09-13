import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Journey Cards to have onclick events
old_journey = content[content.find('<!-- Box 1'):content.find('<!-- CADETS PAGE -->')]
new_journey_boxes = '''<!-- Box 1: Thinking Stage -->
                <div onclick="openJourneyModal('think')" class="glass-card" data-aos="fade-up" data-aos-delay="200" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(225,29,72,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #E11D48; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">01</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Thinking<br>Stage</h3>
                        <p style="color: #E11D48; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 4 MODULES ↗</p>
                    </div>
                </div>

                <!-- Box 2: Training Stage -->
                <div onclick="openJourneyModal('train')" class="glass-card" data-aos="fade-up" data-aos-delay="400" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(56,189,248,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #38BDF8; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">02</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Training<br>Stage</h3>
                        <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 6 MODULES ↗</p>
                    </div>
                </div>

                <!-- Box 3: Job Stage -->
                <div onclick="openJourneyModal('command')" class="glass-card" data-aos="fade-up" data-aos-delay="600" style="position: relative; overflow: hidden; padding: 0; min-height: 450px; display: flex; flex-direction: column; justify-content: flex-end; text-align: left; border: 1px solid rgba(16,185,129,0.3); cursor: pointer;" onmouseover="this.children[0].style.transform='scale(1.1)'; this.children[0].style.opacity='0.7'" onmouseout="this.children[0].style.transform='scale(1)'; this.children[0].style.opacity='0.4'">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=600&auto=format&fit=crop') center/cover; opacity: 0.4; z-index: 0; transition: transform 0.8s ease, opacity 0.5s ease;"></div>
                    <div style="position: relative; z-index: 1; background: linear-gradient(to top, rgba(3,7,18,1) 10%, rgba(3,7,18,0.4) 70%, transparent 100%); padding: 2.5rem; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
                        <div style="color: #10B981; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">03</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Command<br>& Job</h3>
                        <p style="color: #10B981; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 6 MODULES ↗</p>
                    </div>
                </div>
                
            </div>
        </div>
'''
content = content.replace(old_journey, new_journey_boxes)

# 2. Add Modal HTML just before </body>
modal_html = '''
    <!-- JOURNEY MODAL -->
    <div id="journeyModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(3,7,18,0.9); backdrop-filter: blur(10px); z-index: 9999; overflow-y: auto; padding: 2rem;">
        <div style="max-width: 900px; margin: 2rem auto; background: #0f172a; border-radius: 1rem; border: 1px solid rgba(255,255,255,0.1); overflow: hidden; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);">
            <button onclick="closeJourneyModal()" style="position: absolute; top: 1.5rem; right: 1.5rem; background: rgba(0,0,0,0.5); border: none; color: white; font-size: 1.5rem; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; z-index: 10;">×</button>
            <div id="modalHeader" style="height: 200px; background: #333; position: relative;">
                <div id="modalBg" style="position: absolute; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0.5;"></div>
                <div style="position: absolute; bottom: 1.5rem; left: 2rem; z-index: 1;">
                    <h2 id="modalTitle" style="font-size: 2.5rem; color: white; font-weight: 900; margin: 0;">Title</h2>
                </div>
            </div>
            <div style="padding: 2rem;">
                <div id="modalModules" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <!-- Modules injected here -->
                </div>
            </div>
        </div>
    </div>
    
    <script>
        const journeyData = {
            think: {
                title: "Thinking Stage",
                img: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200",
                color: "#E11D48",
                modules: [
                    { id: "01", title: "Career Discovery", desc: "Aptitude, temperament, and circadian resilience assessment." },
                    { id: "02", title: "Eligibility Check", desc: "Mandatory 10+2 Physics and Maths equivalence verification." },
                    { id: "03", title: "Class 1 Medical", desc: "Step-by-step navigation of DGCA empanelled medical examiners." },
                    { id: "04", title: "Costed Roadmap", desc: "Licence pathway, timeline, and total budget with zero hidden surcharges." }
                ]
            },
            train: {
                title: "Training Stage",
                img: "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200",
                color: "#38BDF8",
                modules: [
                    { id: "01", title: "Precision Ground School", desc: "Masterclasses in Air Navigation, Meteorology, and Regulations." },
                    { id: "02", title: "CBT & Adaptive Tests", desc: "Question banks calibrated to real DGCA and FAA patterns." },
                    { id: "03", title: "In-Flight Training", desc: "200+ hours of international flight training in modern glass-cockpits." },
                    { id: "04", title: "MCC & Jet Orientation", desc: "Transitioning from single-pilot habits to a two-crew flight deck." },
                    { id: "05", title: "SOP Discipline", desc: "Callouts, cockpit flows, and non-normal profiles mirroring airlines." },
                    { id: "06", title: "Progress Review", desc: "Graded exactly the way commercial airlines grade their pilots." }
                ]
            },
            command: {
                title: "Command & Job",
                img: "https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=1200",
                color: "#10B981",
                modules: [
                    { id: "01", title: "Airline Readiness", desc: "Technical knowledge, mental maths, and decision making scored." },
                    { id: "02", title: "Assessment Prep", desc: "HR interviews, numerical reasoning, and group exercises." },
                    { id: "03", title: "Simulator Assessment", desc: "Raw-data ILS hand flying and engine failure prep on training devices." },
                    { id: "04", title: "First Officer Development", desc: "Operational discipline, CRM, and threat management." },
                    { id: "05", title: "Command Development", desc: "Leadership, crew management, and operational judgement." },
                    { id: "06", title: "Mentoring", desc: "Safety leadership on the flight deck and upholding standards." }
                ]
            }
        };

        function openJourneyModal(type) {
            const data = journeyData[type];
            document.getElementById('modalTitle').innerText = data.title;
            document.getElementById('modalBg').style.backgroundImage = url('');
            
            const modulesContainer = document.getElementById('modalModules');
            modulesContainer.innerHTML = '';
            
            data.modules.forEach(mod => {
                const div = document.createElement('div');
                div.style.background = 'rgba(255,255,255,0.02)';
                div.style.padding = '1.5rem';
                div.style.borderRadius = '0.5rem';
                div.style.borderLeft = 3px solid ;
                div.innerHTML = 
                    <div style="color: ; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE </div>
                    <h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;"></h4>
                    <p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;"></p>
                ;
                modulesContainer.appendChild(div);
            });
            
            const modal = document.getElementById('journeyModal');
            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }

        function closeJourneyModal() {
            document.getElementById('journeyModal').style.display = 'none';
        }
    </script>
</body>
'''
content = content.replace('</body>', modal_html)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
