from tkinter import *

root = Tk()
root.title("Scoarboard")

displayTextWidget = Text(root)

txt_file = open("ScoreboardStore.txt")
displayText = txt_file.read()
txt_file.close()

displayTextWidget.insert(0.0, displayText)

displayTextWidget.pack(expand=1, fill=BOTH)

root.mainloop()
#Delete this file
