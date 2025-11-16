import os
import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class FloatWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("FloatWidget")
        
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set default position to top-right (screen_width - 400, 0)
        # 400 is the default widget width
        self.root.geometry(f"400x300+{screen_width - 400}+0")
        
        # Make window transparent and borderless
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-transparentcolor', 'black')  # Transparent background
        self.root.attributes('-topmost', False)  # NOT always on top by default
        
        # Main container with transparent background
        self.container = tk.Frame(root, bg='black')
        self.container.pack(fill="both", expand=True)

        # Image label without borders
        self.image_label = tk.Label(self.container, bg="black", bd=0, highlightthickness=0)
        self.image_label.pack(fill="both", expand=True)
        
        # Bind right-click for context menu
        self.image_label.bind("<Button-3>", self.show_context_menu)
        self.root.bind("<Button-3>", self.show_context_menu)

        # Default settings
        self.folder_path = ""
        self.images = []
        self.index = 0
        self.interval = 3000  # 3 seconds
        self.is_running = False
        self.is_topmost = False  # Track topmost state
        
        # Position variables
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Store screen dimensions for reset
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Bind mouse events for dragging
        self.root.bind("<Button-1>", self.start_drag)
        self.root.bind("<B1-Motion>", self.drag_window)
        
        # Show initial context menu
        self.show_initial_menu()

    def get_screen_center(self, window_width, window_height):
        """Calculate center position of screen"""
        x = (self.screen_width - window_width) // 2
        y = (self.screen_height - window_height) // 2
        
        return x, y

    def show_initial_menu(self):
        """Show initial context menu to select folder"""
        popup = tk.Toplevel(self.root)
        popup.title("FloatWidget - Getting Started")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.attributes('-topmost', True)  # Always on top
        
        # Center the popup on screen
        x, y = self.get_screen_center(300, 150)
        popup.geometry(f"300x150+{x}+{y}")
        
        tk.Label(popup, text="FloatWidget - Floating Image Viewer", 
                font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(popup, text="Right-click to access menu options").pack()
        
        tk.Button(popup, text="Select Image Folder", 
                 command=lambda: [self.pick_folder(), popup.destroy()]).pack(pady=5)
        tk.Button(popup, text="Exit", command=self.root.quit).pack(pady=5)

    def show_context_menu(self, event):
        """Right-click context menu"""
        menu = tk.Menu(self.root, tearoff=0)
        
        menu.add_command(label="📁 Select Image Folder", command=self.pick_folder)
        menu.add_command(label="⏱️  Set Time Interval", command=self.set_interval)
        
        if self.is_running:
            menu.add_command(label="⏸️  Pause", command=self.pause_slideshow)
        else:
            menu.add_command(label="▶️  Play", command=self.play_slideshow)
        
        menu.add_command(label="↻ Shuffle Images", command=self.shuffle_images)
        menu.add_separator()
        menu.add_command(label="↔️  Window Size", command=self.set_window_size)
        menu.add_command(label="🔄 Reset Position", command=self.reset_position)
        menu.add_separator()
        
        # Toggle topmost status
        topmost_label = "📌 Always on Top (ON)" if self.is_topmost else "📌 Always on Top (OFF)"
        menu.add_command(label=topmost_label, command=self.toggle_topmost)
        
        menu.add_separator()
        menu.add_command(label="❌ Exit", command=self.root.quit)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def toggle_topmost(self):
        """Toggle always-on-top mode"""
        self.is_topmost = not self.is_topmost
        self.root.attributes('-topmost', self.is_topmost)
        status = "ON" if self.is_topmost else "OFF"
        print(f"Always on Top: {status}")

    def pick_folder(self):
        """Select folder with images"""
        self.folder_path = filedialog.askdirectory()
        if not self.folder_path:
            return

        valid_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")
        self.images = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if f.lower().endswith(valid_ext)
        ]

        if not self.images:
            print("No valid image files found in folder.")
            return

        random.shuffle(self.images)
        self.index = 0
        self.is_running = True
        self.show_image()

    def show_image(self):
        """Display current image"""
        if not self.images or not self.is_running:
            return

        img_path = self.images[self.index]
        
        try:
            img = Image.open(img_path)

            # Get current widget size
            w = max(100, self.image_label.winfo_width())
            h = max(100, self.image_label.winfo_height())

            # Resize with modern Pillow resampling
            img = img.resize((w, h), Image.Resampling.LANCZOS)

            # Convert to Tkinter-compatible image
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)

            # Move to next image
            self.index = (self.index + 1) % len(self.images)

            # Loop with the set interval
            self.root.after(self.interval, self.show_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.index = (self.index + 1) % len(self.images)
            self.root.after(self.interval, self.show_image)

    def set_interval(self):
        """Set time interval between images"""
        popup = tk.Toplevel(self.root)
        popup.title("Set Interval")
        popup.geometry("250x120")
        popup.resizable(False, False)
        popup.attributes('-topmost', True)  # Always on top
        
        # Center the popup on screen
        x, y = self.get_screen_center(250, 120)
        popup.geometry(f"250x120+{x}+{y}")

        tk.Label(popup, text="Seconds per image:").pack(pady=5)
        entry = tk.Entry(popup, width=10)
        entry.insert(0, str(self.interval // 1000))
        entry.pack()

        def save_interval():
            try:
                value = int(entry.get())
                if value > 0:
                    self.interval = value * 1000
                popup.destroy()
            except ValueError:
                pass

        tk.Button(popup, text="Save", command=save_interval).pack(pady=5)

    def pause_slideshow(self):
        """Pause image rotation"""
        self.is_running = False

    def play_slideshow(self):
        """Resume image rotation"""
        if self.images:
            self.is_running = True
            self.show_image()

    def shuffle_images(self):
        """Shuffle image order"""
        if self.images:
            random.shuffle(self.images)
            self.index = 0
            print("Images shuffled!")

    def set_window_size(self):
        """Set custom window size"""
        popup = tk.Toplevel(self.root)
        popup.title("Window Size")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.attributes('-topmost', True)  # Always on top
        
        # Center the popup on screen
        x, y = self.get_screen_center(300, 150)
        popup.geometry(f"300x150+{x}+{y}")

        tk.Label(popup, text="Width (px):").pack(pady=5)
        width_entry = tk.Entry(popup, width=10)
        width_entry.insert(0, str(self.root.winfo_width()))
        width_entry.pack()

        tk.Label(popup, text="Height (px):").pack(pady=5)
        height_entry = tk.Entry(popup, width=10)
        height_entry.insert(0, str(self.root.winfo_height()))
        height_entry.pack()

        def save_size():
            try:
                w = int(width_entry.get())
                h = int(height_entry.get())
                self.root.geometry(f"{w}x{h}")
                popup.destroy()
            except ValueError:
                pass

        tk.Button(popup, text="Apply", command=save_size).pack(pady=5)

    def reset_position(self):
        """Reset window to top-right"""
        self.root.geometry(f"400x300+{self.screen_width - 400}+0")

    def start_drag(self, event):
        """Start window drag"""
        self.drag_start_x = event.x_root - self.root.winfo_x()
        self.drag_start_y = event.y_root - self.root.winfo_y()

    def drag_window(self, event):
        """Drag window around screen"""
        x = event.x_root - self.drag_start_x
        y = event.y_root - self.drag_start_y
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FloatWidget(root)
    root.mainloop()
