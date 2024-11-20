#!/bin/python3

import uuid
import datetime

def get_file_name():
    note_date = str(datetime.date.today())
    note_id = str(uuid.uuid4())
    return f"./notes/{note_id.replace('-', '')}_{note_date.replace('-', '_')}.txt"

def clear_file():
    file = open('./note.txt', 'w')
    file.write("")
    file.close()


note_file = open('./note.txt', 'r+')
note_file_content = note_file.read()
note_file.close()

schedule_file = open(get_file_name(), 'w')
schedule_file.write(note_file_content)
schedule_file.close()

clear_file()