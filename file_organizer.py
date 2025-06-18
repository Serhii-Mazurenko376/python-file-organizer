import os
import shutil

# 📁 1. Set the path to the main folder (adjust as needed for your system)
folder_path = os.path.join(os.path.expanduser('file_organizer'))

# 📦 2. Define file types you want to organize (add more if needed)
file_types = ['txt', 'text', 'pdf', 'jpg', 'jpeg']

# 🗂️ 3. Create folders for each file type (if not already there)
for file_type in file_types:
    folder_name = os.path.join(folder_path, file_type.upper())
    os.makedirs(folder_name, exist_ok=True)

# 🔁 4. Loop through all items in the main folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # 🚫 Skip folders and hidden/system files
    if os.path.isdir(file_path) or filename.startswith('.'):
        continue

    # 🔍 Get the file extension
    ext = filename.split('.')[-1].lower()

    # ✅ Move the file if the extension matches
    if ext in file_types:
        target_folder = os.path.join(folder_path, ext.upper())
        new_path = os.path.join(target_folder, filename)
        shutil.move(file_path, new_path)
        print(f"Moved: {filename} → {ext.upper()}/")
