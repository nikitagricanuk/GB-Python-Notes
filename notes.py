from random import randint as rint
from datetime import date

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
    id = new_id()
    #        id    created         edited  title    body
    data = f"{id};{date.today()};{None};{title};{body}\n"
    with open('db.csv', 'a') as f:
        f.write(data)
        f.close()
    
def del_note(id):
    with open('db.csv', 'r') as f:
        lines = f.readlines()
        f.close()
    with open('file.txt', 'w') as f:
        for line in lines:
            if not line.startswith(str(id)):
                f.write(line)
