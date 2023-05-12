# FilmFlix Python App with database using sqlite3


import sqlite3 as sql  # import sqlite3 module


# mySQL connector to the database filmflix.db
try:
    with sql.connect("filmflix.db") as conn:
    # with sql.connect(
    #     "C:/Users/Glow/OneDrive/JustIT/Python/Python Classes/Python Project/Python Worksheets Py/FlimFlixPythonApp/filmflix.db"
    # ) as conn:
        _mycursor = conn.cursor()
except sql.OperationalError as err:
    print(f"Connection error: '{err}'")
else:
    print("Database connection successful")


# query to insert data
def insert_query(param):
    try:
        print(param)
        tsql = f"INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES ({param[0]}, '{param[1].title()}', {param[2]}, '{param[3].upper()}', {param[4]}, '{param[5].title()}');"
        _mycursor.execute(tsql)
    except sql.OperationalError as err:
        conn.rollback()
        print(f"insert error: '{err}'")
        return 0
    else:
        conn.commit()
        print("queries executed and committed")
        return 1


# query to update data
def update_query(param):
    try:
        tsql = f"UPDATE tblFilms SET {param[0]} = ('{param[1].title()}') WHERE UPPER({param[2]}) LIKE UPPER('%{param[3]}%');"
        _mycursor.execute(tsql)
    except sql.OperationalError as err:
        conn.rollback()
        print(f"update error: '{err}'")
        return 0
    else:
        conn.commit()
        print("queries executed and committed")
        return 1


# query to delete data
def delete_query(param):
    try:
        tsql = (
            f"DELETE FROM tblFilms WHERE UPPER({param[0]}) LIKE UPPER('%{param[1]}%');"
        )
        _mycursor.execute(tsql)
    except sql.OperationalError as err:
        conn.rollback()
        print(f"delete error: '{err}'")
        return 0
    else:
        conn.commit()
        print("queries executed and committed")
        return 1


# Read all records from the table tblfilms where?
def print_query(param):
    try:
        print(f"param[0] = {param[0].upper()}  param[1] = {param[1].upper()}")

        print_all = []
        tsql = f"SELECT * FROM tblFilms WHERE UPPER({param[0]}) LIKE UPPER('%{param[1]}%');"
        print("\nReading data from table:")
        for row in _mycursor.execute(tsql):
            print_all.append(row)
    except sql.OperationalError as err:
        print(f"print error: '{err}'")
        return 0
    else:
        return print_all


# Read all record from the table tblfilms
def printall_query():
    try:
        print_all = []
        print("\nReading data from table:")
        tsql = "SELECT * FROM tblFilms;"
        for row in _mycursor.execute(tsql):
            print_all.append(row)
    except sql.OperationalError as err:
        print(f"print all error: '{err}'")
        return 0
    else:
        return print_all


def close_conn():
    conn.close()
    print("Server connection closed.")


if __name__ == "__main__":
    pass
