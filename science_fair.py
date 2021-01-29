# C3BO: Cancer Blood Oncologist

import tkinter as tk  # GUI for project
# from tkinter import Frame, Canvas
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image
import numpy as np
# import tensorflow as tf
# from tensorflow import keras
import glob  # Accessing cancer files
from time import sleep

root = tk.Tk()  # Initializing class
root.title("Moe, Larry, or Curly?")
root.geometry("2000x2000")
# root.wm_attributes('-alpha', 0.7)

classes = {
    0: "It's Moe!",
    1: "It's Larry!",
    2: "It's Curly!",
    3: "It's Shemp!"
}

class GUI:

    def __init__(self, master, WIDTH=300, HEIGHT=300):
        self.master = master
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.DEFAULTCOLOR = "#f25f55"  #"#f25f55"

        self.result = None

        self.bg = tk.Label(master, bg=self.DEFAULTCOLOR)
        self.bg.place(relwidth=1, relheight=1)
        self.showRobot()

        self.uploadImgButton = tk.Button(master, text="upload image",
                                         bg="#f0b8b4", activebackground="#d4a29f", command=self.uploadImage)
        self.uploadImgButton.pack(side=tk.BOTTOM, pady=50)
        # Label to see image uploaded by user
        self.sign_image = tk.Label(master, bg=self.DEFAULTCOLOR)
        self.sign_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.classifyImg = tk.Button(master, text="classify image",
                                  bg="#f0b8b4", command=self.classifyImage)
        self.classifyImg.place(relx=0.79,rely=0.46)
        self.clfLabel = tk.Label(self.master, bg=self.DEFAULTCOLOR, text="")
        self.clfLabel.pack(side=tk.LEFT, anchor="nw", pady=250)

    def uploadImage(self):
        Image_Width = 200
        Image_Height = 200
        Image_Size = (Image_Width, Image_Height)
        
        # "dataverse_files/MiMM_SBILab Dataset/"
        # file_path = filedialog.askopenfilename()
        file_path = "dataverse_files/MiMM_SBILab Dataset/"
        
        def iterateThroughFile():
            index = np.random.randint(1, 5)
            path2files = glob.glob(file_path+"*.bmp")
            uploaded = Image.open(path2files[index])
            uploaded.thumbnail(Image_Size)
            im = ImageTk.PhotoImage(uploaded)
            self.sign_image.configure(image=im)
            self.sign_image.image = im
            self.master.after(100, iterateThroughFile)
            
        iterateThroughFile()

    def showRobot(self):
        robImgLabel = tk.Label(root, bg=self.DEFAULTCOLOR)
        robImgLabel.pack(side=tk.LEFT, anchor="s", pady=100)

        uploaded = Image.open("C3BO.png")
        uploaded = uploaded.resize((261, 320))
        robImg = ImageTk.PhotoImage(uploaded)
        robImgLabel.configure(image=robImg)
        robImgLabel.image = robImg

    def classifyImage(self):
        self.clfLabel.config(text=" I think this is pizza ", font=("Rockwell Condensed", 20),
                             bg="#d9cb96", fg="#6e5907")

gui = GUI(root)
tk.mainloop()