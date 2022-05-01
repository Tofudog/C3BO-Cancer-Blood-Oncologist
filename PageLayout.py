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
import numpy as np
# from keras.metrics import Precision, Recall, AUC,\
# SensitivityAtSpecificity, SpecificityAtSensitivity

# Builder.load_file('star_design.kv')  ### must change Widget to PageLayout


from kivy.graphics import Line










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








class Chatbot(FloatLayout):


    def __init__(self, **kwargs):
        
        super(FloatLayout, self).__init__(**kwargs)
        
        self.leuk_link = "https://github.com/Tofudog/C3BO-Cancer-Blood-Oncologist"
        self.classes = ["ALL", "Healthy", "MM", "Chronic Myeloid Leukemia"]
        self.curr_img_file = None
        self.model = None # model
        bck_color = "olive"
       
        self.curr_img_file = None
        self.curr_genetic_id = None
        
        quote_label = Label(text="[i]“R2D2, You Know Better Than To Trust A Strange Computer!” -C-3PO[/i]",
                            markup=True, font_size=16, color="black", pos=(205, 10))
        self.add_widget(quote_label)
        
        
        
        r2d2_img = Image(source="C-3BO_project\R2D2_img.png", size=(165, 165), pos=(440, 270))
        self.add_widget(r2d2_img)
        
        with self.canvas:
            Line(points=[575, 405, 600, 425], color="red")
        
        #later change to just diagnose_button
        diagnose_button = Button(text="Diagnose Peripheral\nBlood Smear", color="white", 
                                  background_color="#F24B82", background_down="red",
                                  size=(145, 65), pos=(515, 100), on_release=self.diagnose)
        self.add_widget(diagnose_button)

        
        (88, 141, 92)
        self.txt_input_file = TextInput(text="Or type in the file's path...",
                                    auto_indent=True, cursor_blink=True,
                                    background_color="#588D5C", size=(195, 75), pos=(700, 100))
        self.add_widget(self.txt_input_file)
        
        #file_chooser = FileChooserListView(on_selection=self.select, pos=(555, 100))
        #self.add_widget(file_chooser)

    
        
        ### update
        self.point_list = [
            600, 375, 600, 645,
            600, 375, 900, 375,
            900, 375, 900, 645,
            600, 645, 900, 645,
        ]
        
        with self.canvas:
            # (0, 128, 128)
            Line(points=self.point_list, color="#008080", width=2, dash_offset=1)
        
        
        
        og_display_img = "C-3BO_project\leukemia_front.png"
        self.leuk_img = Image(source=og_display_img, size=(215, 185), pos=(620, 395))
        self.add_widget(self.leuk_img)
        
        self.add_widget(
            Label(text="[u]Diagnostic Results[/u]", markup=True,
            font_size=28, color="black", pos=(1030, 565))  
        )
        
        
        self.bullet1 = "leukemia is ..."
        self.bullet2 = "Prognosis: ..."
        self.bullet3 = "Likelihood: ...%"
        self.bullet4 = "BCR-ABL1 Gene: ..."
        
        self.bullets = f"* {self.bullet1}\n* {self.bullet2}\n* {self.bullet3}\n* {self.bullet4}"
        self.bulleted_results = Label(text=self.bullets, size=(60, 135), color="black", pos=(1020, 480))
        self.add_widget(self.bulleted_results)
        
        #self.add_widget(
        #    Image(source="C-3BO_project\results\abl1_bcr_algo.png",
        #          size=(300, 205), pos=(1010, 100))    
        #)
            

        # logo = Image(source="C-3BO_project/c3bo_temp_logo.png",
        #              size=(self.width+10, self.height+10), pos=(20, 630))
        # self.add_widget(logo)
        
        # # Markup must be set to true to underline, ital, etc...
        # # ellipsis_options={'color':(180, 67, 38, 1),'underline':True}
        # title = Label(text="[u][i]Cancer-3 Blood Oncologist[/i][/u]",
        #               markup=True, font_size=60,
        #               ellipsis_options={'color':(180, 67, 38, 1),'underline':True},
        #               pos=(570, 660))
        # self.add_widget(title)
        
        
        # # Hopefully star wars text font
        # label2 = Label(text="[b]General Info[/b]", 
        #                 markup=True, size_hint_y=1, color=bck_color,
        #                 outline_color="black", outline_width=2, font_size=30,
        #                 pos=(60, 475))
        # self.add_widget(label2)
        
        # info = "* Leukemia: overproduction of WBC in marrow"
        # info += "\n* C-3BO operates with a custom CNN"
        # info += "\n* C-3BO cannot speak spanish"
        # info += "\n* Version 2.2 comes with BCR-ABL1 analysis"
        # info_label = Label(text=info, size=(60, 135), color="black",
        #                     pos=(145, 400))
        # self.add_widget(info_label)
        
        # self.leuk_link = "https://github.com/Tofudog/C3BO-Cancer-Blood-Oncologist"
        # proj_info = Button(text="Full Open-Source\nProject + Code", size=(200, 60),
        #                    color="white", background_color="#F24B82", pos=(25, 165))
        # proj_info.bind(on_release=self.leukemia_info)
        # self.add_widget(proj_info)
        
        # # Later use this quote: "R2D2, You Know Better Than To Trust A Strange Computer!"
        # quote = Label(text="[i]“We Seem To Be Made To Suffer. It’s Our Lot In Life.”[/i] -C-3PO",
        #               markup=True, font_size=16,
        #               color="black", underline=False,
        #               pos=(185, 10))
        # self.add_widget(quote)
        
        # image = Image(source="C-3BO_project/C3BO.png",
        #               size=(self.width + 120, self.height + 120), pos=(510, 50))
        
        # # #### no attribute 'texture_size' ---> no need to observe, as .kv will handle
        # self.add_widget(image)
        
        # ############ FIX! color: #FF6B7C
        # # robo_talk = Label(text="Greetings Doctor How may I help you?", markup=True, font_size=18,
        # #                   color="black", background_color="red", pos=(545, 105))
        # # self.add_widget(robo_talk)
        
        # inputEmail = TextInput(text="Type in your email: ", multiline=False, size=(345, 40), pos=(780, 135))
        # self.add_widget(inputEmail)
        
        # self.add_widget(
        #     TextInput(text="email a question...", multiline=True, size=(345, 40), pos=(780, 95))
        # )
        
        
        # send_email = Button(text="Send", size=(345, 40),
        #                    color="white", background_color="FB830F", pos=(780, 55))
        
        # self.add_widget(send_email)
        
        
        
        
        
        
        
        
        
        
        
        
    
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
        
    def pointList(self, *args):
        return self.point_list

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
  
    def diagnose(self, btn):
        ### bottom regex does not work yet
        #m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
        #self.curr_img_file = self.txt_input_file.text
        self.leuk_img.source = self.curr_img_file
        img = cv.imread(self.curr_img_file)
        img = cv.resize(img, (128, 128))
        img = np.expand_dims(img, 0)
        
        pred = self.classes[np.argmax(self.model.predict(img))]
        likelihood = np.max(self.model.predict(img))
        
        if pred != "Healthy":
            self.bullet1 = "Leukemia is present"
            self.bullet2 = f"Prognosis: {pred}"
            self.bullet3 = f"Likelihood: {likelihood*100.}%"
            self.bullet4 = "No BCR-ABL1"
        else:
            self.bullet1 = "Leukemia is not present"
            self.bullet2 = "---"
            self.bullet3 = "---"
            self.bullet4 = "No BCR-ABL1"
            
        self.bullets = f"* {self.bullet1}\n* {self.bullet2}\n* {self.bullet3}\n* {self.bullet4}"
        self.bulleted_results.text = self.bullets
        
        
        print()
        print(f"prediction for file {self.curr_img_file}: {pred}")
    


class Star(FloatLayout):
    
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
    

        
        

########## Test this out later

class CustomApp(App):

    def build(self):
        # 1. (216 / 255., 195 / 255., 21 / 255., 1)
        # 2. (128 / 255., 128 / 255., 0, 1)
        Window.clearcolor = (128 / 255., 128 / 255., 0, 1)
        #Window.clearcolor = (216 / 255., 195 / 255., 21 / 255., 1)
        return Chatbot()


if __name__ == '__main__':
    CustomApp().run()
    



