# Database Converter

## Overview

The Database Converter is a graphical application built in wxPython for exporting MySQL database tables to CSV files. It allows users to select specific tables for export, providing a convenient way to extract data from a MySQL database.

## Features

- Connects to a MySQL database using user-defined configurations.
- Displays available database tables in a grid for user selection.
- Supports exporting selected tables to CSV files.
- User-friendly graphical interface.

## Project Structure

The project is organized into the following components:

- **`csv_exporter.py`**: Contains the `export_table_to_csv` function for exporting a MySQL table to a CSV file.

- **`db_connector.py`**: Defines the `DatabaseConnectionManager` class, serving as a context manager for managing database connections and cursors.

- **`gui.py`**: Houses the `DatabaseConverter` class, responsible for creating the graphical user interface using wxPython.

- **`main.py`**: The main script to run the application.

## Requirements

- Python 3.9
- wxPython 4.2.1a
- MySQL Connector Python

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/szarkadani/database_converter
   cd database-converter
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Update the `config.ini` file with your MySQL database configuration.

## Usage

Run the application using the following command:

```bash
python main.py
```

- The application window will appear with a grid of available tables.
- Select tables for export by checking the corresponding checkboxes.
- Click the "Save" button to export the selected tables to CSV files in the `exported_tables` directory.

## Notes

- The `exported_tables` directory will be created automatically to store the exported CSV files.
- Ensure that the `config.ini` file contains accurate database configuration details.
