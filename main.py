import os
from tabulate import tabulate
from art import *
from lib.preprocessing import preprocessing
import pandas as pd
from lib.queries import old_date, recent_date, sort_customers

df = pd.DataFrame()


def browse_files():

    path = "files/"
    frames = []
    i = 0
    with os.scandir(path) as files:
        for file in files:
            frames.append(file.name)
    return frames


######################
### Menú principal ###
######################

while True:
    os.system("cls")
    tprint("Sample Test")
    list = browse_files()
    df["Files"] = list
    df.index.name = "Id"
    print(tabulate(df, headers="keys", tablefmt="psql"))
    try:
        id = int(input("\nChoose an Id to select a csv file: "))
    except:
        input("\nEnter a valid choice. Press key to continue...")
        os.system("cls")
        continue

    if id <= len(df.index) - 1:
        os.system("cls")
        query = df.query("Id == " + str(id))
        filename = query["Files"].values[0]
        route = "files/" + filename
        df2 = preprocessing(route)

        if df2 is None:
            print("No data in file")
            input("\nPress Enter to return...")

        else:
            while True:
                print("File selected: " + filename)
                print("\n(q) - Show the dataframe preprocessed")
                print("(w) - Customer with the oldest check in date")
                print("(a) - Customer with the most recent check in date")
                print("(s) - List of customers sorted alphabetically")
                print("(e) - Return to select another file\n")

                key = str(input("Press the key to select your query: "))

                if key == "q":
                    os.system("cls")
                    print(tabulate(df2, headers="keys", tablefmt="psql"))
                    input("Press Enter to return...")
                    os.system("cls")

                elif key == "w":
                    os.system("cls")

                    df2 = preprocessing(route)
                    query = old_date(df2)
                    print(
                        "Full Name: "
                        + query["First Name"].values[0]
                        + " "
                        + query["Last Name"].values[0]
                        + "\nLast Check-In Date: "
                        + query["Last Check-In Date"].values[0]
                    )

                    input("\nPress Enter to return...")
                    os.system("cls")

                elif key == "a":
                    os.system("cls")

                    df2 = preprocessing(route)
                    query = recent_date(df2)
                    print(
                        "Full Name: "
                        + query["First Name"].values[0]
                        + " "
                        + query["Last Name"].values[0]
                        + "\nLast Check-In Date: "
                        + query["Last Check-In Date"].values[0]
                    )

                    input("\nPress Enter to return...")
                    os.system("cls")
                elif key == "s":
                    os.system("cls")

                    df2 = preprocessing(route)
                    list = sort_customers(df2)
                    print(list)

                    input("\nPress Enter to return...")
                    os.system("cls")

                elif key == "e":
                    os.system("cls")
                    break

                else:
                    os.system("cls")
                    print("\nUnexpected input.")
                    input("\nPress Enter to return...")
                    os.system("cls")
    else:
        os.system("cls")
        print("Id not found")
        input("Press Enter to return...")
