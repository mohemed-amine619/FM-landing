import os
import glob

components_dir = "/home/mohamed.bougrioua@beyn.dz/Bureau/my-project/fm-landing/src/components"
vue_files = glob.glob(os.path.join(components_dir, "*.vue"))

for file_path in vue_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Revert to premium silky durations (not too fast, not too slow)
    content = content.replace("duration: 0.4", "duration: 0.8")
    content = content.replace("duration: 0.5", "duration: 1.0")
    content = content.replace("duration: 0.6", "duration: 1.2")
    content = content.replace("stagger: 0.05,", "stagger: 0.15,")
    content = content.replace("stagger: 0.055,", "stagger: 0.15,")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Restored silky smooth GSAP animations!")
