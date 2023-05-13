from mysqlCRUD import *
import time as tme
import msvcrt as msv
import sys


# ------------------------------------------------


def verified(sel, selction):
    try:
        if sel in selction:
            return True
        else:
            return False
    except ValueError:
        return False


def manipInsert(i=0, j=0):
    global get_out_loop
    tbl_col_val = [
        "filmID(integer)",
        "title(text)",
        "yearReleased(integer)",
        "rating(text)",
        "duration(integer)",
        "genre(text)",
    ]

    insert_opt_list = []
    insert_opt = ""

    print(
        "Enter value you want to insert to FlimFlix table"
        + "\n"
        + "You should provide the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            insert_opt = input(f">>> {tbl_col_val[i]}: ")
            if insert_opt != "?":
                insert_opt_list.append(insert_opt)
                print(f"Record to be added to the table: {insert_opt_list}")
            else:
                print('Now press ESC')
                if msv.getch() == chr(27).encode():
                    get_out_loop,j = True,5
                    print(j)
                    break
            i += 1
            tme.sleep(1)

        try:
            if (
                isinstance(int(insert_opt_list[0]), int)
                and isinstance(str(insert_opt_list[1]), str)
                and isinstance(int(insert_opt_list[2]), int)
                and isinstance(str(insert_opt_list[3]), str)
                and isinstance(int(insert_opt_list[4]), int)
                and isinstance(str(insert_opt_list[5]), str)
                and insert_opt != ""
            ):
                ins = insert_query(insert_opt_list)
                if ins == 1:
                    print("Record added to the table")
                    return
                else:
                    raise ValueError("error raised")
        except ValueError:
            print("Values or datatype incorrect. Plase try again" + "\n")
            insert_opt_list = []
            i, j = 0, j + 1
            if j == 5:
                print("Tried 5x. Please start all over")
                break


def manipUpdate(i=0, j=0):
    global get_out_loop
    tbl_col_val = ["UPDATE tblfilms SET", "=", "WHERE", "="]

    update_opt_list = []
    update_opt = ""

    print(
        "Enter column name and value you want to update in FlimFlix table"
        + "\n"
        + "You should provide the correct recrods accordingly with the datatype"
    )

    print(j)
    while j < 5:
        while i < len(tbl_col_val):
            update_opt = input(f">>> {tbl_col_val[i]}: ")
            if update_opt != "?":
                update_opt_list.append(update_opt)
                print(f"Record to be amended in the table: {update_opt_list}")
            else:
                print('Now press ESC')
                if msv.getch() == chr(27).encode():
                    get_out_loop = True
                    print(j)
                    break
            i += 1
            tme.sleep(1)

        try:
            if (
                isinstance(str(update_opt_list[0]), str)
                and isinstance(str(update_opt_list[2]), str)
                and update_opt != ""
            ):
                upd = update_query(update_opt_list)
                if upd == 1:
                    print("Record updated in the table")
                    return
                else:
                    raise ValueError("error raised")
        except ValueError:
            print("Values or datatype incorrect. Plase try again" + "\n")
            update_opt_list = []
            i, j = 0, j + 1
            if j == 5:
                print("Tried 5x. Please start all over")
                break


def manipDelete(i=0, j=0):
    global get_out_loop
    tbl_col_val = ["DELETE FROM tblfilms WHERE", "="]

    delete_opt_list = []
    delete_opt = ""

    print(
        "Enter column and value you want to delete in FlimFlix table"
        + "\n"
        + "You should provide the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            delete_opt = input(f">>> {tbl_col_val[i]}: ")
            if delete_opt != "?":
                delete_opt_list.append(delete_opt)
                print(f"Record to be deleted from the table: {delete_opt_list}")
            else:
                print('Now press ESC')
                if msv.getch() == chr(27).encode():
                    get_out_loop = True
                    break
            i += 1
            tme.sleep(1)

        try:
            if isinstance(str(delete_opt_list[0]), str) and delete_opt != "":
                dee = delete_query(delete_opt_list)
                if dee == 1:
                    print("Record deleted from the table")
                    return
                else:
                    raise ValueError("error raised")
        except ValueError:
            print("Values or datatype incorrect. Plase try again" + "\n")
            delete_opt_list = []
            i, j = 0, j + 1
            if j == 5:
                print("Tried 5x. Please start all over")
                break


def manipPrint(i=0, j=0):
    global get_out_loop
    tbl_col_val = ["SELECT * FROM tblfilms WHERE", "="]

    print_opt_list = []
    print_opt = ""

    print(
        "Enter column and value you want to delete in FlimFlix table"
        + "\n"
        + "You should provide the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            print_opt = input(f">>> {tbl_col_val[i]}: ")
            if print_opt != "?":
                print_opt_list.append(print_opt)
                print(f"Record to be printed: {print_opt_list}")
            else:
                print('Now press ESC')
                if msv.getch() == chr(27).encode():
                    get_out_loop = True
                    break
            i += 1
            tme.sleep(1)

        try:
            if isinstance(str(print_opt_list[0]), str) and print_opt != "":
                dee = print_query(print_opt_list)
                if dee == 0:
                    raise ValueError("error raised")
                else:
                    print("record printed from the table")
                    return dee
        except ValueError:
            print("Values or datatype incorrect. Plase try again" + "\n")
            print_opt_list = []
            i, j = 0, j + 1
            if j == 5:
                print("Tried 5x. Please start all over")
                break


def filmflix_tmx():
    global get_out_loop
    get_out_loop = False
    print(f"get_out_loop0: {get_out_loop}")

    try:
        while True:
            print(
                "\n"
                + "PRINT ALL (Enter 1)"
                + "\n"
                + "INSERT    (Enter 2)"
                + "\n"
                + "UPDATE    (Enter 3)"
                + "\n"
                + "DELETE    (Enter 4)"
                + "\n"
                + "PRINT     (Enter 5)"
                + "\n"
                + "EXIT      (Enter 6)"
                + "\n"
                + "Use (PRINT ALL) when necessary to view the records on the table to have an idea of what to do."
                + "\n"
                + "Also you can use ['?'+'ENTER'+'ESC'] key combinations to go back to the main menu at any point"
                + "\n"
            )

            input_option = input(">>> Please enter a number: ")
            # print("\n")

            if input_option != "?":
                try:
                    confirmed = False
                    while not confirmed:
                        input_option = int(input_option)
                        if verified(input_option, [1, 2, 3, 4, 5, 6]):
                            confirmed = True

                            if input_option == 1:
                                rows = printall_query()
                                for row in rows:
                                    print(row)
                            elif input_option == 2:
                                manipInsert()
                            elif input_option == 3:
                                manipUpdate()
                            elif input_option == 4:
                                manipDelete()
                            elif input_option == 5:
                                rows = manipPrint()
                                for row in rows:
                                    print(row)
                            elif input_option == 6:
                                close_conn()
                                sys.exit(
                                    "you cancelled the program. Refresh the browser to restart the app"
                                )
                        else:
                            print("Ooops! Please enter only number: (1 - 6)")
                            break

                except ValueError:
                    print("Oi! You can only enter number: (1 - 6)")
                finally:
                    tme.sleep(1)
                    if get_out_loop == True:
                        raise Exception

            elif input_option == "?":
                print('Now press ESC')
                if msv.getch() == chr(27).encode():
                    raise Exception

    except Exception:
        from main import main_func

        print("exit program, going to main menu")
        tme.sleep(1)
        main_func()  # exit program and go to main menu
        # break


if __name__ == "__main__":
    pass


# ---------------------------------------------
