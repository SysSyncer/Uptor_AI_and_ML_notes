import pandas as pd

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")
print(df.head())

encoded_data = pd.get_dummies(df['cut'])
print(encoded_data)

final_df = pd.concat([df, encoded_data], axis=1)
final_df.drop('cut', axis=1, inplace=True)
print(final_df)