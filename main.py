from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen,ScreenManager

from instructions import*

name = ''
age = 0
p1 = 0
p2 = 0
p3 = 0

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
        self.btn1 = Button(text = "Начать",color = "#FFFFFF",size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(text ='0',multiline=False)
        

        self.label1 = Label(text = txt_instruction)
        self.label2 = Label(text = "Имя:",halign = 'right')
        self.label3 = Label(text = "Возраст:",halign = 'right')

        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)

        self.h1 = BoxLayout(spacing = 8,size_hint=(0.8, None), height='30sp')
        self.h2 = BoxLayout(spacing = 8,size_hint=(0.8, None), height='30sp')

        self.h1.add_widget(self.label2)
        self.h1.add_widget(self.name_input)

        self.h2.add_widget(self.label3)
        self.h2.add_widget(self.age_input)

        self.v1.add_widget(self.label1)
        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.h2)  
        self.v1.add_widget(self.btn1)   

        self.add_widget(self.v1)
        self.btn1.on_press = self.next
    def next(self):
        global name,age
        name = self.name_input.text
        age = int(self.age_input.text)
        self.manager.current = '1' 
class FirstScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = Button(text = "Продолжить",color = "#FFFFFF",size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.res_input = TextInput(text ='0',multiline=False)
        

        self.label1 = Label(text = txt_test1)
        self.label2 = Label(text = "Введите результат:",halign = 'right')

        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)

        self.h1 = BoxLayout(spacing = 8,size_hint=(0.8, None), height='30sp')

        self.h1.add_widget(self.label2)
        self.h1.add_widget(self.res_input)

        self.v1.add_widget(self.label1)
        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.btn1)   

        self.add_widget(self.v1)
        self.btn1.on_press = self.next
    def next(self):
        global p1
        p1 = int(self.res_input.text)
        self.manager.current = '2' 
class SecondScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = Button(text = "Продолжить",color = "#FFFFFF",size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.label1 = Label(text = txt_test2)
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label1)
        self.v1.add_widget(self.btn1)
        self.add_widget(self.v1)
        self.btn1.on_press = self.next
    def next(self):
        self.manager.current = '3' 
class ThirdScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = Button(text = "Завершить",color = "#FFFFFF",size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.res1_input = TextInput(text ='0',multiline=False)
        self.res2_input = TextInput(text ='0',multiline=False)
        

        self.label1 = Label(text = txt_test3)
        self.label2 = Label(text = "Результат:",halign = 'right')
        self.label3 = Label(text = "Результат после отдыха:",halign = 'right')

        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)

        self.h1 = BoxLayout(spacing = 8,size_hint=(0.8, None), height='30sp')
        self.h2 = BoxLayout(spacing = 8,size_hint=(0.8, None), height='30sp')
        self.h1.add_widget(self.label2)
        self.h1.add_widget(self.res1_input)

        self.h2.add_widget(self.label3)
        self.h2.add_widget(self.res2_input)

        self.v1.add_widget(self.label1)
        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.h2)
        self.v1.add_widget(self.btn1)   

        self.add_widget(self.v1)
        self.btn1.on_press = self.next
    def next(self):
        global p2,p3
        p2 = int(self.res1_input.text)
        p3 = int(self.res2_input.text)
        self.manager.current = '4' 
class FourthScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)   
        self.label = Label(text = "Экран 4")
        self.v1 = BoxLayout(orientation = "vertical",padding = 8,spacing = 8)
        self.v1.add_widget(self.label)
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
