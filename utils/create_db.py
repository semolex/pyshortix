""" Creates `SQLite` database file and required table for usage with default controller."""

from config import DEFAULT_DB_NAME, DEFAULT_DB_PATH
import sqlite3


conn = sqlite3.connect(DEFAULT_DB_PATH + DEFAULT_DB_NAME)
conn.execute('''CREATE TABLE urls (short_part text, full_url text)''')
