import os
import glob

components_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "components")
vue_files = glob.glob(os.path.join(components_dir, "*.vue"))

for file_path in vue_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Make everything ultra smooth and slow
    content = content.replace("duration: 0.8", "duration: 1.5")
    content = content.replace("duration: 1.0", "duration: 2.0")
    content = content.replace("duration: 1.2", "duration: 2.5")
    content = content.replace("stagger: 0.15,", "stagger: 0.3,")
    content = content.replace("stagger: 0.15", "stagger: 0.3")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Applied ULTRA SILKY SMOOTH GSAP animations!")
