import webbrowser
from tkinter import Tk
r = Tk()
word = r.selection_get(selection="CLIPBOARD")
url = "https://translate.google.com/?sl=auto&tl=bg&text="+word+"&op=translate"
webbrowser.open(url)