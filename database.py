import sqlite3

conn = sqlite3.connect('atrp.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE atrp(
        id integer PRIMARY KEY,
        name text ,
        age integer,
        email text
        
     )""")'''

c.execute("""INSERT INTO atrp VALUES(
        '1',
        'Jhon',
        '23',
        'jhon@email.com'

        )


""")

conn.commit()

conn.close()