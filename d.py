import pandas as pd

csv = "csv/easyfood.csv"

data = pd.read_csv(csv)

print(data["상품코드"])