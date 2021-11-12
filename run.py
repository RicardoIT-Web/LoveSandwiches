# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get Sales figures input from the user
    """
    print("Please enter sales data from the last Market.")
    print("Data should be six numbers, seperated by commas.")
    print("example: 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")
    #print(f"The data provided is {data_str}")

    sales_data = data_str.split(",")
    #print(sales_data)
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values int integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    #print(values)

    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()