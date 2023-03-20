import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk
import cv2

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengolahan Citra")
        self.root.geometry("800x600")

        self.image_path = None
        self.original_image = None
        self.processed_image = None

        self.label_box = tk.LabelFrame(root, text='Creator', padx=5, pady=5)
        self.label_box.place(x=210, y=520, width=400, height=70)
        self.info_label = tk.Label(self.root, text="Dibuat oleh: Melsy Patricia Anggelina. E  NIM: F55121026  Kelas: A")
        self.info_label.place(x=230, y=550)

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        self.original_label = tk.Label(self.image_frame)
        self.original_label.grid(row=0, column=0, padx=10)

        self.processed_label = tk.Label(self.image_frame)
        self.processed_label.grid(row=0, column=1, padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.open_button = tk.Button(self.button_frame, text="Buka Gambar", command=self.open_image)
        self.open_button.grid(row=0, column=0, padx=10)

        self.sharpen_button = tk.Button(self.button_frame, text="Sharpening", command=self.sharpen_image, state=tk.DISABLED)
        self.sharpen_button.grid(row=0, column=1, padx=10)

        self.binarize_button = tk.Button(self.button_frame, text="Citra Biner", command=self.binarize_image, state=tk.DISABLED)
        self.binarize_button.grid(row=0, column=2, padx=10)

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.image_path)
        self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)

        self.display_image(self.original_label, self.original_image)

        self.sharpen_button.config(state=tk.NORMAL)
        self.binarize_button.config(state=tk.NORMAL)

    def sharpen_image(self):
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        self.processed_image = cv2.filter2D(self.original_image, -1, kernel)

        self.display_image(self.processed_label, self.processed_image)

    def binarize_image(self):
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        self.processed_image = cv2.cvtColor(threshold_image, cv2.COLOR_GRAY2RGB)

        self.display_image(self.processed_label, self.processed_image)

    def display_image(self, label, image):
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        label.config(image=image)
        label.image = image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
