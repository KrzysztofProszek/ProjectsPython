import sqlite3

# conn = sqlite3.connect('sqlDB.db')
# c = conn.cursor()
# c.execute('CREATE TABLE stocks(date date, trans text, symbol text, qty real, price real)')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# conn.close()
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t )
# print(c.fetchone())
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# conn.commit()


# -------------------------------CWICZENIA---------------------------------

# 1
# conn = sqlite3.connect(':memory:')
# conn.close()

# 2
# import sqlite3
# conn = sqlite3.connect('temp.db')
# c = conn.cursor()
# print("Baza danych stworzona i połczona z SQLite.")
# c.execute("SELECT sqlite_version();")
# record = c.fetchall()
# print("Wersja bazy danych SQLite to: ", record)
# print("Wersja modułu sqlite3 to: ", sqlite3.version)
# conn.close()
# print("Połczenie SQLite jest zamknięte.")

# 3
# conn = sqlite3.connect(':memory:')
# try:
#     c = conn.cursor()
#     c.execute('SELECT * FROM users')
#     conn.close()
# except sqlite3.Error:
#     print('Problem z operacja na bazie danych')

# 4
# try:
#     conn = sqlite3.connect('CodeBrainers.db')
#     c = conn.cursor()
#     tbl_names = ['Customer', 'Order_product', 'Product']
#     for tbl in tbl_names:
#         c.execute(f'SELECT * FROM {tbl}')
#         print(c.fetchall())
# except:
#     print('problem z operacja na bazie danych')
# else:
#     conn.close()

# 5
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE users(login VARCHAR(8) NOT NULL, name VARCHAR(40) NOT NULL, phone_no VARCHAR(15)')
c.execute("INSERT INTO users VALUES ('user', 'Jan Nowak', '1234567890')")
c.execute('SELECT * FROM users')
print(c.fetchall())
conn.close()
