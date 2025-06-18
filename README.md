# 🗂️ Python File Organizer Script

Automatically organizes files into folders based on their file types — built using Python and runs perfectly even on iOS with Pythonista 3!

---

## ✨ Features

- 📁 Creates folders for each file type
- 📦 Moves files into matching folders (e.g. `.txt` → `TXT/`)
- 🔒 Ignores folders and hidden system files
- 📱 Works on iPhone/iPad (Pythonista 3) or desktop

---

## 🔧 How It Works

1. Set the main folder path
2. Define the file extensions you want to organize
3. Script scans the folder
4. Files are moved into subfolders like `PDF/`, `JPG/`, `TXT/`

---

## 📂 Example Folder Structure

Before running:
<code>
```plaintext
file_organizer/
├── test.txt
├── notes.pdf
├── photo.jpeg
```
</code>

After running:
<code>
```plaintext
file_organizer/
├── TXT/
│   └── test.txt
├── PDF/
│   └── notes.pdf
├── JPEG/
│   └── photo.jpeg
```
</code>
---

## 🚀 Getting Started

### ✅ Requirements
- Python 3
- (Optional) [Pythonista 3](https://omz-software.com/pythonista/) on iOS

### ▶️ Run the Script

```bash
python file_organizer.py
```

### Or tap ▶️ in Pythonista.

---

## ⚙️ Configuration

Update this list to add more file types:
```
file_types = ['txt', 'pdf', 'jpeg', 'jpg']
```
## 🙌 Author

**Serhii Mazurenko**

📍 Sweden | 👨‍💻 Python beginner, automation enthusiast

[🔗 LinkedIn](https://www.linkedin.com/in/serhii-mazurenko-1361245f)  
[💼 GitHub](https://github.com/Serhii-Mazurenko376)

---

## 🏗️ Future Ideas
	- Group similar extensions together (e.g. .jpg, .jpeg)
	- Custom folder names (like Documents/, Images/)
	- GUI version using Tkinter or Kivy
