import webbrowser
from tkinter import Tk
from tkinter import TclError
r = Tk()

try:
	word = r.selection_get(selection="CLIPBOARD")
	url = "https://translate.google.com/?sl=auto&tl=bg&text="+word+"&op=translate"
	webbrowser.open(url)
except TclError:
    
	print('clipboard is empty')