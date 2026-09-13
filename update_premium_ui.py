import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

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
                    
                    <!-- 4 Pins (Glass Cards) -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 5rem;">
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem; transition: 0.3s; cursor: default;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%)'">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem;">DURATION</div>
                            <div style="color: white; font-size: 1.2rem; font-weight: 700;">${data.duration}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem; transition: 0.3s; cursor: default;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%)'">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem;">YOU ENTER WITH</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.enterWith}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem; transition: 0.3s; cursor: default;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%)'">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem;">YOU LEAVE WITH</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.leaveWith}</div>
                        </div>
                        <div style="background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%); border: 1px solid rgba(255,255,255,0.05); border-top: 3px solid ${data.color}; border-radius: 1rem; padding: 2rem; transition: 0.3s; cursor: default;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%)'">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.8rem;">GATE</div>
                            <div style="color: white; font-size: 1.05rem; line-height: 1.5;">${data.gate}</div>
                        </div>
                    </div>

                    <!-- Section Header -->
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1.5rem; margin-bottom: 2rem;">
                        <div style="color: #64748B; font-weight: 800; letter-spacing: 2px; font-size: 0.85rem;">INSIDE THIS STAGE</div>
                        <div style="background: ${data.color}22; color: ${data.color}; padding: 0.4rem 1.2rem; border-radius: 2rem; font-weight: 800; letter-spacing: 1.5px; font-size: 0.75rem;">${data.modules.length} MODULES</div>
                    </div>

                    <!-- Sleek Flowchart Timeline -->
                    <div id="flowchartModules" style="display: flex; flex-direction: column; gap: 1rem;"></div>
                    
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
                row.style.gap = '2rem';
                row.style.padding = '2rem';
                row.style.background = 'rgba(255,255,255,0.015)';
                row.style.borderRadius = '1rem';
                row.style.border = '1px solid rgba(255,255,255,0.03)';
                row.style.transition = 'all 0.3s ease';
                row.onmouseover = function() { this.style.background = 'rgba(255,255,255,0.04)'; this.style.transform = 'translateX(10px)'; this.style.borderColor = 'rgba(255,255,255,0.1)'; };
                row.onmouseout = function() { this.style.background = 'rgba(255,255,255,0.015)'; this.style.transform = 'translateX(0)'; this.style.borderColor = 'rgba(255,255,255,0.03)'; };
                
                row.innerHTML = `
                    <div style="color: ${data.color}; font-weight: 900; font-family: monospace; font-size: 1.8rem; opacity: 0.9; margin-top: -0.2rem;">${mod.id}</div>
                    <div>
                        <h4 style="color: white; font-size: 1.3rem; font-weight: 800; margin-bottom: 0.8rem; letter-spacing: -0.5px;">${mod.title}</h4>
                        <p style="color: #94A3B8; font-size: 1.05rem; line-height: 1.7; margin: 0; font-weight: 300;">${mod.desc}</p>
                    </div>
                `;
                flowchart.appendChild(row);
            });
            
            modal.style.display = 'block';
            setTimeout(() => modal.style.opacity = '1', 10);
        }

        function closeJourneyModal()"""

content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

# Ensure the modal wrapper has flexbox centering
old_wrapper = '<div id="journeyModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); backdrop-filter: blur(10px); z-index: 9999; overflow-y: auto; padding: 2rem;"></div>'
new_wrapper = '<div id="journeyModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(3, 7, 18, 0.85); backdrop-filter: blur(20px); z-index: 9999; overflow-y: auto; padding: 2rem;"></div>'
content = content.replace(old_wrapper, new_wrapper)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Modal to ultra-premium design.")
