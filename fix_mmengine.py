import os
import sys
import site

# Find the path where mmengine is installed
def find_mmengine_path():
    for site_package in site.getsitepackages() + [site.getusersitepackages()]:
        mmengine_path = os.path.join(site_package, "mmengine", "registry", "registry.py")

        if os.path.exists(mmengine_path):
            return mmengine_path
    return None

# Patch the registry.py file
def patch_registry(file_path):
    
    with open("./fix_mmengine.py", "r") as f:
        content = f.read()

    with open(file_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    mmengine_file = find_mmengine_path()
    
    if mmengine_file:
        patch_registry(mmengine_file)
    else:
        sys.exit(1)
