"""Module for working with database"""

import sqlite3
import os


def __check_table_exists():
    if not os.path.exists(os.getcwd() + '/urls.db'):
        raise Exception("Error: There's no urls.db file")

    command = """
    CREATE TABLE "URLS" (
	"short"	VARCHAR(16) UNIQUE,
	"full"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("short")
    )
    """

    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(command)
        except sqlite3.OperationalError:
            pass


def __execute_command(command: str, params: tuple):
    __check_table_exists()

    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            cursor.execute(command, params)

            result = cursor.fetchone()

            if result is None:
                return None

            return result
    except Exception as e:
        print(f"Got exception: {e}")
        return None


def get_url(code):
    """Gets url from database by it's code"""
    command = """SELECT full FROM urls WHERE short=?;"""

    result = __execute_command(command, (code,))

    if result is None:
        return None
    return result[0]


def add_url(code, url):
    """Adds pair (code, url) to database"""
    command = """INSERT INTO urls (short, full) VALUES (?, ?);"""

    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            cursor.execute(command, (code, url,))
        return True
    except Exception as e:
        print(f"Got exception: {e}")
        return None


def try_get_code(url):
    """Returns code of URL if exists in database, else None"""
    command = """SELECT short FROM urls WHERE full=?;"""
    result = __execute_command(command, (url,))

    if result is None:
        return None
    return result[0]
