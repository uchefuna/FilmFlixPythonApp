# Python App Tkinter GUI
# Designed by Uche Ezike


from filmflixtmx import *
from TkAppPrintAllRecords import *
import webbrowser


class PythonAppBox:
    def __init__(self, root):
        self.root = root

    def tk_interface(self):
        # setting title
        self.root.title("Python App Interface")
        # setting window size
        width, height = 550, 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.win_x)

        frame1 = tk.Frame(master=self.root, width=width, height=height)
        frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.create_layout(6, 0)

    def win_x(self):
        close_conn()
        self.root.destroy()
        sys.exit("you cancelled the program. Refresh the browser to restart the app")

    def create_layout(self, z, j):
        labelTeaxt = [
            "Github",
            "unezike@gmail.com / 07960450962",
            "LinkedIn",
            "FilmFlix Python App with database",
            "Python SQL Project - Just IT Software Development Bootcamp Final Project",
            "A user GUI to manipulate SQL database using python",
            "Designed by Uchefuna Ezike",
        ]

        cur, fnt, fntn, fgc, und = "", "Times", 10, "#333333", ""
        label_acc_details = []
        for _ in range(len(labelTeaxt)):
            if "FilmFlix" in labelTeaxt[_]:
                fnt, fntn = "Arial", 20
            elif "Github" == labelTeaxt[_] or "LinkedIn" == labelTeaxt[_]:
                cur, fgc, und = "hand2", "blue", "underline"
            label_acc_details.append(
                tk.Label(
                    self.root,
                    justify="center",
                    fg=fgc,
                    cursor=cur,
                    text=labelTeaxt[_],
                    font=f"{fnt} {fntn} {und}",
                )
            )
            cur, fnt, fntn, fgc, und = "", "Times", 10, "#333333", ""

        label_acc_details[0].bind(
            "<Enter>", lambda e: label_acc_details[0].configure(fg="red")
        )
        label_acc_details[0].bind(
            "<Leave>", lambda e: label_acc_details[0].configure(fg="blue")
        )
        label_acc_details[0].bind("<Button-1>", self.acc_github)
        label_acc_details[0].place(x=10, y=10, width=70, height=20)

        label_acc_details[1].bind(
            "<Enter>", lambda e: label_acc_details[1].configure(fg="orange")
        )
        label_acc_details[1].bind(
            "<Leave>", lambda e: label_acc_details[1].configure(fg="black")
        )
        label_acc_details[1].place(x=90, y=10, width=350, height=20)

        label_acc_details[2].bind(
            "<Enter>", lambda e: label_acc_details[2].configure(fg="red")
        )
        label_acc_details[2].bind(
            "<Leave>", lambda e: label_acc_details[2].configure(fg="blue")
        )
        label_acc_details[2].bind("<Button-1>", self.acc_linkedin)
        label_acc_details[2].place(x=470, y=10, width=70, height=20)

        label_acc_details[3].place(x=10, y=40, width=500, height=50)

        # footer ------------------------------------------
        label_acc_details[4].place(x=0, y=420, width=530, height=20)

        label_acc_details[5].place(x=0, y=440, width=530, height=20)

        label_acc_details[6].place(x=0, y=470, width=530, height=20)
        # -------------------------------------------------

        labelTeaxt = [
            "Print ALL",
            "INSERT",
            "UPDATE",
            "DELETE",
            "PRINT",
            "EXIT",
            "Print all records on the table",
            "Add a record to  the table",
            "Amend a record to the table",
            "Delete a record from the table",
            "Specify a movie to print",
            "Exit program and go back to main menu",
        ]

        for _ in range(z):
            tk.Button(
                self.root,
                bd=3,
                bg="#f0f0f0",
                cursor="hand2",
                fg="#000000",
                text=labelTeaxt[_],
                font=("Times", 12),
                command=lambda e=_: self.button_query(e),
            ).place(x=20, y=100 + j, width=100, height=30)

            tk.Label(
                self.root,
                anchor="w",
                fg="#333333",
                text=labelTeaxt[_ + 6],
                font=("Times", 12),
            ).place(x=150, y=100 + j, width=400, height=30)
            j += 50

    def acc_github(self, event=None):
        webbrowser.open_new("https://github.com/uchefuna")
        print("Github account")

    def acc_linkedin(self, event=None):
        webbrowser.open_new("https://www.linkedin.com/in/unezike")
        print("LinkedIn account")

    def button_query(self, e, i=0, v=[]):
        from ManipulateQuery import InsertQuery

        p_list = [
            "Python SQL App",
            "600x550",
            "Enter details you want to insert to the Flimflix table: ",
            "600x420",
            "Enter details you want to update to the Flimflix table: ",
            "720x400",
            "Specify the movie you want to delete from the Flimflix table: ",
            "600x300",
            "Specify the movie you want to print from the Flimflix table: ",
        ]

        try:
            row = 0
            if e == 0:
                print("print ALL")
                if i == 0:
                    row = printall_query()
                    if row == 0:
                        row = "Error printing all records from the table"
                elif i == 1:
                    row = insert_query(v)
                    if row == 1:
                        row = printall_query()
                    else:
                        row = "Error inserting record to the table"
                elif i == 2:
                    row = update_query(v)
                    if row == 1:
                        row = printall_query()
                    else:
                        row = "Error updating record to the table"
                elif i == 3:
                    row = delete_query(v)
                    if row == 1:
                        row = printall_query()
                    else:
                        row = "Error deleting record to the table"
                elif i == 4:
                    row = print_query(v)
                    if row == 0:
                        row = "Error printing a record from the table"
                PrintAllRecordGUI(self.root, 0, p_list[0], row, p_list[1])
            elif e == 1:
                InsertQuery(self.root, 1, p_list[0], p_list[2], p_list[3])
                print("insert query")
            elif e == 2:
                InsertQuery(self.root, 2, p_list[0], p_list[4], p_list[5])
                print("update query")
            elif e == 3:
                InsertQuery(self.root, 3, p_list[0], p_list[6], p_list[7])
                print("delete query")
            elif e == 4:
                InsertQuery(self.root, 4, p_list[0], p_list[8], p_list[7])
                print("print query")
            elif e == 5:
                # close_conn()
                self.root.destroy()
                print("exit program, going to main menu")
                tme.sleep(2)
                main_func() # exit program and go to main menu
        except Exception as err:
            print(f"main error: {err}")


def main_func():
    confirmed = False
    while not confirmed:
        print(
            "\n"
            + "FilmFlix Python App with database"
            + "\n"
            + "To manipulate and perform CRUD operation on the the FilmFlix database."
            + "\n"
            + "\n"
            + "MAIN MENU:"
            + "\n"
            + "Choose (1) to use the Tkinter user interface (GUI)."
            + "\n"
            + "Choose (2) to use the command line interface (CLI)."
            + "\n"
            + "\n"
            + "USE TKINTER USER GUI      (Enter 1)"
            + "\n"
            + "USE TERMINAL INTERFACE    (Enter 2)"
            + "\n"
        )

        tme.sleep(1)
        try:
            input_option = int(input(">>>>> Please enter a number: "))

            if verified(input_option, [1, 2]):
                confirmed = True
                tme.sleep(1)

                if input_option == 1:
                    root = tk.Tk()
                    app = PythonAppBox(root)
                    app.tk_interface()
                    root.mainloop()
                elif input_option == 2:
                    filmflix_tmx()
            else:
                print("Ooops! Please enter only number: (1 - 2): ")

        except ValueError:
            print("Oi! You can only enter number: (1 - 2) ")
        finally:
            tme.sleep(1)


if __name__ == "__main__":
    main_func()
