import unicodedata

def remove_accent(text):
    try:
        text = unicode(text, "utf-8")
    except NameError:
        pass
    text = unicodedata.normalize("NFD", text).encode(
        "ascii", "ignore").decode("utf-8")
    return str(text)


def old_date(df2):
    mindate = df2["Last Check-In Date"].min()
    df2["Last Check-In Date"] = df2["Last Check-In Date"].dt.strftime(
        "%Y-%m-%d"
    )
    mindate = mindate.to_pydatetime()
    mindate = mindate.strftime("%Y-%m-%d")
    query = df2["Last Check-In Date"] == mindate
    query = df2.loc[query]
    return query


def recent_date(df2):
    maxdate = df2["Last Check-In Date"].max()
    df2["Last Check-In Date"] = df2["Last Check-In Date"].dt.strftime(
        "%Y-%m-%d"
    )
    maxdate = maxdate.to_pydatetime()
    maxdate = maxdate.strftime("%Y-%m-%d")
    query = df2["Last Check-In Date"] == maxdate
    query = df2.loc[query]
    return query


def sort_customers(df2):
    customer_list = []
    df2["Full Name"] = df2["First Name"] + " " + df2["Last Name"]
    list = df2["Full Name"].values.tolist()
    for x in list:
        x = remove_accent(x)
        customer_list.append(x)
    customer_list.sort()
    return customer_list
