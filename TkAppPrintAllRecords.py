# A GUI designed using Tkinter to display all records of Flimflix


import tkinter as tk
import tkinter.font as tkFont


class PrintAllRecordGUI(tk.Toplevel):
    nid = 0
    message = []

    def __init__(self, master, nid, title, message, winSize):
        tk.Toplevel.__init__(self, master)
        self.nid = nid
        self.title(title)
        self.message = message
        self.winSize = winSize

        self.display_note_gui()

    def display_note_gui(self):
        self.geometry(self.winSize)
        self.protocol("WM_DELETE_WINDOW", self.win_x)

        self.configure(background="#BAD0EF")
        title = tk.Entry(self, relief="flat", bg="#BAD0EF", bd=0)
        title.pack(side="top")
        scrollBar = tk.Scrollbar(self, takefocus=0, width=10)
        scrollBar.pack(side="right", fill="y")

        textArea = tk.Text(
            self, height=4, width=1000, bg="#BAD0EF", font=("Times", "14")
        )
        textArea.pack(side="left", fill="y")
        scrollBar.config(command=textArea.yview)
        textArea.config(yscrollcommand=scrollBar.set)
        textArea.insert("end", "  Reading data from table:" + "\n")

        if type(self.message) == str:
            textArea.insert("end", "  " + self.message + "\n")
        else:
            for row in self.message:
                textArea.insert("end", "  " + str(row) + "\n")

    def win_x(self):
        self.destroy()
