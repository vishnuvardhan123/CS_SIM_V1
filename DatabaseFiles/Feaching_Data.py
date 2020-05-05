import sqlite3


def login_data():
    connection = sqlite3.connect('login.db')

    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Username : ", data[0])
        print("Password : ", data[1])




login_data()
