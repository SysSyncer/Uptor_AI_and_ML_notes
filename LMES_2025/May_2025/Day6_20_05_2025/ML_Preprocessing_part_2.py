import pandas as pd

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")
print(df.head())

finding_null_count = df.isna().sum()
print(finding_null_count)

df.drop("Unnamed: 0", axis=1, inplace=True)
print(df.head())

df.drop(["carat", "cut"], axis=1, inplace=True)
print(df.head())

"""
axis=1 - This is basically to remove on column wise.
inplace=True - This is basically like save rather than creating and returning a new updated copy.
(Ensuring removal happened properly)
"""
