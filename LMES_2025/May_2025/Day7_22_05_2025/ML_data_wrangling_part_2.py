import pandas as pd

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)

# for x in df.columns:
#     if df[x].dtype == "O":
#         print(x, "\t| Object")
#     else:
#         print(x, "\t| Numeric")

# Choose OrdinalEncoder for Ordinal data.
# Ordinal data follow a natural order and follows natural ranking.
# E.g., Small, Medium, Large - 1, 2, 3

"""pip install scikit-learn"""
from sklearn.preprocessing import OrdinalEncoder # Go for OrdinalEncoder if we are encoding a target data
label_object = OrdinalEncoder()

df['cut'] = label_object.fit_transform(df[['cut']])
print(df.head(10))
