import os
import subprocess
from dotenv import load_dotenv

def convert_all_ui_files():
    load_dotenv()
    ui_directory =  os.getenv('FILE_DIR') # Укажите путь к директории с .ui файлами
    for root, dirs, files in os.walk(ui_directory):
        for file in files:
            if file.endswith('.ui'):
                ui_file = os.path.join(root, file)
                py_file = os.path.join(root, file.replace('.ui', '_ui.py'))
                command = f"pyside6-uic {ui_file} -o {py_file}"
                subprocess.run(command, shell=True)
                print(f"Converted {ui_file} to {py_file}")

def convert_all_qrs_files():
    load_dotenv()
    ui_directory =  os.getenv('FILE_DIR') # Укажите путь к директории с .ui файлами
    for root, dirs, files in os.walk(ui_directory):
        for file in files:
            if file.endswith('.qrc'):
                ui_file = os.path.join(root, file)
                py_file = os.path.join(root, file.replace('.qrc', '_rc.py'))
                command = f"pyside6-rcc {ui_file} -o {py_file}"
                subprocess.run(command, shell=True)
                print(f"Converted {ui_file} to {py_file}")

if __name__ == "__main__":
    convert_all_ui_files()
    convert_all_qrs_files()