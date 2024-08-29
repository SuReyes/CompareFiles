import unittest
import pandas as pd
import sqlite3  # You can replace this with another database library if needed

from infrastructure.BreedRepository import get_breed_data


def read_excel(file_path):
    """Read data from an Excel file into a DataFrame."""
    reader = pd.DataFrame
    return reader.read_excel(file_path)


#def fetch_data_from_db(db_connection_str, query):
    """Fetch data from the database into a DataFrame."""
    #with sqlite3.connect(db_connection_str) as conn:
    #return pd.read_sql_query(query, conn)


def compare_data(excel_df, db_df):
    """Compare two DataFrames and return the differences."""
    # Assuming both DataFrames have the same structure and columns
    differences = excel_df.compare(db_df)
    return differences


class TestCompareBreeds(unittest.TestCase):

    def test_get_breeds(self):
        # Paths and connection details
        excel_file_path = 'tests/CKC Breed Colours.xlsx'
        #db_connection_str = 'path_to_your_database.db'  # Update as needed
        query = get_breed_data()

        # Read data
        excel_df = read_excel(excel_file_path)
        db_df = query

        # Compare data
        differences = compare_data(excel_df, db_df)

        # Output differences
        if not differences.empty:
            print("Differences found:")
            print(differences)
        else:
            print("No differences found.")
