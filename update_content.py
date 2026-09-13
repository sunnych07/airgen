import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_pages = '''
        <!-- ABOUT PAGE -->
        <div id="about" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1100px; margin: 0 auto;">
            <div class="glass-card" style="max-width: 1000px; text-align: left; padding: 3rem;">
                <div style="display: inline-block; padding: 0.4rem 1rem; border-radius: 2rem; background: rgba(56,189,248,0.1); color: #38BDF8; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; margin-bottom: 1rem;">ELEVATING AVIATION</div>
                <h2 style="font-size: 3rem; color: white; font-weight: 900; margin-bottom: 1.5rem; line-height: 1.2;">We Don't Just Train Pilots.<br><span style="color: #38BDF8;">We Forge Captains.</span></h2>
                <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.8; margin-bottom: 2.5rem; max-width: 800px;">
                    Inspired by the strict safety tolerances of European EASA standards and the dynamic environments of the FAA, AirGen Aviation delivers a world-class syllabus. We bridge the critical gap between initial cadet training and the right seat of a commercial airliner, ensuring our graduates are instantly airline-ready.
                </p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 200px; background: rgba(0,0,0,0.4); padding: 1.5rem; border-radius: 1rem; border-left: 4px solid #38BDF8; transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="font-size: 2.5rem; color: white; font-weight: 900;">100%</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; font-weight: 600; margin-top: 0.5rem;">DGCA Compliance</p>
                    </div>
                    <div style="flex: 1; min-width: 200px; background: rgba(0,0,0,0.4); padding: 1.5rem; border-radius: 1rem; border-left: 4px solid #E11D48; transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="font-size: 2.5rem; color: white; font-weight: 900;">210+</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; font-weight: 600; margin-top: 0.5rem;">Flight Hours</p>
                    </div>
                    <div style="flex: 1; min-width: 200px; background: rgba(0,0,0,0.4); padding: 1.5rem; border-radius: 1rem; border-left: 4px solid #FBBF24; transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <h3 style="font-size: 2.5rem; color: white; font-weight: 900;">G1000</h3>
                        <p style="color: #94A3B8; font-size: 0.95rem; font-weight: 600; margin-top: 0.5rem;">Glass-Cockpit Fleet</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- JOURNEY PAGE -->
        <div id="journey" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1100px; margin: 0 auto;">
            <h2 style="font-size: 2.5rem; color: white; font-weight: 900; text-align: center; margin-bottom: 2.5rem;">The <span style="color: #FBBF24;">18-Month</span> Flightpath</h2>
            <div style="display: flex; flex-direction: column; gap: 1.5rem; position: relative;">
                
                <div class="glass-card" style="max-width: 1000px; padding: 1.5rem 2.5rem; display: flex; align-items: center; gap: 2rem; transition: 0.3s;" onmouseover="this.style.borderColor='#38BDF8'" onmouseout="this.style.borderColor='rgba(56,189,248,0.2)'">
                    <div style="font-size: 3rem; font-weight: 900; color: rgba(56,189,248,0.2);">01</div>
                    <div>
                        <h3 style="font-size: 1.3rem; color: white; font-weight: 800; margin-bottom: 0.25rem;">Theoretical Knowledge (Ground School)</h3>
                        <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.75rem;">MONTH 1 - 4 &nbsp;|&nbsp; HYDERABAD HQ</p>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">Intensive DGCA exam preparation utilizing modern CBT (Computer Based Training) covering Air Navigation, Meteorology, Air Regulations, and Technical General.</p>
                    </div>
                </div>

                <div class="glass-card" style="max-width: 1000px; padding: 1.5rem 2.5rem; display: flex; align-items: center; gap: 2rem; transition: 0.3s;" onmouseover="this.style.borderColor='#38BDF8'" onmouseout="this.style.borderColor='rgba(56,189,248,0.2)'">
                    <div style="font-size: 3rem; font-weight: 900; color: rgba(56,189,248,0.2);">02</div>
                    <div>
                        <h3 style="font-size: 1.3rem; color: white; font-weight: 800; margin-bottom: 0.25rem;">Initial Flight Training (PPL & CPL)</h3>
                        <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.75rem;">MONTH 5 - 12 &nbsp;|&nbsp; USA / SOUTH AFRICA</p>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">Take to the skies in Cessna 172s equipped with Garmin G1000 avionics. Log 200+ hours mastering basic maneuvers, cross-country flights, and night operations.</p>
                    </div>
                </div>

                <div class="glass-card" style="max-width: 1000px; padding: 1.5rem 2.5rem; display: flex; align-items: center; gap: 2rem; transition: 0.3s;" onmouseover="this.style.borderColor='#38BDF8'" onmouseout="this.style.borderColor='rgba(56,189,248,0.2)'">
                    <div style="font-size: 3rem; font-weight: 900; color: rgba(56,189,248,0.2);">03</div>
                    <div>
                        <h3 style="font-size: 1.3rem; color: white; font-weight: 800; margin-bottom: 0.25rem;">Multi-Engine & Instrument Rating</h3>
                        <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.75rem;">MONTH 13 - 15 &nbsp;|&nbsp; ADVANCED FLEET</p>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">Learn to manage complex, multi-engine aircraft in zero-visibility conditions, preparing you for the rigorous demands of commercial airline operations.</p>
                    </div>
                </div>

                <div class="glass-card" style="max-width: 1000px; padding: 1.5rem 2.5rem; display: flex; align-items: center; gap: 2rem; transition: 0.3s;" onmouseover="this.style.borderColor='#10B981'" onmouseout="this.style.borderColor='rgba(56,189,248,0.2)'">
                    <div style="font-size: 3rem; font-weight: 900; color: rgba(16,185,129,0.2);">04</div>
                    <div>
                        <h3 style="font-size: 1.3rem; color: white; font-weight: 800; margin-bottom: 0.25rem;">APS MCC & Type Rating (A320/B737)</h3>
                        <p style="color: #10B981; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.75rem;">MONTH 16 - 18 &nbsp;|&nbsp; FULL FLIGHT SIMULATOR</p>
                        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">The final step. Transition from a cadet to a First Officer by mastering multi-crew cooperation and heavy jet operations in a Level-D Simulator.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- CADETS PAGE -->
        <div id="cadets" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1100px; margin: 0 auto; text-align: center;">
            <h2 style="font-size: 2.5rem; color: white; font-weight: 900; margin-bottom: 1rem;">Hall of <span style="color: #38BDF8;">Wings</span></h2>
            <p style="color: #94A3B8; font-size: 1.1rem; margin-bottom: 3rem; max-width: 700px; margin-left: auto; margin-right: auto;">Our legacy is measured by the success of our alumni. Over 80 AirGen graduates are currently flying active commercial lines globally.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
                <div class="glass-card" style="padding: 2rem; text-align: left;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                        <div style="width: 60px; height: 60px; border-radius: 50%; background: url('https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop') center/cover; border: 2px solid #38BDF8;"></div>
                        <span style="background: rgba(16,185,129,0.1); color: #10B981; padding: 0.3rem 0.8rem; border-radius: 1rem; font-size: 0.75rem; font-weight: 700;">INDIGO</span>
                    </div>
                    <h3 style="font-size: 1.25rem; color: white; font-weight: 800;">F.O. Rahul Sharma</h3>
                    <p style="color: #38BDF8; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">CLASS OF 2023 &nbsp;•&nbsp; A320</p>
                    <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; font-style: italic;">"AirGen's structured syllabus and modern fleet made my airline assessment a breeze. Highly recommended."</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem; text-align: left;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                        <div style="width: 60px; height: 60px; border-radius: 50%; background: url('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop') center/cover; border: 2px solid #E11D48;"></div>
                        <span style="background: rgba(225,29,72,0.1); color: #E11D48; padding: 0.3rem 0.8rem; border-radius: 1rem; font-size: 0.75rem; font-weight: 700;">AIR INDIA</span>
                    </div>
                    <h3 style="font-size: 1.25rem; color: white; font-weight: 800;">F.O. Ananya Patel</h3>
                    <p style="color: #E11D48; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">CLASS OF 2024 &nbsp;•&nbsp; B737</p>
                    <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; font-style: italic;">"From zero hours to the right seat of a Boeing 737. The instructors here truly care about your progression."</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem; text-align: left;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
                        <div style="width: 60px; height: 60px; border-radius: 50%; background: url('https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=200&auto=format&fit=crop') center/cover; border: 2px solid #FBBF24;"></div>
                        <span style="background: rgba(251,191,36,0.1); color: #FBBF24; padding: 0.3rem 0.8rem; border-radius: 1rem; font-size: 0.75rem; font-weight: 700;">AKASA AIR</span>
                    </div>
                    <h3 style="font-size: 1.25rem; color: white; font-weight: 800;">F.O. Vikram Singh</h3>
                    <p style="color: #FBBF24; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">CLASS OF 2023 &nbsp;•&nbsp; B737 MAX</p>
                    <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; font-style: italic;">"The simulator sessions and MCC prep were world-class. It gave me the edge I needed during hiring."</p>
                </div>
            </div>
        </div>

        <!-- FOUNDERS PAGE -->
        <div id="founders" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1100px; margin: 0 auto;">
            <div class="glass-card" style="max-width: 900px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 3rem; align-items: center; padding: 3rem;">
                <div style="flex: 1; min-width: 250px;">
                    <img src="https://images.unsplash.com/photo-1544717305-2782549b5136?q=80&w=400&auto=format&fit=crop" style="width: 100%; border-radius: 1rem; border: 4px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                </div>
                <div style="flex: 2; min-width: 300px; text-align: left;">
                    <div style="display: inline-block; padding: 0.4rem 1rem; border-radius: 2rem; background: rgba(225,29,72,0.1); color: #E11D48; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; margin-bottom: 1rem;">LEADERSHIP</div>
                    <h2 style="font-size: 2.5rem; color: white; font-weight: 900; margin-bottom: 0.5rem;">Captain Manas Teja</h2>
                    <p style="color: #38BDF8; font-size: 1rem; font-weight: 700; margin-bottom: 1.5rem; letter-spacing: 1px;">CHIEF INSTRUCTOR & FOUNDER</p>
                    <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
                        With over 15,000 flight hours across heavy jets and instructional aircraft, Capt. Teja founded AirGen with a singular vision: to eliminate the inefficiencies in modern flight training. 
                    </p>
                    <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.7;">
                        "We built the academy that we wished existed when we were starting out. Transparent pricing, strict safety protocols, and a direct pipeline to the airlines."
                    </p>
                </div>
            </div>
        </div>

        <!-- COURSES PAGE -->
        <div id="courses" class="page-section hidden-section fade-in" style="width: 100%; padding: 2rem; max-width: 1200px; margin: 0 auto; text-align: center;">
            <h2 style="font-size: 2.5rem; color: white; font-weight: 900; margin-bottom: 1rem;">Training <span style="color: #38BDF8;">Programs</span></h2>
            <p style="color: #94A3B8; font-size: 1.1rem; margin-bottom: 3rem; max-width: 600px; margin-left: auto; margin-right: auto;">Choose your pathway to the flight deck. Financing and scholarship options available for eligible candidates.</p>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem;">
                
                <div class="glass-card" style="flex: 1; min-width: 300px; max-width: 350px; padding: 2.5rem; display: flex; flex-direction: column;">
                    <h3 style="font-size: 1.5rem; color: white; font-weight: 800; margin-bottom: 1rem;">Ab-Initio CPL</h3>
                    <p style="color: #38BDF8; font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;">18 <span style="font-size: 1rem; color: #94A3B8; font-weight: 600;">Months</span></p>
                    <ul style="text-align: left; color: #cbd5e1; font-size: 0.95rem; line-height: 2; margin-bottom: 2rem; flex-grow: 1; list-style-type: none; padding: 0;">
                        <li>✓ DGCA Ground Classes</li>
                        <li>✓ 210 Hours Flight Training</li>
                        <li>✓ USA / RSA Accommodation</li>
                        <li>✓ Multi-Engine Rating</li>
                    </ul>
                    <button onclick="showPage('register')" class="btn-primary" style="background: transparent; border: 2px solid #38BDF8; color: #38BDF8;">Apply Now</button>
                </div>

                <div class="glass-card" style="flex: 1; min-width: 300px; max-width: 350px; padding: 2.5rem; display: flex; flex-direction: column; transform: scale(1.05); border-color: #FBBF24; box-shadow: 0 0 30px rgba(251,191,36,0.15); z-index: 10;">
                    <div style="background: #FBBF24; color: black; font-size: 0.75rem; font-weight: 800; padding: 0.3rem 1rem; border-radius: 20px; display: inline-block; margin: -4rem auto 2rem auto;">MOST POPULAR</div>
                    <h3 style="font-size: 1.5rem; color: white; font-weight: 800; margin-bottom: 1rem;">Zero to A320</h3>
                    <p style="color: #FBBF24; font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;">21 <span style="font-size: 1rem; color: #94A3B8; font-weight: 600;">Months</span></p>
                    <ul style="text-align: left; color: #cbd5e1; font-size: 0.95rem; line-height: 2; margin-bottom: 2rem; flex-grow: 1; list-style-type: none; padding: 0;">
                        <li>✓ Everything in Ab-Initio</li>
                        <li>✓ APS MCC Certification</li>
                        <li>✓ Airbus A320 Type Rating</li>
                        <li>✓ Airline Interview Prep</li>
                    </ul>
                    <button onclick="showPage('register')" class="btn-primary">Apply Now</button>
                </div>

                <div class="glass-card" style="flex: 1; min-width: 300px; max-width: 350px; padding: 2.5rem; display: flex; flex-direction: column;">
                    <h3 style="font-size: 1.5rem; color: white; font-weight: 800; margin-bottom: 1rem;">APS MCC Only</h3>
                    <p style="color: #10B981; font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;">3 <span style="font-size: 1rem; color: #94A3B8; font-weight: 600;">Weeks</span></p>
                    <ul style="text-align: left; color: #cbd5e1; font-size: 0.95rem; line-height: 2; margin-bottom: 2rem; flex-grow: 1; list-style-type: none; padding: 0;">
                        <li>✓ Multi-Crew Cooperation</li>
                        <li>✓ Jet Orientation Course</li>
                        <li>✓ B737/A320 Fixed Base Sim</li>
                        <li>✓ For Existing CPL Holders</li>
                    </ul>
                    <button onclick="showPage('register')" class="btn-primary" style="background: transparent; border: 2px solid #10B981; color: #10B981;">Apply Now</button>
                </div>

            </div>
        </div>
'''

# Find the placeholder section block to replace
start_marker = "<!-- ABOUT PAGE -->"
end_marker = "<!-- REGISTER PAGE -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_pages + "\n        " + content[end_idx:]
    with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Content replaced successfully.")
else:
    print("Could not find markers.")
