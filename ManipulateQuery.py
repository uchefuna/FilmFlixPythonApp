# Progrm to manipulate Queries in the table


from main import PythonAppBox as pab
from mysqlCRUD import *
import tkinter as tk


class InsertQuery(tk.Toplevel):
    nid = 0
    message = ""

    def __init__(self, master, nid, title, message, winSize):
        self.root = tk.Toplevel.__init__(self, master)
        # root=self.master
        self.nid = nid
        self.title(title)
        self.message = message
        self.winSize = winSize

        self.create_note_gui()

    def create_note_gui(self):
        self.geometry(self.winSize)
        self.maxsize(
            self.winSize.split("x")[0], self.winSize.split("x")[1]
        )  # width x height
        self.configure(background="#BAD0EF")

        labelTeaxt = [
            "filmID(integer):",
            "title(text):",
            "yearReleased(integer):",
            "rating(text):",
            "duration(integer):",
            "genre(text):",
        ]

        dec_info = tk.Label(
            self, text=self.message, bg="#BAD0EF", font=("Times", 14)
        ).grid(row=0, column=0, columnspan=4, padx=(10, 0), pady=5, sticky="w")

        z, r = 6, 7
        if "insert" in self.message:
            self.key_word = "insert"
            print("insert")
        elif "update" in self.message:
            labelTeaxt = ["UPDATE tblfilms SET:", "=:", "WHERE:", "=:"]
            self.key_word = "update"
            z, r = z - 2, r - 2
            print("update")
        elif "delete" in self.message:
            labelTeaxt = ["DELETE FROM tblfilms WHERE:", "=:"]
            self.key_word = "delete"
            z, r = z - 4, r - 4
            print("delete")
        elif "print" in self.message:
            labelTeaxt = ["SELECT * FROM tblfilms WHERE:", "=:"]
            self.key_word = "print"
            z, r = z - 4, r - 4
            print("print")

        self.bottom_note(r)
        self.mid_note(z, labelTeaxt)

    def mid_note(self, z, labelTeaxt):
        i, j = 0, 1
        self.entries = [tk.Entry(self, bd=3, font=("Arial", 12)) for _ in range(z)]
        self.entries[0].focus_set()
        for entry in self.entries:
            tk.Label(self, text=labelTeaxt[i], bg="#BAD0EF", font=("Times", 11)).grid(
                row=j, column=0, padx=(10, 320), pady=5, sticky="w"
            )
            entry.grid(row=j, column=0, columnspan=2, padx=(320, 0), pady=5, sticky="w")
            i, j = i + 1, j + 1

    def bottom_note(self, r):
        btn = tk.Button(self, text=self.key_word.upper())
        btn.grid(row=r, column=0, ipadx=5, padx=(15, 90), pady=5, sticky="w")
        btn.bind("<Button-1>", self.print_input)

        tk.Label(
            self,
            text=f"Click button to {self.key_word} records to the Flimflix table",
            bg="#BAD0EF",
            fg="#333333",
            font=("Arial", 14),
        ).grid(row=r, column=0, columnspan=5, padx=(70, 0), pady=5, sticky="w")

        tk.Label(
            self,
            text=f"NOTE: {self.key_word.title()} button only works when you provided the correct recrods accordingly with the datatype",
            bg="#BAD0EF",
            font=("Arial", 10),
        ).grid(row=r + 1, column=0, columnspan=4, padx=(10, 0), pady=5, sticky="w")

    def print_input(self, *args):
        entry_val = []
        for entry in self.entries:
            entry_val.append(entry.get())
            entry.delete(0, "end")
        print(entry_val)

        info_c = [
            "green",
            "Correct records and datatype entered and sent to the database."
            + "\n"
            + "You can insert more movies and/or close the window when you're done",
            "brown",
            "Please enter correct records or datatype",
            "red",
            "An error occured. Please enter correct records or datatype",
        ]
        try:
            if "insert" in self.message:
                if (
                    isinstance(int(entry_val[0]), int)
                    and isinstance(str(entry_val[1]), str)
                    and isinstance(int(entry_val[2]), int)
                    and isinstance(str(entry_val[3]), str)
                    and isinstance(int(entry_val[4]), int)
                    and isinstance(str(entry_val[5]), str)
                    and str(entry_val) != ""
                ):
                    fg_color = info_c[0]
                    labelTeaxt = info_c[1]
                    print(labelTeaxt)
                    self.destroy()
                    pab(self.root).button_query(0, 1, entry_val)
            elif "update" in self.message:
                if (
                    isinstance(str(entry_val[0]), str)
                    and isinstance(str(entry_val[2]), str)
                ) and (
                    str(entry_val[0]) != ""
                    and str(entry_val[1]) != ""
                    and str(entry_val[2]) != ""
                    and str(entry_val[3]) != ""
                ):
                    fg_color = info_c[0]
                    labelTeaxt = info_c[1]
                    print(labelTeaxt)
                    self.destroy()
                    pab(self.root).button_query(0, 2, entry_val)
            elif "delete" in self.message:
                if isinstance(str(entry_val[0]), str) and str(entry_val[0]) != "":
                    fg_color = info_c[0]
                    labelTeaxt = info_c[1]
                    print(labelTeaxt)
                    self.destroy()
                    pab(self.root).button_query(0, 3, entry_val)
            elif "print" in self.message:
                if (
                    isinstance(str(entry_val[0]), str)
                    and str(entry_val[0]) != ""
                    and str(entry_val[1]) != ""
                ):
                    fg_color = info_c[0]
                    labelTeaxt = info_c[1]
                    print(labelTeaxt)
                    self.destroy()
                    pab(self.root).button_query(0, 4, entry_val)
            else:
                fg_color = info_c[2]
                labelTeaxt = info_c[3]
                print(labelTeaxt)
        except Exception as err:
            fg_color = info_c[4]
            labelTeaxt = info_c[5]
            print(f"manipulating error: {err}")
            print(labelTeaxt)

            labels = tk.Label(
                self,
                text=labelTeaxt,
                anchor="w",
                bg="#BAD0EF",
                fg=fg_color,
                font=("Times", 10),
            )
            labels.place(x=20, y=360, width=560, height=30)
