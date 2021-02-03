# C3BO: Cancer Blood Oncologist

# GUI imports
import tkinter as tk
from tkinter import Frame, Canvas
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image

# Data science imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Machine Learning/Deep Learning imports
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # So the dlerror does not appear
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
from sklearn.model_selection import train_test_split

# Extra imports
import glob  # To access cancer files

root = tk.Tk()  # Initializing class
root.title("C3BO: Cancer Blood Oncologist")
root.geometry("2000x2000")

greetingC3BO = "Hello there! I am C3BO\n"
greetingC3BO += "Using Convolutional Neural Networks, my brilliant\n creator Leonardo Amatoregis de Farias\n"
greetingC3BO += "trained me to predict blood cancer"

phrasesC3BO = [
    "Is that a nice hat you've got?",
    "Wonderful weather we are having is it not?",
    "Did you know that I am fluent in over six million forms of communication",
    "I enjoy listening to the sound of rain",
    "Do you know what a sigmoid function is?",
    "Water and metal mix rather curiously..."
]

hasCancer = {
    0: "No",
    1: "Yes"   
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
        # self.exitProgram()

        self.uploadImgButton = tk.Button(master, text="upload image",
                                         bg="#f0b8b4", activebackground="#d4a29f", command=self.uploadImage)
        self.uploadImgButton.pack(side=tk.BOTTOM, pady=50)
        # Label to see image uploaded by user
        self.sign_image = tk.Label(master, bg=self.DEFAULTCOLOR)
        self.sign_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.classifyImg = tk.Button(master, text="classify image",
                                  bg="#f0b8b4", command=self.classifyImage)
        self.classifyImg.place(relx=0.79,rely=0.46)
        self.clfLabel = tk.Label(self.master, font=("Rockwell Condensed", 20),
                                 text=greetingC3BO, bg="#d9cb96", fg="#6e5907")
        self.clfLabel.pack(side=tk.LEFT, anchor="nw", pady=200)
        
        self.mainClasses = ["does not have blood cancer", "has blood cancer"]
        
        file_path = "dataverse_files/MiMM_SBILab Dataset/"
        path2files = glob.glob(file_path+"*.bmp")
        self.cancerData = path2files  # Initializing data

    def uploadImage(self):
        Image_Width = 200
        Image_Height = 200
        Image_Size = (Image_Width, Image_Height)
        
        # "dataverse_files/MiMM_SBILab Dataset/"
        file_path = filedialog.askopenfilename()
        
        file_path = "dataverse_files/MiMM_SBILab Dataset/"
        path2files = glob.glob(file_path+"*.bmp")
        self.cancerData = path2files
        
        def iterateThroughFile():
            try:
                randIndex = np.random.randint(0, len(file_path)-1)
                uploaded = Image.open(path2files[randIndex])
                uploaded.thumbnail(Image_Size)
                im = ImageTk.PhotoImage(uploaded)
                self.sign_image.configure(image=im)
                self.sign_image.image = im
            except Exception as e:
                print(e)
            self.master.after(25, iterateThroughFile)
            
        def verboseC3BO():
            self.clfLabel.config(text=np.random.choice(phrasesC3BO))  
            self.master.after(3000, verboseC3BO)
            
        iterateThroughFile()
        verboseC3BO()

    def showRobot(self):
        robImgLabel = tk.Label(root, bg=self.DEFAULTCOLOR)
        robImgLabel.pack(side=tk.LEFT, anchor="s", pady=100)

        uploaded = Image.open("C3BO.png")
        uploaded = uploaded.resize((261, 320))
        robImg = ImageTk.PhotoImage(uploaded)
        robImgLabel.configure(image=robImg)
        robImgLabel.image = robImg
        
    def exitProgram(self):
        exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy) 
        exit_button.pack()
    
    def classifyImage(self):
        self.clfLabel.config(text=" I think this is pizza ")
        self.prepareData()
        
    def prepareData(self):
        X = []
        y = []

        for i in range(len(self.cancerData)):
            currentImgToArr = mpimg.imread(self.cancerData[i])
            X.append(currentImgToArr)
            y.append(1)  # 1 means patient has cancer
        
        # Splitting dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
        
        X_train = np.array(X_train)
        # X_test = np.array(X_test)
        # y_train = np.array(y_train)
        # y_test = np.array(y_test)
        
        # def plot_sample(X, y, index):
        #     plt.figure(figsize=(15,2))
        #     plt.imshow(mpimg.imread(X[index]))
        #     plt.xlabel(self.mainClasses[y[index]])
            
        # plot_sample(X_train, y_train, 0)
        
        # Normalizing training data (images)
        X_train = X_train / 255.0
        print(X_train)
        # X_test = X_test / 255.0
        
        # cnn = models.Sequential([
        #     layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
        #     layers.MaxPooling2D((2, 2)),
            
        #     layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        #     layers.MaxPooling2D((2, 2)),
            
        #     layers.Flatten(),
        #     layers.Dense(64, activation='relu'),
        #     layers.Dense(10, activation='softmax')
        # ])
        
        
        # cnn.compile(optimizer='adam',
        #     loss='sparse_categorical_crossentropy',
        #     metrics=['accuracy'])
        
        # cnn.fit(X_train, y_train, epochs=10)
        # cnn.evaluate(X_test, y_test)
            

gui = GUI(root)
tk.mainloop()












