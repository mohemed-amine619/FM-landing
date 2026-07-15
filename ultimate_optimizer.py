import os
import glob
import re

components_dir = os.path.join(os.path.dirname(__file__), "src", "components")
vue_files = glob.glob(os.path.join(components_dir, "*.vue"))

# Also include style.css if needed, though we already cleaned it mostly
css_file = os.path.join(os.path.dirname(__file__), "src", "style.css")
all_files = vue_files + [css_file]

for file_path in all_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Remove all backdrop filters (backdrop-blur-sm, md, lg, xl)
    content = re.sub(r'\bbackdrop-blur-(sm|md|lg|xl|2xl|3xl)\b', '', content)
    
    # 2. Replace blur-2xl and blur-3xl with solid fallbacks or radial gradients
    # For ContactForm.vue (blur-3xl)
    if "ContactForm.vue" in file_path:
        content = content.replace("blur-3xl", "")
        content = content.replace("animate-pulse-glow", "")
        
    # For ServicesSection.vue (blur-2xl)
    if "ServicesSection.vue" in file_path:
        content = content.replace("blur-2xl", "")
        
    # 3. For WhyChooseUs.vue: remove backdrop-blur from section
    if "WhyChooseUs.vue" in file_path:
        content = content.replace("backdrop-blur-sm", "")
        
    # 4. Remove heavy text shadows and box shadows if they are causing lag
    # We will leave simple shadows but remove massive ones on hover
    
    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Ultimate performance optimizations applied!")
