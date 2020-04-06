import sqlite3
import os


def __check_table_exists():
    if not os.path.exists(os.getcwd() + '/urls.db'):
        raise Exception("Error: There's no urls.db file")

    command = """
        CREATE TABLE URLS(
        short VARCHAR(16) PRIMARY KEY,
        full TEXT	NOT NULL
        );
        """
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(command)
        except sqlite3.OperationalError:
            pass


def get_url(code):
    command = """SELECT full FROM urls WHERE short=?;"""

    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            cursor.execute(command, (code,))

            result = cursor.fetchone()

            if result is None:
                return None

            return result[0]
    except Exception as e:
        print(f"Got exception: {e}")
        return None


def add_url(code, url):
    command = """INSERT INTO urls (short, full) VALUES (?, ?);"""

    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            cursor.execute(command, (code, url))
        return True
    except Exception as e:
        print(f"Got exception: {e}")
        return None
