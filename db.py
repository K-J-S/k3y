import sqlite3

PATH = "sqlite:///var/www/k3y/db/tpc.db"


def get_data(request):
    try:
        # Creates or opens a file called mydb with a SQLite3 DB
        db = sqlite3.connect(PATH)
        print("connected")
        # Get a cursor object
        cursor = db.cursor()
        # Check if table users does not exist and create it
        cursor.execute(request)
        data = cursor.fetchall()

    # Catch the exception
    except Exception as e:
        print('{0}'.format(e))
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
    finally:
        # Close the db connection
        db.close()

    return data
