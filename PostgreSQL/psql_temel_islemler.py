#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user = "test_u", password = "test_u", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")



# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# print ("Table created successfully")

# conn.commit()
# conn.close()

INS1 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )"
INS2 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
INS3 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
INS4 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"

cur = conn.cursor()
for INSERT in INS1, INS2, INS3, INS4:
    try:
        cur.execute(INSERT)
        conn.commit()
        print ("Records created successfully")
    except psycopg2.errors.UniqueViolation:
        print(INSERT,"HATA...")
    continue
conn.close()


# cur = conn.cursor()

# cur.execute("SELECT id, name, address, salary  from COMPANY")
# rows = cur.fetchall()
# for row in rows:
#    print ("ROW:", row)
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#    print ("SALARY = ", row[3], "\n")

# print ("Operation done successfully")
# conn.close()


# cur = conn.cursor()
# print ("1-Total number of rows deleted :", cur.rowcount)
# cur.execute("DELETE from COMPANY where ID=1 and ID=3;")
# conn.commit()
# print ("2-Total number of rows deleted :", cur.rowcount)

# cur.execute("SELECT id, name, address, salary  from COMPANY")
# rows = cur.fetchall()
# for row in rows:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#    print ("SALARY = ", row[3], "\n")

# print ("Operation done successfully")
# conn.close()