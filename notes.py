from random import randint as rint
from datetime import date
from tabulate import tabulate

def new_id():
    id = rint(0, 99)
    try:
        f = open('db.csv', 'r')
        data = f.readlines()
        for line in data:
                if line.split(';')[0] == id:
                    new_id()
                else:
                    break
        f.close()
    except FileNotFoundError:
        id = 0
    return id

def add_note(title, body):
    if title == None and body == None:
        print("You must specify at least one argument! Exiting...")
        exit()
    
    id = new_id()
    #        id    created         edited  title    body
    data = f"{id};{date.today()};{None};{title};{body}\n"
    with open('db.csv', 'a') as f:
        f.write(data)
        f.close()
    
def del_note(id):
    if id == None:
        print("You must specify at least one argument! Exiting...")
        exit()
    
    with open('db.csv', 'r') as f:
        lines = f.readlines()
        f.close()
    with open('db.csv', 'w') as f:
        for line in lines:
            if not line.startswith(str(id)):
                f.write(line)

def read_note(id):
    if id == None:
        table_head = ["ID", "Created", "Edited", "Title", "Body"]
        table_data = []
        try:
            f = open('db.csv', 'r')
            data = f.readlines()
            for line in data:
                    tmp_data = [line.split(';')[0], 
                                line.split(';')[1], 
                                line.split(';')[2], 
                                line.split(';')[3], 
                                line.split(';')[4]]
                    table_data.append(tmp_data)
            f.close()
        except FileNotFoundError:
            print("Could not find database file.")
        print(tabulate(table_data, headers=table_head, tablefmt="grid"))

    else:
        try:
            f = open('db.csv', 'r')
            data = f.readlines()
            for line in data:
                    if line.split(';')[0] == id:
                        print(f"Title: \n\t{line.split(';')[3]}\n")
                        print(f"Body: \n\t{line.split(';')[4]}")
            f.close()
        except FileNotFoundError:
            print("Could not find database file.")

def edit_note(id):
    if id == None:
        print("You must specify at least one argument! Exiting...")
        exit()
    
    read_note(id)
    new_title = input("Please enter new title: ")
    new_body = input("Please enter new body: ")

    with open('db.csv', 'r') as f:
        lines = f.readlines()
        f.close()
    with open('db.csv', 'w') as f:
        for line in lines:
            if line.split(';')[0] != id:
                f.write(line)
            else:
                #                id                    created             edited        title       body
                new_line = f"{line.split(';')[0]};{line.split(';')[1]};{date.today()};{new_title};{new_body}\n"
                f.write(new_line)