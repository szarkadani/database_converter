import mysql.connector
import configparser
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = os.path.join(SCRIPT_DIR, '../config.ini')


class DatabaseConnectionManager:
    def __enter__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.conn = mysql.connector.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password'],
            database=config['Database']['database']
        )

        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()
