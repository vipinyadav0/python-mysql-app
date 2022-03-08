import mysql.connector
import re

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "adminadmin"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

found = False

for db in cursor:
    pattern = "[(,')]"
    db_string = re.sub(pattern, "", str(db))

    if (db_string == 'vocab'):
        found = True
        print('Database vocab exists')

if (not found):
    cursor.execute('CREATE DATABASE vocab')

fh = open("Vocabulary_list.csv", "r")

wd_list = fh.readlines()

wd_list.pop(0)

vocab_list = []

for rawstring in wd_list:
    word, definition = rawstring.split(',', 1)

    definition = definition.rstrip()

    vocab_list.append({word, definition})

# print(vocab_list)