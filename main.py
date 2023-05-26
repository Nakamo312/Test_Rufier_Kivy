from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main',**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal



class MainScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = ScrButton(self,'down','1',text = "1 экран",color = "#FFFFFF")
        self.btn2 = ScrButton(self,'left','2',text = "2 экран",color = "#FF0000")
        self.btn3 = ScrButton(self,'up','3',text = "3 экран",color = "#00FF00")
        self.btn4 = ScrButton(self,'right','4',text = "4 экран",color = "#0000FF")

        self.label = Label(text = "Нажми на любую кнопку")

        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.h1 = BoxLayout(spacing = 8)
        self.v1.add_widget(self.btn1)
        self.v1.add_widget(self.btn2)
        self.v1.add_widget(self.btn3)
        self.v1.add_widget(self.btn4)    

        self.h1.add_widget(self.label)
        self.h1.add_widget(self.v1) 

        self.add_widget(self.h1)



class FirstScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = ScrButton(self,'up','main',text = "Назад",color = "#FFFFFF")
        self.label = Label(text = "Экран 1")
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label)
        self.v1.add_widget(self.btn1)
        self.add_widget(self.v1)
class SecondScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = ScrButton(self,'right','main',text = "Назад",color = "#FFFFFF")
        self.label = Label(text = "Экран 2")
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label)
        self.v1.add_widget(self.btn1)
        self.add_widget(self.v1)
class ThirdScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = ScrButton(self,'down','main',text = "Назад",color = "#FFFFFF")
        self.label = Label(text = "Экран 3")
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label)
        self.v1.add_widget(self.btn1)
        self.add_widget(self.v1)
class FourthScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)   
        self.btn1 = ScrButton(self,'left','main',text = "Назад",color = "#FFFFFF")
        self.label = Label(text = "Экран 4")
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label)
        self.v1.add_widget(self.btn1)
        self.add_widget(self.v1)     
class MyFirstApp(App):

    def build(self):
        sm = ScreenManager() 
        sm.add_widget(MainScreen(name = 'main'))

        sm.add_widget(FirstScreen(name = '1'))
        sm.add_widget(SecondScreen(name = '2'))
        sm.add_widget(ThirdScreen(name = '3'))
        sm.add_widget(FourthScreen(name = '4'))
        return sm

app = MyFirstApp()
app.run()