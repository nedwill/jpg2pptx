import kivy
kivy.require('1.7.2')
import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView,FileChooserIconView

class MainWindow(GridLayout):
	def __init__(self, **kwargs):
		super(MainWindow,self).__init__(**kwargs)
		self.cols = 2
		#filepicker, num selected
		#dwide "go"
		#self.add_widget(Label(text='Pick Files'))
		#filePickerButton = Button(text='Pick Files')
		#fileChooser = FileChooserListView(text='Pick Files')
		fileChooser = FileChooserIconView(text='Pick Files')
		self.add_widget(fileChooser)
		self.add_widget(Label(text='Number of Files Selected'))
		#self.username = TextInput(multiline=False)
		#self.add_widget(self.username)
		#self.add_widget(Label(text='password'))
		#self.password = TextInput(password=True, multiline=False)
		#self.add_widget(self.password)

class MyApp(App):
	title = "JPG2PPTX"
	def build(self):
		#self.title = "JPG2PPTX"
		return MainWindow()

if __name__ == '__main__':
	MyApp().run()