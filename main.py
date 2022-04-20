from tabulate import tabulate
from lib.preprocessing import preprocessing

route = "files/Sample test file - Sheet1.csv"

df2 = preprocessing(route)
print(tabulate(df2, headers="keys", tablefmt="psql"))