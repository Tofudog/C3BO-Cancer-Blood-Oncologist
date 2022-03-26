"""

sentences = ["do or do not, there is no try",
              "artwodeetwo", "Goodbye friends",
              "easy there chewie", "beep boop",
              "We're related Leia, we can't get married!",
              "Join the dark side, idiot!"]

Created on Thu Feb  3 09:10:56 2022

This provides the source code for the
app GUI functionalities of C-3BO.
Hopefully, this will be nice to look at!

@author: leode
"""






import os
os.environ['KIVY_TEXT'] = 'pil'
import kivy

## App is present in kivy_installation_dir/kivy/app.py.
from kivy.app import App


# specific imports from layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.window import Window


# importing design from kivy_app.kv
from kivy.lang import Builder

# Miscellaneous imports
import random
import io

import cv2 as cv

# c3bo functionality
from CBO import C3BO

import numpy as np
from keras.metrics import Precision, Recall, AUC,\
SensitivityAtSpecificity, SpecificityAtSensitivity


Builder.load_file('kivy_app.kv')



# path = "C-3BO_project/C3BO.png"
# img = Image(source=path)
# self.image = img

# button =  Button(text="Submit",
#                   background_color=(0, 10, 1, 8),
#                   on_release=self.callback)


def driverModel():
    ##### ----------------
    parent = "Blood-Cancer_Data"
    ALL_IDB1 = f"{parent}/All_IDB1/im"
    annotate1 = f"{parent}/ALL_IDB1/xyc"
    AML_ALL_img = f"{parent}/SN-AM-BALL-MM"
    classes_AML_ALL, _, __ = os.walk(AML_ALL_img)
    multiple_myeloma = f"{parent}/multiple_myeloma"
    myeloma_annotate = f"{parent}/multiple_myeloma/Annotated_PPT_MM_Data.pdf"
    ##### ----------------
    
    c3bo = C3BO(main_file=parent, annotate_file=annotate1, classes=None)
    c3bo.annotate_files(ALL_IDB1, AML_ALL_img)
    data = c3bo.classes
    img_files, centroid_files = data.keys(), data.values()
    
    c3bo.to_df(img_files, centroid_files)
    c3bo.label_diagnosis()
    c3bo.strong_neural_net((128, 128, 3), 3)
    
    metrics = ["accuracy", Precision(), Recall(), AUC(),
                SensitivityAtSpecificity(0.5), SpecificityAtSensitivity(0.5)]
    c3bo.compile_model('rmsprop', 'categorical_crossentropy', metrics)
    
    df = c3bo.df
    
    img_pixels = df["image_pixels"].copy()
    labels = df["diagnosis"].copy()
    files = df["image_files"].copy()
    c3bo.preprocess(labels)
    
    X_full_data = c3bo.images_array(img_pixels, (128, 128, 3))
    X_full_data = c3bo.shuffle_data(X_full_data)
    
    X_train, y_train, X_val, y_val, X_test, y_test = c3bo.partitioned_data(X_full_data)
    c3bo.train(X_train, y_train, X_val, y_val)
    
    return c3bo.model


# model = driverModel()


# class LoadDialog(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)


# class SaveDialog(FloatLayout):
#     save = ObjectProperty(None)
#     text_input = ObjectProperty(None)
#     cancel = ObjectProperty(None)

classes = ["ALL", "Healthy", "MM", "Chronic Myeloid Leukemia"]

class Chatbot(PageLayout):
    
    # def show_load(self):
    #     content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Load file", content=content,
    #                         size_hint=(0.9, 0.9))
    #     self._popup.open()

    # def show_save(self):
    #     content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Save file", content=content,
    #                         size_hint=(0.9, 0.9))
    #     self._popup.open()
    
    def leaveApp(self):        
        App.get_running_app().stop()
        Window.close()

    def recordImg(self):
        field = str.split(self.ids.fileId.text, sep="; ")
        image_file = field[0]
        genetic_id = field[1]
        self.ids.input_image.source = image_file
        img = cv.imread(image_file)
        print(img)
        img = cv.resize(img, (128, 128))
        
        #pred = classes[np.argmax(model.predict(np.expand_dims(img, axis=0)))]
        pred = ""
        
        #self.ids.name_label.text = "Leonardo de Farias is cool"
        if pred != "healthy":
            self.ids.clinCls.text = f"Oh My! you do have {pred}"
        
        
        
    # def select(self, *args):
    #     try: self.label.text = args[1][0]
    #     except: pass
        
    
    

        
        



class CustomApp(App):

    def build(self):
        return Chatbot()


if __name__ == '__main__':
    CustomApp().run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def nextSentence(self)
#     return self.sentences(random.randint(1, 6))


# class CustomBtn(Widget):

#      pressed = ListProperty([0, 0])

#      def on_touch_down(self, touch):
#          if self.collide_point(*touch.pos):
#              self.pressed = touch.pos
#              return True
#          return super(CustomBtn, self).on_touch_down(touch)
     
#     def on_pressed(self, instance, pos):
#         print ('pressed at {pos}'.format(pos=pos))
    







        









































    # FloatLayout:
              
    #     canvas.before:
    #         Color:
    #             rgba: (1, 1, 1, 1)
    #         Rectangle:
    #             source:'C-3BO_project/background.jpg'
    #             size: root.width, root.height
    #             pos: self.pos

    #     Image:
    #         id: c3bo
    #         source: "C-3BO_project/C3BO.png"
    #         pos: (80, 50)
    #         size_hint: (2, 2)
            
    #     Image:
    #         id: callout
    #         source: "C-3BO_project/c3bo_callout.png"
    #         pos: (80, 185)
    #         size_hint: (2, 2)
            
    #     Label:
    #         text: "Personal Credentials"
    #         pos: (900, 125)
    #         size_hint: (5, 5)
            
    #     Label:
    #         id: credential_type
    #         text: "Full Name (Last, First, Middle)"
    #         pos: (850, 80)
    #         size_hint: (2, 2)
            
        
    #     # Adjust background_normal (be creative)
    #     TextInput:
    #         multiline: True
    #         hint_text: 'Luke Skywalker'
    #         pos: (915, 50)
    #         size_hint: (3, 3)
            
    # GridLayout:
    
    #     rows: 1
    #     cols: 1
        
    #     Label:
    #         text: "mama mia!"





"""    FloatLayout:
    
        canvas:
            Color:
                rgba: 143 / 255., 112 / 205., 88 / 255., 1
            Rectangle:
                pos: self.pos
                size: self.size
    
        
        Image:
            source: "C-3BO_project/R2D2_img.jpg"
            size_hint: (.5, .25)
            #pos: (125, 300)
        
        # Peripheral Blood Smear Image
        Image:
            source: "Blood-Cancer_Data/ALL_IDB1/im/Im001_1.jpg"
            size_hint: (.5, .25)
            #pos: (235, 415)
        """






    
    
    
    
    
    