import kivy
import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.text import Label
from kivy.core.text import LabelBase
from database import DataBase


mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="weak",
      database="mydatabase"
    )


class SigninWindow(BoxLayout,Screen,Widget):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    info = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def loginBtn(self):
        
        if db.validate(self.email.text, self.pwd.text):
            MainWindow.current = self.email.text
            self.reset()
            self.info.text = ""
            self.manager.current = "main"
        else:
            self.info.text = "[color=#FF0000]Email ID or Password is Incorrect[/color]"
            self.reset()
    
     
    def reset(self):
        self.email.text = ""
        self.pwd.text = ""
        
    
            
class Signup(BoxLayout,Screen,Widget):
    
    name1 = ObjectProperty(None)
    year = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    pwd1 = ObjectProperty(None)
    branch = ObjectProperty(None)
    contact = ObjectProperty(None)    
    s_name = ObjectProperty(None)
    mail = ObjectProperty(None)
    passw = ObjectProperty(None)
    passw1 = ObjectProperty(None)
    con = ObjectProperty(None)
    
    def submit(self):
        if self.name1.text != "":
            if self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
                    if len(self.pwd.text) > 5:
                        if self.pwd.text == self.pwd1.text:
                            if self.pwd != "":
                                db.add_user(self.email.text, self.pwd.text, self.name1.text)
                                self.reset()
                                self.manager.current = "main_win"
                            else:
                                self.passw.text = "[color=#FF0000]Cannot be left blank[/color]"
                        else:
                            self.passw1.text = "[color=#FF0000]Do not Match[/color]"
                    else:
                        self.passw.text = "[color=#FF0000]Strength weak[/color]"
            else:
                self.mail.text = "[color=#FF0000]Enter Valid Email Id[/color]"
        else:
            self.s_name.text = "[color=#FF0000]Enter Full Name[/color]"
            
    def re(self):
        self.branch.text = ""
        self.passw1.text = ""
        self.passw.text = ""
        self.reset()
        sm.current = "main_win"
        
    def reset(self):
        self.branch.text = ""
        self.year.text = ""
        self.pwd1.text = ""
        self.contact.text = ""
        self.email.text = ""
        self.pwd.text = ""
        self.name1.text = ""
                                


class MainWindow(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
    

class Prof_page(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)

class PY_Lang(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)


class C_Lang(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)


class jv_lang(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)


class RasB_Lang(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)


class py_info(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_info1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_first(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_fnx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_fnx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_finfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #Second Project
class py_sec(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_snx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_snx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_sinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #third Project
class py_third(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_tnx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_tnx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_tinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #fourth Project
class py_four(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_fonx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_fonx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class py_foinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)

class jv_info(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_info1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_first(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_fnx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_fnx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_finfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #Second Project
class jv_sec(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_snx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_snx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_sinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #third Project
class jv_third(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_tnx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_tnx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_tinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          #fourth Project
class jv_four(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_fonx1(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_fonx2(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
class jv_foinfo(BoxLayout, Screen):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)


class WindowManager(ScreenManager): 
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()
    
sm = WindowManager()
db = DataBase("users.txt")
    
class SigninApp(App):
    def build(self):
        return 


if __name__ == "__main__":
    SigninApp().run() 
