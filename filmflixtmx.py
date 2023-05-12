from mysqlCRUD import *
import time as tme
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
    except Exception:
        return False


def manipInsert(i=0, j=0):
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
        + "You should provided the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            insert_opt = input(f">>> {tbl_col_val[i]}: ")
            insert_opt_list.append(insert_opt)
            print(f"List of record to insert: {insert_opt_list}")
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
                    print("insert all good")
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
    tbl_col_val = ["UPDATE tblfilms SET", "=", "WHERE", "="]

    update_opt_list = []
    update_opt = ""

    print(
        "Enter column and value you want to update in FlimFlix table"
        + "\n"
        + "You should provided the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            update_opt = input(f">>> {tbl_col_val[i]}: ")
            update_opt_list.append(update_opt)
            print(f"Record to update: {update_opt_list}")
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
                    print("update all good")
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
    tbl_col_val = ["DELETE FROM tblfilms WHERE", "="]

    delete_opt_list = []
    delete_opt = ""

    print(
        "Enter column and value you want to delete in FlimFlix table"
        + "\n"
        + "You should provided the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            delete_opt = input(f">>> {tbl_col_val[i]}: ")
            delete_opt_list.append(delete_opt)
            print(f"Record to delete: {delete_opt_list}")
            i += 1
            tme.sleep(1)

        try:
            if isinstance(str(delete_opt_list[0]), str) and delete_opt != "":
                dee = delete_query(delete_opt_list)
                if dee == 1:
                    print("delete all good")
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
    tbl_col_val = ["SELECT * FROM tblfilms WHERE", "="]

    print_opt_list = []
    print_opt = ""

    print(
        "Enter column and value you want to delete in FlimFlix table"
        + "\n"
        + "You should provided the correct recrods accordingly with the datatype"
    )

    while j < 5:
        while i < len(tbl_col_val):
            print_opt = input(f">>> {tbl_col_val[i]}: ")
            print_opt_list.append(print_opt)
            print(f"Record to delete: {print_opt_list}")
            i += 1
            tme.sleep(1)

        try:
            if isinstance(str(print_opt_list[0]), str) and print_opt != "":
                dee = print_query(print_opt_list)
                if dee == 0:
                    raise ValueError("error raised")
                else:
                    print("print all good")
                    return dee
        except ValueError:
            print("Values or datatype incorrect. Plase try again" + "\n")
            print_opt_list = []
            i, j = 0, j + 1
            if j == 5:
                print("Tried 5x. Please start all over")
                break


def filmflix_tmx():
    while True:
        print(
            "\n"
            + "PRINT ALL (Option 1): "
            + "\n"
            + "INSERT    (Option 2): "
            + "\n"
            + "UPDATE    (Option 3): "
            + "\n"
            + "DELETE    (Option 4): "
            + "\n"
            + "PRINT     (Option 5): "
            + "\n"
            + "EXIT      (Option 6): "
            + "\n"
        )

        try:
            input_option = int(input(">>> Please enter a number: "))

            confirmed = False
            while not confirmed:
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
                        sys.exit("you cancelled the program")
                else:
                    print("Ooops! Please enter only number (1 - 6): ")
                    break

        except ValueError as err:
            print("Oi! You can only enter numbers: ")
        except Exception as err:
            print("Oi! You can only enter numbers: ")
        finally:
            tme.sleep(1)


# ---------------------------------------------
