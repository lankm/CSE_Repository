# libraries used:
# pip install pandas openpyxl sqlite3
import os
import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3 as sqlite

default_database = "LibManageSys.sqlite"

def excel_to_sqlite(file_path, table_name, database_path=default_database):
    df = pd.read_excel(file_path, engine='openpyxl')
    db = sqlite.connect(database_path)
    df.to_sql(table_name, db, if_exists='append', index=False)
    db.close()

def importXLSXtoSQL():
    for file in os.listdir():
        if file.endswith('.xlsx'):
            excel_to_sqlite(file, file.split(".")[0].upper())


def run(sqlite_command, database_path=default_database):
    db = sqlite.connect(database_path)
    cursor = db.cursor()
    result = cursor.execute(sqlite_command).fetchall()
    db.commit()
    cursor.close()
    db.close()
    return result

def read(filename):
    buffer = ""
    outputs = []
    with open(filename) as file:
        for line in file:
            if(not line.startswith("--")):
                if(";" in line):
                    buffer += line[:line.index(";")]
                    print(buffer)
                    outputs.append(run(buffer))
                    buffer = ""
                else:
                    buffer += line + " "
    return outputs


def main():
    read("createTables.sql")
    importXLSXtoSQL() # Exports all .xlsx files to .csv using the pandas library and the openpyxl engine

    root = tk.Tk()
    root.geometry("400x400")
    root.title("Library Manager")

    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1,text="tab1")
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2,text="tab2")
    tabControl.pack()

    lab1 = tk.Label(tab1, text="Test")
    lab1.pack()

    root.mainloop()
    



if __name__ == "__main__":
    main()
