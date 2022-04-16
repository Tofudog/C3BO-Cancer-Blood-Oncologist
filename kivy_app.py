import os
#os.environ['KIVY_TEXT'] = 'pil'
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
import kivy
from kivy.app import App


# specific imports from layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window


# To get extra fonts
from kivy.core.text import LabelBase

# importing design from kivy_app.kv
# from kivy.lang import Builder

# Miscellaneous imports
import random
import io
import cv2 as cv

# c3bo functionality
# from CBO import C3BO
# import numpy as np
# from keras.metrics import Precision, Recall, AUC,\
# SensitivityAtSpecificity, SpecificityAtSensitivity

# Builder.load_file('star_design.kv')  ### must change Widget to PageLayout

# LabelBase.register(name=, fn_regular='')
# path = "C-3BO_project/C3BO.png"
# img = Image(source=path)
# self.image = img
# button =  Button(text="Submit",
#                   background_color=(0, 10, 1, 8),
#                   on_release=self.callback)





# def driverModel():
#     ##### ----------------
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
    
#     X_train, y_train, X_val, y_val, X_test, y_test = c3bo.partitioned_data(X_full_data)
#     c3bo.train(X_train, y_train, X_val, y_val)
    
#     return c3bo.model


# model = driverModel()









classes = ["ALL", "Healthy", "MM", "Chronic Myeloid Leukemia"]











class CustomImage(Image):
    def __init__(self, **kwargs):
        super(Image, self).__init__()

    def texture_width(self):
        return self.texture.size[0]

    def texture_height(self):
        return self.texture.size[1]

    def rescale(self, width, height):
        """
        Resize the image to fit the given dimensions, zooming in or out if
        needed without losing the aspect ratio
        :param width: target width
        :param height: target height
        :return: new dimensions as a tuple (width, height)
        """
        ratio = 0.0
        new_width = 0.0
        new_height = 0.0

        target_width = float(width)
        target_height = float(height)

        image_width = float(self.texture_width())
        image_height = float(self.texture_height())

        ratio = target_width / image_width
        new_width = image_width * ratio
        new_height = image_height * ratio

        if (new_height < target_height):
            ratio = target_height / new_height
            new_height *= ratio
            new_width *= ratio

        if new_width > 0 and new_height > 0:
            self.width = new_width
            self.height = new_height

        return (new_width, new_height)
    
    

class Chatbot(FloatLayout):
    
    def __init__(self, **kwargs):
        
        super(FloatLayout, self).__init__(**kwargs)
        
        bck_color = "#D8C315"
        
       
        # self.curr_img_file = None
        # self.curr_genetic_id = None
        
        # with self.canvas:
        #     self.Rectangle.color = (63, 24, 25, 38)
        
    
        logo = Image(source="C-3BO_project/c3bo_temp_logo.png",
                     size=(self.width+10, self.height+10), pos=(20, 630))
        self.add_widget(logo)
        
        # Markup must be set to true to underline, ital, etc...
        # ellipsis_options={'color':(180, 67, 38, 1),'underline':True}
        title = Label(text="[u][i]Cancer-3 Blood Oncologist[/i][/u]",
                      markup=True, font_size=60,
                      ellipsis_options={'color':(180, 67, 38, 1),'underline':True},
                      pos=(570, 660))
        self.add_widget(title)
        
        
        # Hopefully star wars text font
        label2 = Label(text="[b]General Info[/b]", 
                        markup=True, size_hint_y=1, color=bck_color,
                        outline_color="black", outline_width=2, font_size=30,
                        pos=(60, 475))
        self.add_widget(label2)
        
        info = "* Leukemia: overproduction of WBC in marrow"
        info += "\n* C-3BO operates with a custom CNN"
        info += "\n* C-3BO cannot speak spanish"
        info += "\n* Version 2.2 comes with BCR-ABL1 analysis"
        info_label = Label(text=info, size=(60, 135), color="black",
                            pos=(145, 400))
        self.add_widget(info_label)
        
        self.leuk_link = "https://github.com/Tofudog/C3BO-Cancer-Blood-Oncologist"
        proj_info = Button(text="Full Open-Source\nProject + Code", size=(200, 60),
                           color="white", background_color="#F24B82", pos=(25, 165))
        proj_info.bind(on_release=self.leukemia_info)
        self.add_widget(proj_info)
        
        # Later use this quote: "R2D2, You Know Better Than To Trust A Strange Computer!"
        quote = Label(text="[i]“We Seem To Be Made To Suffer. It’s Our Lot In Life.”[/i] -C-3PO",
                      markup=True, font_size=16,
                      color="black", underline=False,
                      pos=(185, 10))
        self.add_widget(quote)
        
        image = Image(source="C-3BO_project/C3BO.png",
                      size=(self.width + 120, self.height + 120), pos=(510, 50))
        
        # #### no attribute 'texture_size' ---> no need to observe, as .kv will handle
        self.add_widget(image)
        
        ############ FIX! color: #FF6B7C
        # robo_talk = Label(text="Greetings Doctor How may I help you?", markup=True, font_size=18,
        #                   color="black", background_color="red", pos=(545, 105))
        # self.add_widget(robo_talk)
        
        inputEmail = TextInput(text="Type in your email: ", multiline=False, size=(345, 40), pos=(780, 135))
        self.add_widget(inputEmail)
        
        self.add_widget(
            TextInput(text="email a question...", multiline=True, size=(345, 40), pos=(780, 95))
        )
        
        
        send_email = Button(text="Send", size=(345, 40),
                           color="white", background_color="FB830F", pos=(780, 55))
        
        self.add_widget(send_email)
        
        # exitButton = Button(text="Exit", background_color=(2, 10, 19, 8),
        #                     pos=(980, 10))
        # exitButton.bind(on_press=self.leaveApp)
        # self.add_widget(exitButton)
        
        
        
        
        
        
    
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
    
    def leaveApp(self, *args):        
        App.get_running_app().stop()
        Window.close()

    def recordImg(self):
        # field = str.split(self.ids.fileId.text, sep="; ")
        # image_file = field[0]
        # curr_img_file = image_file
        
        # genetic_id = field[1]
        # curr_genetic_id = genetic_id
        
        # self.ids.input_image.source = image_file
        
        img = cv.imread(self.curr_img_file)
        img = cv.resize(img, (128, 128))
        
        # pred = classes[np.argmax(model.predict(np.expand_dims(img, axis=0)))]
        # pred = ""
        
        # #self.ids.name_label.text = "Leonardo de Farias is cool"
        # if pred != "healthy":
        #     self.ids.clinCls.text = f"Oh My! you do have {pred}"
        print(img.shape)
        print(img)
        
        
    def select(self, *args):
        try: 
            self.curr_img_file = args[1][0]
            print(self.curr_img_file)
        except FileNotFoundError:
            # start logger: leodefarias25@gmail.com
            # use logger to specify in an email
            print()
        except Exception as e:
            print(type(e))
            
    def leukemia_info(self, *args, **kwargs):
        import webbrowser
        # it will open google window in your browser
        webbrowser.open(self.leuk_link)
  
    
    
    """canvas:
            Color:
                rgba: 216 / 255., 195 / 255., 88 / 255., 1
            Rectangle:
                pos: self.pos
                size: self.size
 
        rows: 2
        cols: 3
        
        Label:
            text: "Greetings Patient\nHow may I help you?"
            halign: 'right'
            valign: 'middle'   
            
        Label:
            text: "General Info"
            size_hint_y: .4
            color: 0, 0, 0, 1
            outline_color: 0, 0.5, 0.5, 1
            font_size: 30
             
        Label:
            text: ""

        Image:
            # Strangely enough, source should be .png
            source: "C-3BO_project/C3BO.png"
            size: self.texture_size
        
        Label:
            text: ""

        TextInput:
            ### somehow get research on questions leuk.
            text: """

    
        
    
    

        
        

########## Test this out later

class CustomApp(App):

    def build(self):
        Window.clearcolor = (216 / 255., 195 / 255., 21 / 255., 1)
        return Chatbot()


if __name__ == '__main__':
    CustomApp().run()
    
    
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
    
"""        # Creating Icon view other side
        FileChooserIconView:
            canvas.before:
                Color:
                    rgb: .5, .4, .5
                Rectangle:
                    pos: self.pos
                    size: self.size
            on_selection: root.select(*args)
        ##########"""  
    
    
    
    
    
    
    
    
    
    
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






    
    
    
    
    
    