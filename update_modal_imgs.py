import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update journeyData to include images for every single module
new_data = """const journeyData = {
            think: {
                title: "Thinking Stage",
                subtitle: "Should I become a pilot?",
                img: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200",
                color: "#E11D48",
                duration: "2-6 weeks",
                enterWith: "No prior aviation experience required (10+2 with Physics & Maths)",
                leaveWith: "A costed roadmap with real dates and a DGCA computer number",
                gate: "Class 1 Medical + DGCA Computer Number",
                modules: [
                    { id: "01", title: "Career discovery", desc: "An honest conversation about aptitude, temperament, circadian resilience and what the job is actually like day to day.", modImg: "https://images.unsplash.com/photo-1573164713988-8665fc963095?q=80&w=400&auto=format&fit=crop" },
                    { id: "02", title: "Eligibility & regulatory check", desc: "Age, education and the mandatory 10+2 Physics and Maths equivalence, verified before you commit any money.", modImg: "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=400&auto=format&fit=crop" },
                    { id: "03", title: "Class 1 medical guidance", desc: "Step-by-step navigation of DGCA empanelled examiners and IAM/CME centres — the single most common point at which a plan collapses.", modImg: "https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=400&auto=format&fit=crop" },
                    { id: "04", title: "Costed operational roadmap", desc: "Licence pathway, timeline, aircraft hourly rates, overseas living costs and total budget written down, with no hidden surcharges.", modImg: "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?q=80&w=400&auto=format&fit=crop" }
                ]
            },
            train: {
                title: "Training Stage",
                subtitle: "How do I become competent?",
                img: "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200",
                color: "#38BDF8",
                duration: "12-18 months",
                enterWith: "Class 1 medical and DGCA computer number in hand",
                leaveWith: "CPL with multi-engine instrument rating, 200+ logged hours, MCC and JOC complete",
                gate: "Theory papers cleared + CPL issued + MCC/JOC pass",
                modules: [
                    { id: "01", title: "Precision ground school", desc: "Live masterclasses across Air Navigation, Meteorology, Air Regulations and Technical General, with mental maths and scenario work throughout.", modImg: "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?q=80&w=400&auto=format&fit=crop" },
                    { id: "02", title: "CBT & adaptive test series", desc: "Computer-based modules and question banks calibrated to real DGCA, FAA and EASA paper patterns — not memorisation shortcuts.", modImg: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=400&auto=format&fit=crop" },
                    { id: "03", title: "In-flight training abroad", desc: "Hour building with a partner flying organisation in the US, South Africa or Australia. The flying that turns theory into handling.", modImg: "https://images.unsplash.com/photo-1529154691717-3306083d869e?q=80&w=400&auto=format&fit=crop" },
                    { id: "04", title: "MCC & jet orientation", desc: "The transition from single-pilot habits to a two-crew flight deck: task sharing, swept-wing aerodynamics, FMS navigation and energy management.", modImg: "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=400&auto=format&fit=crop" },
                    { id: "05", title: "SOP & checklist discipline", desc: "Callouts, cockpit flow patterns and non-normal profiles mirroring scheduled carrier standards, so type rating starts from a professional baseline.", modImg: "https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=400&auto=format&fit=crop" },
                    { id: "06", title: "Airline-style progress review", desc: "Graded the way airlines grade: standard achieved, improvement recommended, or further development required.", modImg: "https://images.unsplash.com/photo-1588600878108-578307a3cc9d?q=80&w=400&auto=format&fit=crop" }
                ]
            },
            command: {
                title: "Command & Job",
                subtitle: "How do I become a captain?",
                img: "https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=1200",
                color: "#10B981",
                duration: "Career-long",
                enterWith: "CPL holder preparing for a cadet or first officer vacancy",
                leaveWith: "A line job, and a route to the left seat",
                gate: "Airline command upgrade board & ATPL viva",
                modules: [
                    { id: "01", title: "Airline readiness assessment", desc: "Technical knowledge, communication, mental maths and decision making scored against real airline selection criteria.", modImg: "https://images.unsplash.com/photo-1569154941061-e231b4725ef1?q=80&w=400&auto=format&fit=crop" },
                    { id: "02", title: "Selection & assessment centre prep", desc: "Technical and HR interviews, aptitude, numerical, verbal and spatial reasoning, group exercises and competency-based questions.", modImg: "https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?q=80&w=400&auto=format&fit=crop" },
                    { id: "03", title: "Simulator assessment preparation", desc: "Raw-data ILS hand flying, engine failure at V1, steep turns and single-engine go-arounds on flight training devices.", modImg: "https://images.unsplash.com/photo-1610884639947-f311c81ef432?q=80&w=400&auto=format&fit=crop" },
                    { id: "04", title: "First officer development", desc: "Operational discipline, line-oriented thinking, CRM and threat & error management through the right-hand seat.", modImg: "https://images.unsplash.com/photo-1601758252277-2e11e3b2e775?q=80&w=400&auto=format&fit=crop" },
                    { id: "05", title: "Command development", desc: "Leadership, crew management, risk and operational judgement — including diversion and fuel strategy under pressure.", modImg: "https://images.unsplash.com/photo-1583344605174-8b5e902b37bd?q=80&w=400&auto=format&fit=crop" },
                    { id: "06", title: "Mentoring the next generation", desc: "Safety leadership on the flight deck, constructive feedback to junior first officers, and upholding institutional standards.", modImg: "https://images.unsplash.com/photo-1559685084-28b9fb635e14?q=80&w=400&auto=format&fit=crop" }
                ]
            }
        };"""

pattern_data = r'const journeyData = \{.*?command: \{.*?\]\s*\}\s*\};'
content = re.sub(pattern_data, new_data, content, flags=re.DOTALL)


# 2. Update the JS rendering logic to include these images in the DOM
old_js_pattern = r'function openJourneyModal\(type\).*?function closeJourneyModal\(\)'

new_js = """function openJourneyModal(type) {
            const data = journeyData[type];
            const modal = document.getElementById('journeyModal');
            
            let descText = "";
            let num = "";
            if(type === 'think') { descText = "Before a single rupee is spent, we establish whether aviation is the right career for you — and if it is, exactly what your route looks like, costed and dated."; num = "1"; }
            else if(type === 'train') { descText = "Ground school, flight hours and the jet transition. Every subject runs through the ASK framework so theory becomes cockpit capability rather than exam recall."; num = "2"; }
            else { descText = "The stage most academies skip entirely. Airline selection, the right-hand seat, and then the leadership and judgement a command upgrade is actually assessed on."; num = "3"; }

            modal.innerHTML = `
            <div style="position: absolute; top: 2rem; right: 2rem; z-index: 10;">
                <button onclick="closeJourneyModal()" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: white; font-size: 1.5rem; width: 45px; height: 45px; border-radius: 50%; cursor: pointer; backdrop-filter: blur(5px); transition: 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">×</button>
            </div>
            <div style="max-width: 900px; margin: 2rem auto; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); border-radius: 1.5rem; overflow: hidden; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8);">
                
                <!-- Glow Effect -->
                <div style="position: absolute; top: -100px; left: -100px; width: 300px; height: 300px; background: ${data.color}; filter: blur(150px); opacity: 0.15; z-index: 0; pointer-events: none;"></div>

                <div style="padding: 4rem; position: relative; z-index: 1;">
                    
                    <!-- Premium Badge -->
                    <div style="display: inline-flex; align-items: center; gap: 0.8rem; padding: 0.5rem 1rem 0.5rem 0.5rem; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 2rem; margin-bottom: 2rem;">
                        <div style="background: ${data.color}; color: #000; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 900;">${num}</div>
                        <div style="color: white; font-weight: 800; letter-spacing: 2px; font-size: 0.8rem;">${data.title.toUpperCase()}</div>
                    </div>
                    
                    <!-- Huge Crisp Title -->
                    <h2 style="color: white; font-size: 3.5rem; font-weight: 900; margin-bottom: 1.5rem; letter-spacing: -1.5px; line-height: 1.1;">${data.subtitle}</h2>
                    <p style="color: #94A3B8; font-size: 1.15rem; line-height: 1.7; margin-bottom: 4rem; max-width: 700px; font-weight: 300;">${descText}</p>
                    
                    <!-- 4 Pins (With Icons) -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 5rem;">
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.2rem;">⏱️</span> DURATION</div>
                            <div style="color: white; font-size: 1.2rem; font-weight: 700;">${data.duration}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.2rem;">🎓</span> YOU ENTER WITH</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.enterWith}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.2rem;">✈️</span> YOU LEAVE WITH</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.leaveWith}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.2rem;">🔒</span> GATE</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.gate}</div>
                        </div>
                    </div>

                    <!-- Section Header -->
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1.5rem; margin-bottom: 2rem;">
                        <div style="color: #64748B; font-weight: 800; letter-spacing: 2px; font-size: 0.85rem;">INSIDE THIS STAGE</div>
                        <div style="background: ${data.color}22; color: ${data.color}; padding: 0.4rem 1.2rem; border-radius: 2rem; font-weight: 800; letter-spacing: 1.5px; font-size: 0.75rem;">${data.modules.length} MODULES</div>
                    </div>

                    <!-- Visual Modules with High-End Images -->
                    <div id="flowchartModules" style="display: flex; flex-direction: column; gap: 1.5rem;"></div>
                    
                    <!-- Action Footer -->
                    <div style="margin-top: 4rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 3rem;">
                        <button onclick="toggleChat(); closeJourneyModal();" style="background: ${data.color}; color: #000; border: none; padding: 1.2rem 3.5rem; border-radius: 3rem; font-weight: 800; font-size: 1.1rem; letter-spacing: 1.5px; cursor: pointer; transition: 0.3s; box-shadow: 0 10px 25px ${data.color}44;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 35px ${data.color}66'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 25px ${data.color}44'">
                            ASK ABOUT ${data.title.toUpperCase()} ↗
                        </button>
                    </div>
                </div>
            </div>`;

            const flowchart = document.getElementById('flowchartModules');
            data.modules.forEach(mod => {
                const row = document.createElement('div');
                row.style.display = 'flex';
                row.style.alignItems = 'center'; // Center align the image and text
                row.style.gap = '2rem';
                row.style.padding = '1.5rem';
                row.style.background = 'rgba(255,255,255,0.02)';
                row.style.borderRadius = '1rem';
                row.style.border = '1px solid rgba(255,255,255,0.05)';
                row.style.transition = 'all 0.3s ease';
                row.onmouseover = function() { this.style.background = 'rgba(255,255,255,0.05)'; this.style.transform = 'translateX(10px)'; this.style.borderColor = 'rgba(255,255,255,0.1)'; };
                row.onmouseout = function() { this.style.background = 'rgba(255,255,255,0.02)'; this.style.transform = 'translateX(0)'; this.style.borderColor = 'rgba(255,255,255,0.05)'; };
                
                row.innerHTML = `
                    <div style="position: relative; width: 120px; height: 120px; flex-shrink: 0; border-radius: 0.8rem; overflow: hidden; border: 2px solid ${data.color}44;">
                        <div style="position: absolute; top: 0; left: 0; background: rgba(0,0,0,0.4); width: 100%; height: 100%; z-index: 1;"></div>
                        <img src="${mod.modImg}" style="width: 100%; height: 100%; object-fit: cover; z-index: 0; position: relative;">
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 2; color: white; font-weight: 900; font-family: monospace; font-size: 2rem; text-shadow: 0 5px 15px rgba(0,0,0,0.9);">${mod.id}</div>
                    </div>
                    <div>
                        <h4 style="color: white; font-size: 1.3rem; font-weight: 800; margin-bottom: 0.5rem; letter-spacing: -0.5px;">${mod.title}</h4>
                        <p style="color: #94A3B8; font-size: 1rem; line-height: 1.6; margin: 0; font-weight: 300;">${mod.desc}</p>
                    </div>
                `;
                flowchart.appendChild(row);
            });
            
            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }

        function closeJourneyModal()"""

content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added gorgeous images to the modal list!")
