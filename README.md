# FloatWidget 🎬
A lightweight, transparent floating image viewer for Windows. Perfect for displaying images as a desktop widget with automatic cycling through folders. Wanted for motivational images.

---

## ✨ Features

### 🪟 Transparent & Borderless  
Clean floating design that blends beautifully with your desktop.

### 🖱️ Draggable Window  
Click and drag anywhere to move the widget.

### ▶️⏸️ Play / Pause Slideshow  
Full control over automatic image cycling.

### 🔀 Shuffle Mode  
Randomize image order instantly.

### ⚙️ Customizable  
- Set interval between images  
- Adjust window size  
- Position anywhere on screen  

### 📌 Always-on-Top Toggle  
Switch between floating and regular window mode.

### 🧭 Right-Click Menu  
All options accessible via a simple context menu.

### 🖼️ Supports Multiple Image Formats  
JPG, PNG, GIF, BMP, WebP.

### ↖️ Top-Right Default Position  
Starts neatly docked to the top-right corner.

---

## 🚀 Quick Start

### For Non-Technical Windows Users
1. Download **FloatWidget.exe** from the **Releases** page  
2. Double-click to run  
3. Choose an image folder  
4. Enjoy your floating slideshow! 🎉

---

## 👨‍💻 For Developers

### Requirements
- Python 3.7+
- Pillow (PIL)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/FloatWidget.git
cd FloatWidget

# Install dependencies
pip install -r requirements.txt

# Run FloatWidget
python FloatWidget.py
```
---

## 📖 Usage
Start the App
```bash
python FloatWidget.py
```

### Right-Click Menu Options

| Option | Description |
|--------|-------------|
| 📁 **Select Image Folder** | Choose the folder to display images from |
| ⏱️ **Set Time Interval** | Change the time (in seconds) between image transitions |
| ▶️ **Play** / ⏸️ **Pause** | Start or stop the slideshow |
| ↻ **Shuffle Images** | Randomize the order of displayed images |
| ↔️ **Window Size** | Resize the floating widget window |
| 🔄 **Reset Position** | Move the window back to the top-right corner |
| 📌 **Always on Top** | Toggle whether the widget stays above other windows |
| ❌ **Exit** | Close FloatWidget |


### 🖱️ Mouse Controls
- **Click & Drag** – Move the window anywhere on your screen  
- **Right-Click** – Open the context menu  

---

## 🖼️ Supported Image Formats
- **JPG / JPEG**  
- **PNG**  
- **GIF**  
- **BMP**  
- **WebP**

---

## 💻 System Requirements

### **For .EXE Version**
- Windows 10/11 (64-bit)  
- ~30MB free space  
- No Python needed  

### **For Python Version**
- Windows 10/11  
- Python 3.7+  
- ~50MB free space  

---

## 🛠️ Installation from Source

### **Step 1: Install Python**
Download from: https://www.python.org/downloads/  
✔ Make sure to enable **“Add Python to PATH”**

### **Step 2: Clone the Repository**
```bash
git clone https://github.com/yourusername/FloatWidget.git
cd FloatWidget
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Run FloatWidget**
```bash
python FloatWidget.py
```

---

## 🔨 Building Your Own .EXE

# Install PyInstaller
pip install pyinstaller

# Build .exe (from FloatWidget directory)
pyinstaller --onefile --windowed FloatWidget.py

# Find your .exe in the 'dist' folder
# You can now share this .exe with anyone - no Python required!

---

## ⚙️ Configuration

FloatWidget stores all settings in memory. Preferences reset when you close and reopen the application.

**Default Settings:**
- Image cycle interval: 3 seconds
- Window size: 400x300 pixels
- Starting position: Top-right corner
- Always-on-top: OFF

To change defaults, edit these values in `FloatWidget.py`:
```bash
self.interval = 3000  # milliseconds
# Change window size in geometry: 400x300
```

---


## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError: No module named 'PIL'" | Run: `pip install pillow` |
| "No valid image files found" | Ensure folder contains .jpg, .png, .gif, .bmp, or .webp files |
| Window not transparent | Only works on Windows. Try restarting the app |
| Can't drag window | Click directly on the image area to drag |
| Popups appearing off-screen | They should be centered. Try closing and reopening |

## 🎨 Use Cases

- **Content Creators** - Preview reference images while working
- **Designers** - Keep design mockups visible during development
- **Photographers** - Display photo collections as desktop art
- **Students** - Study with floating note images or diagrams
- **Productivity** - Use as a persistent reminder or inspiration widget

## 🔧 Tech Stack

- **Language:** Python 3.7+
- **GUI Framework:** Tkinter (built-in with Python)
- **Image Processing:** Pillow (PIL)
- **Build Tool:** PyInstaller (for .EXE creation)

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

This means you're free to use, modify, and distribute FloatWidget!

## 🤝 Contributing

Found a bug? Have a feature request? Contributions are welcome!
PR with description is the key!

## ⭐ Show Your Support

If FloatWidget is useful to you, please:
- ⭐ Star this repository
- 🔗 Share it with others
- 💬 Leave feedback

## 🎯 Roadmap

Potential future features:
- [ ] Image preview hover tooltip
- [ ] Keyboard shortcuts (Alt+P for pause, etc.)
- [ ] Remember last folder location
- [ ] Custom hotkeys
- [ ] Video support
- [ ] Mac/Linux support

---

**Made with ❤️ for simplicity. Built for productivity. Designed for you.**

Enjoy FloatWidget! 🎉
