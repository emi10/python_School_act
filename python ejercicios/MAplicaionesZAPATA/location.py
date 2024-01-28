import sqlite3

conn1 = sqlite3.connect('user_Data.db')
cursor1 = conn1.cursor()

cursor1.execute("SELECT * FROM users")
user_data = cursor1.fetchall()
print("Información de user_Data.db:")
for row in user_data:
    print(row)

conn1.close()

conn2 = sqlite3.connect('notifications.db')
cursor2 = conn2.cursor()

cursor2.execute("SELECT * FROM notifications")
notifications_data = cursor2.fetchall()
print("\nInformación de notifications.db:")
for row in notifications_data:
    print(row)

conn2.close()


conn3 = sqlite3.connect('carts.db')
cursor3 = conn3.cursor()

cursor3.execute("SELECT * FROM shopping_carts")
carts_data = cursor3.fetchall()
print("\nInformación de carts.db:")
for row in carts_data:
    print(row)

conn3.close()