import sqlite3
# создаём базу данных

conn = sqlite3.connect('name.db')
# создаём объект cursor, который позволяет нам взаимодействовать
cursor = conn.cursor()
#
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#
# # cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# #
# conn.commit()
#
# d = 'red'
# f = 'black'
# # cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES(?,?)''',(d,f))
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# #
# cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# conn.commit()
# cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
t = 4
cursor.execute('''UPDATE tab_1 SET col_1 = 'world' WHERE id = ?''',(t,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)