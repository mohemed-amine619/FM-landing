import os
import glob

components_dir = os.path.join(os.path.dirname(__file__), "src", "components")
vue_files = glob.glob(os.path.join(components_dir, "*.vue"))

for file_path in vue_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Speed up GSAP durations
    content = content.replace("duration: 1.2", "duration: 0.5")
    content = content.replace("duration: 1,", "duration: 0.4,")
    content = content.replace("duration: 0.8", "duration: 0.4")
    content = content.replace("duration: 1.5", "duration: 0.6")
    content = content.replace("stagger: 0.2", "stagger: 0.05")
    content = content.replace("stagger: 0.1", "stagger: 0.05")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done speeding up GSAP animations!")
