import tkinter as tk
from PIL import Image, ImageTk  # pip install pillow

IMAGE_PATH = "jumbojosh.jpeg"  # Replace with your image file

def trigger_prank():
    prank_window = tk.Toplevel(root)
    prank_window.attributes("-fullscreen", True)
    prank_window.overrideredirect(True)
    prank_window.config(bg="black")

    # Load image
    img = Image.open(IMAGE_PATH)
    screen_width = prank_window.winfo_screenwidth()
    screen_height = prank_window.winfo_screenheight()
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    prank_img = ImageTk.PhotoImage(img)

    label = tk.Label(prank_window, image=prank_img)
    label.image = prank_img
    label.pack()

    # ESC and Ctrl+Q to exit
    prank_window.bind("<Escape>", lambda e: prank_window.destroy())
    prank_window.bind("<Control-q>", lambda e: prank_window.destroy())

    # Force focus (important for Raspberry Pi)
    prank_window.focus_force()

# Main app
root = tk.Tk()
root.geometry("400x200")
root.title("Payment")

button = tk.Button(
    root, text="Pay $100 to <name>",
    font=("Arial", 20, "bold"), fg="white", bg="red",
    command=trigger_prank
)
button.pack(expand=True)

# Root escape safety too
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

