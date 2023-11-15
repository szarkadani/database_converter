import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
EXPORTED_TABLES_DIR = os.path.join(SCRIPT_DIR, '../exported_tables')


def export_table_to_csv(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    if not os.path.exists(EXPORTED_TABLES_DIR):
        os.makedirs(EXPORTED_TABLES_DIR)

    with open(os.path.join(EXPORTED_TABLES_DIR, f'{table_name}.csv'), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(rows)
