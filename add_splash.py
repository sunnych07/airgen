import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

splash_html = """
    <!-- INTRO SPLASH SCREEN -->
    <div id="introSplash" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 99999999; display: flex; justify-content: center; align-items: center; transition: opacity 1s ease-in-out;">
        <video id="introVideo" src="intro.mp4" autoplay muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
        <button onclick="closeSplash()" style="position: absolute; bottom: 40px; right: 40px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.8rem 2rem; border-radius: 3rem; font-weight: 800; letter-spacing: 2px; font-size: 0.8rem; cursor: pointer; backdrop-filter: blur(5px); z-index: 10;">SKIP INTRO ↗</button>
    </div>

    <script>
        function closeSplash() {
            const splash = document.getElementById('introSplash');
            if (splash) {
                splash.style.opacity = '0';
                setTimeout(() => { splash.style.display = 'none'; }, 1000);
            }
        }
        
        document.addEventListener('DOMContentLoaded', () => {
            const video = document.getElementById('introVideo');
            if(video) {
                video.addEventListener('ended', closeSplash);
                // Hard fallback just in case browser blocks autoplay
                setTimeout(closeSplash, 12000);
            }
        });
    </script>
"""

content = content.replace('<body>', '<body>\n' + splash_html)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added intro splash screen.")
