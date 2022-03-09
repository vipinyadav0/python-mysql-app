import mysql.connector
import re

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "adminadmin",
    database = "vocab"

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

sql = "DROP TABLE IF EXISTS vocab_table"
cursor.execute(sql)

sql = "CREATE TABLE vocab_table(word VARCHAR(225), definition VARCHAR(255)"
cursor.execute(sql)


fh = open("Vocabulary_list.csv", "r")

wd_list = fh.readlines()

wd_list.pop(0)

vocab_list = []

for rawstring in wd_list:
    word, definition = rawstring.split(',', 1)

    definition = definition.rstrip()

    vocab_list.append({word, definition})

    sql = "INSERT INTO vocab_table(word, definition) VALUES(%s, %s)"

    values = (word,definition)
    cursor.execute(sql, values)

    conn.commit()
    print("Inserted " + str(cursor.rowcounts) + "row into vocab_table")


# Retrieving Data from the MySql Table using select query
sql = "SELECT * from vocab_table" 
cursor.execute(sql)

result = cursor.fetchall()
# Iterating through results set

for row in result:
    print(row)

sql = "SELECT * from vocab_table WHERE word = %s"

value = ('boisterous',)
cursor.execute(sql)

result = cursor.fetchall()
# Iterating through results set

for row in result:
    print(row)







# print(vocab_list) 


