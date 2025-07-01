import pandas as pd

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)

# for x in df.columns:
#     if df[x].dtype == "O":
#         print(x, "\t| Object")
#     else:
#         print(x, "\t| Numeric")

# Choose LabelEncoder for Nominal data.
# Nominal data doesn't naturally have a ranking, or follow a natural order.
# E.g., Red, Green, Blue - 1, 2, 3

"""pip install scikit-learn"""
from sklearn.preprocessing import LabelEncoder # Go for LabelEncoder if we are performing feature engineering
label_object = LabelEncoder()

df['color'] = label_object.fit_transform(df['color'])
print(df.head(10))
