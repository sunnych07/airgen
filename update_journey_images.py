import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Journey grid entirely to use explicit <img> tags instead of background overlays.
old_journey_pattern = r'<div id="journey".*?<!-- COURSES PAGE -->'

new_journey = """<div id="journey" class="page-section hidden-section fade-in" style="width: 100%; padding: 4rem 2rem; max-width: 1300px; margin: 0 auto; text-align: center;">
            <div style="margin-bottom: 4rem;">
                <h2 style="font-size: 3rem; color: white; font-weight: 900; margin-bottom: 1rem;" data-aos="fade-down">The <span style="color: #10B981;">Journey</span></h2>
                <p style="color: #94A3B8; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">A structured three-stage pipeline taking you from discovery to the left seat.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                
                <!-- Box 1: Ground School -->
                <div onclick="openJourneyModal('think')" data-aos="fade-up" data-aos-delay="200" style="border-radius: 0.8rem; border: 1px solid rgba(225,29,72,0.3); background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s; cursor: pointer; text-align: left;" onmouseover="this.style.borderColor='#E11D48'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(225,29,72,0.3)'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(225,29,72,0.3);">
                    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="color: #E11D48; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">01</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Ground<br>School</h3>
                        <p style="color: #E11D48; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 4 MODULES &#8599;</p>
                    </div>
                </div>

                <!-- Box 2: Training Stage -->
                <div onclick="openJourneyModal('train')" data-aos="fade-up" data-aos-delay="400" style="border-radius: 0.8rem; border: 1px solid rgba(56,189,248,0.3); background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s; cursor: pointer; text-align: left;" onmouseover="this.style.borderColor='#38BDF8'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(56,189,248,0.3)'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(56,189,248,0.3);">
                    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="color: #38BDF8; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">02</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Training<br>Stage</h3>
                        <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 6 MODULES &#8599;</p>
                    </div>
                </div>

                <!-- Box 3: Job Stage -->
                <div onclick="openJourneyModal('command')" data-aos="fade-up" data-aos-delay="600" style="border-radius: 0.8rem; border: 1px solid rgba(16,185,129,0.3); background: #020617; display: flex; flex-direction: column; overflow: hidden; transition: 0.3s; cursor: pointer; text-align: left;" onmouseover="this.style.borderColor='#10B981'; this.style.transform='translateY(-5px)'" onmouseout="this.style.borderColor='rgba(16,185,129,0.3)'; this.style.transform='translateY(0)'">
                    <img src="https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=600&auto=format&fit=crop" style="width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(16,185,129,0.3);">
                    <div style="padding: 2.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="color: #10B981; font-weight: 900; font-size: 1.5rem; margin-bottom: 0.5rem; font-family: monospace;">03</div>
                        <h3 style="font-size: 2.2rem; color: white; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1;">Command<br>& Job</h3>
                        <p style="color: #10B981; font-size: 0.85rem; font-weight: 700; margin-top: 1rem;">CLICK TO VIEW 6 MODULES &#8599;</p>
                    </div>
                </div>
                
            </div>
        </div>
        <!-- COURSES PAGE -->"""

content = re.sub(old_journey_pattern, new_journey, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Journey cards to use explicit img tags.")
