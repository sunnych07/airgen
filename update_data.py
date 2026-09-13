import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the journeyData object with the exact text from the images
new_data = """const journeyData = {
            think: {
                title: "Thinking Stage",
                img: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200",
                color: "#E11D48",
                modules: [
                    { id: "01", title: "Career discovery", desc: "An honest conversation about aptitude, temperament, circadian resilience and what the job is actually like day to day." },
                    { id: "02", title: "Eligibility & regulatory check", desc: "Age, education and the mandatory 10+2 Physics and Maths equivalence, verified before you commit any money." },
                    { id: "03", title: "Class 1 medical guidance", desc: "Step-by-step navigation of DGCA empanelled examiners and IAM/CME centres — the single most common point at which a plan collapses." },
                    { id: "04", title: "Costed operational roadmap", desc: "Licence pathway, timeline, aircraft hourly rates, overseas living costs and total budget written down, with no hidden surcharges." }
                ]
            },
            train: {
                title: "Training Stage",
                img: "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1200",
                color: "#38BDF8",
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
                img: "https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=1200",
                color: "#10B981",
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

# Regex to replace the old journeyData
pattern = r'const journeyData = \{.*?command: \{.*?\]\s*\}\s*\};'
content = re.sub(pattern, new_data, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated JS data successfully.")
