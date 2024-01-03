import shutil
import os
import sys

def copy_submodule(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    shutil.copytree(source_dir, destination_dir)
    print("Submodule copied to destination.")

def override_resources(theme_override_dir, output_to_dir):
    source_override_dir = theme_override_dir
    destination_override_dir = output_to_dir
    for item in os.listdir(source_override_dir):
        s = os.path.join(source_override_dir, item)
        d = os.path.join(destination_override_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("Resources overridden.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine_theme_resources.py <source_dir_path> <override_from_dir_path> <output_dir_path>")
        sys.exit(1)
    source_dir_path = sys.argv[1]
    overridefrom_dir_path = sys.argv[2]
    output_dir_path = sys.argv[3]
    copy_submodule(source_dir_path,output_dir_path)
    override_resources(overridefrom_dir_path, output_dir_path)
