import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old modal HTML base structure
old_modal_html_pattern = r'<div id="journeyModal".*?<div id="modalModules".*?</div>\s*</div>\s*</div>'
new_modal_html = '<div id="journeyModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); backdrop-filter: blur(10px); z-index: 9999; overflow-y: auto; padding: 2rem;"></div>'
content = re.sub(old_modal_html_pattern, new_modal_html, content, flags=re.DOTALL)


# Replace the openJourneyModal function
old_js_pattern = r'function openJourneyModal\(type\).*?function closeJourneyModal\(\)'

new_js = """function openJourneyModal(type) {
            const data = journeyData[type];
            const modal = document.getElementById('journeyModal');
            
            let descText = "";
            let num = "";
            if(type === 'think') { descText = "Before a single rupee is spent, we establish whether aviation is the right career for you — and if it is, exactly what your route looks like, costed and dated."; num = "01"; }
            else if(type === 'train') { descText = "Ground school, flight hours and the jet transition. Every subject runs through the ASK framework so theory becomes cockpit capability rather than exam recall."; num = "02"; }
            else { descText = "The stage most academies skip entirely. Airline selection, the right-hand seat, and then the leadership and judgement a command upgrade is actually assessed on."; num = "03"; }

            modal.innerHTML = '<div style="position: absolute; top: 2rem; right: 2rem; z-index: 10;"><button onclick="closeJourneyModal()" style="background: rgba(255,255,255,0.1); border: none; color: white; font-size: 1.5rem; width: 40px; height: 40px; border-radius: 50%; cursor: pointer;">×</button></div>' +
            '<div style="max-width: 800px; margin: 0 auto; background: #050505; border: 1px solid #222; border-radius: 1rem; overflow: hidden; padding: 3rem; text-align: left;">' +
                '<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; border-bottom: 1px solid #222; padding-bottom: 1.5rem;">' +
                    '<div style="border: 1px solid ' + data.color + '; color: ' + data.color + '; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 900;">' + num + '</div>' +
                    '<div style="color: white; font-weight: 800; letter-spacing: 2px; font-size: 0.9rem;">' + data.title.toUpperCase() + '</div>' +
                '</div>' +
                '<h2 style="color: white; font-size: 2.8rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: -1px;">' + data.subtitle + '</h2>' +
                '<p style="color: #888; font-size: 1.05rem; line-height: 1.6; margin-bottom: 3rem; max-width: 650px;">' + descText + '</p>' +
                
                '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 4rem;">' +
                    '<div style="border: 1px solid #222; border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #555; font-size: 0.65rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">DURATION</div><div style="color: #ddd; font-size: 0.95rem; font-weight: 600;">' + data.duration + '</div></div>' +
                    '<div style="border: 1px solid #222; border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #555; font-size: 0.65rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">YOU ENTER WITH</div><div style="color: #ddd; font-size: 0.95rem; line-height: 1.4;">' + data.enterWith + '</div></div>' +
                    '<div style="border: 1px solid #222; border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #555; font-size: 0.65rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">YOU LEAVE WITH</div><div style="color: #ddd; font-size: 0.95rem; line-height: 1.4;">' + data.leaveWith + '</div></div>' +
                    '<div style="border: 1px solid #222; border-radius: 0.5rem; padding: 1.5rem;"><div style="color: #555; font-size: 0.65rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.5rem;">GATE</div><div style="color: #ddd; font-size: 0.95rem; line-height: 1.4;">' + data.gate + '</div></div>' +
                '</div>' +

                '<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #222; padding-bottom: 1rem; margin-bottom: 1rem;">' +
                    '<div style="color: #555; font-weight: 800; letter-spacing: 2px; font-size: 0.75rem;">INSIDE THIS STAGE</div>' +
                    '<div style="color: ' + data.color + '; font-weight: 800; letter-spacing: 1px; font-size: 0.75rem;">' + data.modules.length + ' MODULES</div>' +
                '</div>' +

                '<div id="flowchartModules" style="display: flex; flex-direction: column;"></div>' +
                
                '<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #222;">' +
                    '<div onclick="toggleChat(); closeJourneyModal();" style="color: white; font-weight: 800; letter-spacing: 2px; font-size: 0.85rem; cursor: pointer; display: flex; justify-content: space-between;">' +
                        '<span>ASK ABOUT ' + data.title.toUpperCase() + '</span><span>↗</span>' +
                    '</div>' +
                '</div>' +
            '</div>';

            const flowchart = document.getElementById('flowchartModules');
            data.modules.forEach(mod => {
                const row = document.createElement('div');
                row.style.display = 'flex';
                row.style.gap = '2rem';
                row.style.padding = '1.5rem 0';
                row.style.borderBottom = '1px solid #1a1a1a';
                row.innerHTML = '<div style="color: ' + data.color + '; font-weight: 800; font-family: monospace; font-size: 0.9rem; padding-top: 0.2rem;">' + mod.id + '</div>' +
                                '<div><h4 style="color: white; font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">' + mod.title + '</h4>' +
                                '<p style="color: #777; font-size: 0.9rem; line-height: 1.6; margin: 0; max-width: 600px;">' + mod.desc + '</p></div>';
                flowchart.appendChild(row);
            });

            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }

        function closeJourneyModal()"""

content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Modal to match Flowchart style.")
