import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the journeyData object with the missing "pin" boxes
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
                    { id: "01", title: "Career discovery", desc: "An honest conversation about aptitude, temperament, circadian resilience and what the job is actually like day to day." },
                    { id: "02", title: "Eligibility & regulatory check", desc: "Age, education and the mandatory 10+2 Physics and Maths equivalence, verified before you commit any money." },
                    { id: "03", title: "Class 1 medical guidance", desc: "Step-by-step navigation of DGCA empanelled examiners and IAM/CME centres — the single most common point at which a plan collapses." },
                    { id: "04", title: "Costed operational roadmap", desc: "Licence pathway, timeline, aircraft hourly rates, overseas living costs and total budget written down, with no hidden surcharges." }
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
                    { id: "01", title: "Precision ground school", desc: "Live masterclasses across Air Navigation, Meteorology, Air Regulations and Technical General, with mental maths and scenario work throughout." },
                    { id: "02", title: "CBT & adaptive test series", desc: "Computer-based modules and question banks calibrated to real DGCA, FAA and EASA paper patterns — not memorisation shortcuts." },
                    { id: "03", title: "In-flight training abroad", desc: "Hour building with a partner flying organisation in the US, South Africa or Australia. The flying that turns theory into handling." },
                    { id: "04", title: "MCC & jet orientation", desc: "The transition from single-pilot habits to a two-crew flight deck: task sharing, swept-wing aerodynamics, FMS navigation and energy management." },
                    { id: "05", title: "SOP & checklist discipline", desc: "Callouts, cockpit flow patterns and non-normal profiles mirroring scheduled carrier standards, so type rating starts from a professional baseline." },
                    { id: "06", title: "Airline-style progress review", desc: "Graded the way airlines grade: standard achieved, improvement recommended, or further development required." }
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
                    { id: "01", title: "Airline readiness assessment", desc: "Technical knowledge, communication, mental maths and decision making scored against real airline selection criteria." },
                    { id: "02", title: "Selection & assessment centre prep", desc: "Technical and HR interviews, aptitude, numerical, verbal and spatial reasoning, group exercises and competency-based questions." },
                    { id: "03", title: "Simulator assessment preparation", desc: "Raw-data ILS hand flying, engine failure at V1, steep turns and single-engine go-arounds on flight training devices." },
                    { id: "04", title: "First officer development", desc: "Operational discipline, line-oriented thinking, CRM and threat & error management through the right-hand seat." },
                    { id: "05", title: "Command development", desc: "Leadership, crew management, risk and operational judgement — including diversion and fuel strategy under pressure." },
                    { id: "06", title: "Mentoring the next generation", desc: "Safety leadership on the flight deck, constructive feedback to junior first officers, and upholding institutional standards." }
                ]
            }
        };"""

pattern_data = r'const journeyData = \{.*?command: \{.*?\]\s*\}\s*\};'
content = re.sub(pattern_data, new_data, content, flags=re.DOTALL)


# Now update the HTML structure inside openJourneyModal to display these 4 pins
old_modal_func = """function openJourneyModal(type) {
            const data = journeyData[type];
            document.getElementById('modalTitle').innerText = data.title;
            document.getElementById('modalBg').style.backgroundImage = "url('" + data.img + "')";
            
            const modulesContainer = document.getElementById('modalModules');
            modulesContainer.innerHTML = '';
            
            data.modules.forEach(mod => {
                const div = document.createElement('div');
                div.style.background = 'rgba(255,255,255,0.02)';
                div.style.padding = '1.5rem';
                div.style.borderRadius = '0.5rem';
                div.style.borderLeft = '3px solid ' + data.color;
                div.innerHTML = '<div style="color: ' + data.color + '; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE ' + mod.id + '</div><h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;">' + mod.title + '</h4><p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;">' + mod.desc + '</p>';
                modulesContainer.appendChild(div);
            });
            
            const modal = document.getElementById('journeyModal');
            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }"""

new_modal_func = """function openJourneyModal(type) {
            const data = journeyData[type];
            document.getElementById('modalTitle').innerText = data.title;
            document.getElementById('modalBg').style.backgroundImage = "url('" + data.img + "')";
            
            const modulesContainer = document.getElementById('modalModules');
            
            // Build the 4 "Pin" Boxes (Duration, Enter With, Leave With, Gate)
            let topBoxesHtml = '<h3 style="color: white; font-size: 2rem; font-weight: 800; margin-bottom: 1.5rem;">' + data.subtitle + '</h3>';
            topBoxesHtml += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem;">';
            
            // Box 1: Duration
            topBoxesHtml += '<div style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #94A3B8; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">DURATION</div><div style="color: white; font-size: 1.1rem; font-weight: 600;">' + data.duration + '</div></div>';
            
            // Box 2: Enter With
            topBoxesHtml += '<div style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #94A3B8; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">YOU ENTER WITH</div><div style="color: white; font-size: 0.95rem;">' + data.enterWith + '</div></div>';
            
            // Box 3: Leave With
            topBoxesHtml += '<div style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #94A3B8; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">YOU LEAVE WITH</div><div style="color: white; font-size: 0.95rem;">' + data.leaveWith + '</div></div>';
            
            // Box 4: Gate
            topBoxesHtml += '<div style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #94A3B8; font-size: 0.7rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">GATE</div><div style="color: white; font-size: 0.95rem;">' + data.gate + '</div></div>';
            
            topBoxesHtml += '</div>';
            topBoxesHtml += '<div style="color: ' + data.color + '; font-size: 0.8rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">INSIDE THIS STAGE (' + data.modules.length + ' MODULES)</div>';
            topBoxesHtml += '<div id="modulesGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;"></div>';
            
            modulesContainer.innerHTML = topBoxesHtml;
            const gridContainer = document.getElementById('modulesGrid');
            
            data.modules.forEach(mod => {
                const div = document.createElement('div');
                div.style.background = 'rgba(255,255,255,0.02)';
                div.style.padding = '1.5rem';
                div.style.borderRadius = '0.5rem';
                div.style.borderLeft = '3px solid ' + data.color;
                div.innerHTML = '<div style="color: ' + data.color + '; font-size: 0.8rem; font-weight: 800; margin-bottom: 0.5rem;">MODULE ' + mod.id + '</div><h4 style="color: white; font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: 700;">' + mod.title + '</h4><p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin: 0;">' + mod.desc + '</p>';
                gridContainer.appendChild(div);
            });
            
            const modal = document.getElementById('journeyModal');
            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }"""

content = content.replace(old_modal_func, new_modal_func)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML logic with pins successfully.")
