# FloatWidget
FloatWidget - A lightweight, transparent floating image viewer for Windows.  Draggable widget with right-click menu controls. Two options: Python code  or ready-to-use .EXE. No bloat, just beautiful floating images. Wanted it for motivational images.


# ✨ Features
🪟 Transparent & Borderless

Clean floating design that blends beautifully with your desktop.

🖱️ Draggable Window

Click and drag anywhere to move the widget.

▶️⏸️ Play / Pause Slideshow

Full control over automatic image cycling.

🔀 Shuffle Mode

Randomize image order instantly.

⚙️ Customizable

Set interval between images

Adjust window size

Position anywhere on screen

📌 Always-on-Top Toggle

Switch between floating and regular window mode.

🧭 Right-Click Menu

All options accessible via a simple context menu.

🖼️ Supports Multiple Image Formats

JPG, PNG, GIF, BMP, WebP.

↖️ Top-Right Default Position

Starts neatly docked to the top-right corner.

🚀 Quick Start
For Non-Technical Windows Users

Download FloatWidget.exe from the Releases page

Double-click to run

Choose an image folder

Enjoy your floating slideshow! 🎉

👨‍💻 For Developers
Requirements

Python 3.7+

Pillow (PIL)

Installation
# Clone the repository
git clone https://github.com/yourusername/FloatWidget.git
cd FloatWidget

# Install dependencies
pip install -r requirements.txt

# Run FloatWidget
python FloatWidget.py

📖 Usage
Starting FloatWidget:

bash
python FloatWidget.py
Right-Click Menu Options:

Option	Description
📁 Select Image Folder	Choose which folder to display images from
⏱️ Set Time Interval	Change seconds between image changes (default: 3s)
▶️ Play / ⏸️ Pause	Start or stop the slideshow
↻ Shuffle Images	Randomize the image order
↔️ Window Size	Resize the floating window
🔄 Reset Position	Move window back to top-right
📌 Always on Top	Toggle whether widget stays above other windows
❌ Exit	Close FloatWidget
Mouse Controls:

Click & Drag - Move the window anywhere on your screen

Right-Click - Show context menu

🖼️ Supported Image Formats
JPG / JPEG

PNG

GIF

BMP

WebP

💻 System Requirements
For .EXE Version:

Windows 10/11 (64-bit)

~30MB free space

No additional installation needed

For Python Version:

Windows 10/11

Python 3.7+

~50MB free space

🛠️ Installation from Source
Step 1: Install Python
Download from https://www.python.org/downloads/

✅ Check "Add Python to PATH" during installation

Step 2: Clone Repository
bash
git clone https://github.com/yourusername/FloatWidget.git
cd FloatWidget
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Run FloatWidget
bash
python FloatWidget.py
🔨 Building Your Own .EXE
Want to create a standalone executable?

bash
# Install PyInstaller
pip install pyinstaller

# Build .exe (from FloatWidget directory)
pyinstaller --onefile --windowed FloatWidget.py

# Find your .exe in the 'dist' folder
# You can now share this .exe with anyone - no Python required!
