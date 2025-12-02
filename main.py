from itertools import cycle 
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow Viewer")

# List of images path
image_paths = [
    r"C:\Users\SIMRAN\OneDrive\Projects\Image Slideshow App\Images\image 1.jpg",
    r"C:\Users\SIMRAN\OneDrive\Projects\Image Slideshow App\Images\image 2.jpg",
    r"C:\Users\SIMRAN\OneDrive\Projects\Image Slideshow App\Images\image 3.jpg",
    r"C:\Users\SIMRAN\OneDrive\Projects\Image Slideshow App\Images\image 4.webp",
]

# Resize the image to 1080x1080
image_size =(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

# Label
label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for i in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()



