import pandas as pd

file_content = pd.read_csv("../../../Dataset/Diamonds/diamonds.csv")
print(file_content)

row_reading = file_content.head()
print(row_reading)