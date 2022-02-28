"""
Created on Thu Dec 30 21:06:26 2021

@author: leode
@company: Blood Bots (BB8)
"""


####### Make sure to get back AML.json file
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
import tensorflow as tf
import keras
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import cv2 as cv
from PIL import Image

import glob
import os
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

### To experiment with other possibly useful
# layers or loss functions from tensorflow

from tensorflow.keras.layers import Input, LSTM
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.metrics import RootMeanSquaredError





class C3BO:
    
    def __init__(self, main_file, annotate_file, classes):
        self.parent = main_file
        self.annotation = annotate_file
        self.classes = classes
        self.y_classes = None
        self.df = None
        self.target_size = (128, 128)
        
    def __str__(self):
        return f"main_file: {self.parent}, labels: {self.classes}\n {self.df.head()}"
    
    def __del__(self):
        pass

    def annotate_files(self, file1, *extra_files):
        classes = dict()
        iter_file = lambda file: [f for f in glob.glob(file + "/*")]
        # Getting every file necessary
        file_list = [file1]
        
        for f in extra_files:
            try:
                a, b, c = os.walk(f)
            except ValueError:
                file_list.append(f)
            except Exception as e:
                print(type(e))
            else:
                for f_ in a[1]:
                    file_list.append(f + "/" + f_)
                    
        for file in file_list:    
            for im_num, (file_, annotate) in enumerate(zip(iter_file(file), iter_file(self.annotation))):     
                if "All_IDB" not in file:
                    if "ALL" in (file_.split("/")[-1]):
                        classes[file_] = "ALL"
                    else:
                        classes[file_] = "MM"
                else:
                    if "_1" in annotate:
                        classes[file_] = "ALL"
                    elif "_0" in annotate:
                        classes[file_] = "healthy"     
        self.classes = classes
    
    def to_df(self, img_files, centroid_files):
        self.df = pd.DataFrame(data={"image_files":img_files,
                                     "annotations:":centroid_files})
        self.df["image_pixels"] = self.df["image_files"].apply(lambda img: mpimg.imread(img)/255.)
        self.df["image_pixels"] = self.df["image_pixels"].apply(lambda img: cv.resize(img, dsize=(128, 128)))
        
    def diagnose_labeling(self, img_file):  
        if "_1" in img_file:
            return "ALL"
        elif "_0" in img_file: 
            return "Healthy"
        
        # Should not be to -5, but -4
        return img_file.split("/")[1][:-8]
    
    def label_diagnosis(self): 
        self.df["diagnosis"] = self.df["image_files"].apply(self.diagnose_labeling)
    
    # Ideal model
    def strong_neural_net(self, shape, n_classes):
        model = Sequential()
        model.add(Conv2D(filters=32, kernel_size=(3, 3), activation="relu", input_shape=shape))
        model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))
        model.add(MaxPooling2D(pool_size=(4, 4)))
        model.add(Dropout(0.4))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))
        model.add(Conv2D(filters=32, kernel_size=(3, 3), activation="relu"))
        model.add(Conv2D(filters=8, kernel_size=(2, 2), activation="relu"))
        model.add(Flatten())
        model.add(Dense(units=64, activation="relu"))
        model.add(Dense(units=n_classes, activation="softmax"))
        self.model = model
    
    def compile_model(self, optimizer="rmsprop", loss="categorical_crossentropy", metric_list=["accuracy"]):
        self.model.compile(optimizer, loss, metrics=metric_list)
    
    def preprocess(self, labels):
        LE = LabelEncoder()               
        self.y_classes = LE.fit_transform(labels)
        
    def images_array(self, data, target_shape):
        final_arr = np.array([[[[]]]])
        n_samples = len(data)
        rows, cols, rgb = target_shape
        for i, d in enumerate(data):
            if d.shape != target_shape:
                n_samples -= 1
                continue
            final_arr = np.append(final_arr, d)
        return final_arr.reshape(n_samples, rows, cols, rgb)
    
    def shuffle_data(self, X_full_data, rand_scale=None):
        indices = np.arange(self.df.shape[0])
        np.random.shuffle(indices)
        X_full_data = X_full_data[indices]
        self.y_classes = self.y_classes[indices]
        return X_full_data
    
    def partitioned_data(self, X_data):
        y_classes = self.y_classes
        y_classes = keras.utils.to_categorical(y_classes, 3)
        X_train, X_val, X_test = X_data[0:180], X_data[180:300], X_data[300:]
        y_train, y_val, y_test = y_classes[0:180], y_classes[180:300], y_classes[300:]
        return X_train, y_train, X_val, y_val, X_test, y_test

    def train(self, X_train, y_train, X_val, y_val):
        datagen = ImageDataGenerator()        
        datagen.fit(X_train)
        hist = self.model.fit(datagen.flow(X_train, y_train),
                             validation_data=(X_val, y_val), epochs=35,
                             steps_per_epoch=10)
        
        ######------------------
        # hist_df = pd.DataFrame(cnn_hist.history) 
        # # save to json:  
        # hist_json_file = 'C-3BO_project/results/cnn_history1.json' 
        # with open(hist_json_file, mode='w') as f:
        #     hist_df.to_json(f)
        ######------------------
        
    

from keras.metrics import Precision, Recall, AUC,\
SensitivityAtSpecificity, SpecificityAtSensitivity


# def main():
#     ##### Files to be used
#     parent = "Blood-Cancer_Data"
#     ALL_IDB1 = f"{parent}/All_IDB1/im"
#     annotate1 = f"{parent}/ALL_IDB1/xyc"
#     AML_ALL_img = f"{parent}/SN-AM-BALL-MM"
#     classes_AML_ALL, _, __ = os.walk(AML_ALL_img)
#     multiple_myeloma = f"{parent}/multiple_myeloma"
#     myeloma_annotate = f"{parent}/multiple_myeloma/Annotated_PPT_MM_Data.pdf"
#     ##### ----------------
    
#     c3bo = C3BO(main_file=parent, annotate_file=annotate1, classes=None)
#     c3bo.annotate_files(ALL_IDB1, AML_ALL_img)
#     data = c3bo.classes
#     img_files, centroid_files = data.keys(), data.values()
    
#     c3bo.to_df(img_files, centroid_files)
#     c3bo.label_diagnosis()
#     c3bo.strong_neural_net((128, 128, 3), 3)
    
#     metrics = ["accuracy", Precision(), Recall(), AUC(),
#                 SensitivityAtSpecificity(0.5), SpecificityAtSensitivity(0.5)]
#     c3bo.compile_model('rmsprop', 'categorical_crossentropy', metrics)
    
#     df = c3bo.df
    
#     img_pixels = df["image_pixels"].copy()
#     labels = df["diagnosis"].copy()
#     files = df["image_files"].copy()
#     c3bo.preprocess(labels)
    
#     X_full_data = c3bo.images_array(img_pixels, (128, 128, 3))
#     X_full_data = c3bo.shuffle_data(X_full_data)
    
#     X_train, y_train, X_val, y_valn, X_test, y_test = c3bo.partitioned_data(X_full_data)
#     c3bo.train(X_train, y_train, X_val, y_val)

# if __name__ == '__main__':
#     main()





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    