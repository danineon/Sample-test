import pandas as pd
def preprocessing(route):
    # Read the csv and transform to dataframe
    try:
        df = pd.read_csv(route, encoding="utf8")
    except:
        return
    # Remove all rows containing NaN in all columns
    df = df.dropna(how="all")

    # Reset index after removing all rows containing NaN in all columns and set name index
    df.reset_index(inplace=True, drop=True)
    df.index.name = "Id"

    # Change de date column "string" to "datetime64" and reformat the date column
    df["Last Check-In Date"] = pd.to_datetime(
        df["Last Check-In Date"], infer_datetime_format=True
    )

    # Remove spaces from the "Phone" column
    df["Phone"] = df["Phone"].str.replace(" ", "")

    return df