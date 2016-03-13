from tkinter import *

def scoreboardDisplay():
        root = Tk()
        root.title("Scoarboard")

        displayTextWidget = Text(root)

        txt_file = open("ScoreboardStore.txt")
        displayText = txt_file.read()
        txt_file.close()

        displayTextWidget.insert(0.0, displayText)

        displayTextWidget.pack(expand=1, fill=BOTH)

        root.mainloop()

class scoreboardGUI:
    def __init__(self, master):
        self.master = master
        master.title("Scoreboard")

        #root.geometry("500x500")

        self.label = Label(master, text = "Your score was: ")
        self.label.pack()

        self.label = Label(master, text = "Please enter your display name: ")
        self.label.pack()

        self.input = Entry(root)
        self.input.pack()
        
        self.submit_button = Button(master, text = "Submit", command = self.submit)
        self.submit_button.pack()

    def submit(self):
        value = 0
        f = open("ScoreboardStore.txt", "a")
        f.write("\n" + str(value) + "........." + self.input.get())
        f.close()
        scoreboardDisplay()

root = Tk()
scoreboard = scoreboardGUI(root)
root.mainloop()
