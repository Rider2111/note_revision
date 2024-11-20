#!/bin/python3

import os
import datetime

note_file_names = os.listdir("./notes")
data = {}
primary = 0
secondary = 1

def revise_note(revision_note_id: list):
    for note_file_name in note_file_names:
        note_id, _ = note_file_name.split('_',1)
        if note_id in revision_note_id:
            read_note = open(f'./notes/{note_file_name}')
            print(f'{note_file_name}\n')
            print(read_note.read())
            print("\n*********************************************\n")
            

for note_file_name in note_file_names:
    note_id, note_date = note_file_name.split('_',1)
    note_date = note_date.replace('.txt','')
    note_date = datetime.datetime.strptime(note_date,"%Y_%m_%d").date()
    data[note_id] = note_date

def get_next_fibinacco():
    global primary
    global secondary
    temp = primary
    primary = secondary
    secondary = secondary + temp
    return secondary

revision_note_ids = []

def update_data(note_dict: dict):
    updated_data = {}
    for key, value in note_dict.items():
        if value == datetime.date.today():
            revision_note_ids.append(key)
        elif value < datetime.date.today():
            updated_data[key] = value
    return updated_data

while len(data) != 0:
    n = get_next_fibinacco()
    for note_id, note_date in data.items():
        note_date = note_date + datetime.timedelta(days=n)
        data[note_id] = note_date
    data = update_data(data)

revise_note(revision_note_ids)