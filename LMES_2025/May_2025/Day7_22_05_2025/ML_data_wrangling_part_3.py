import pandas as pd

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")

category_data = df['cut'].unique()
print(category_data)

df['cut'] = df['cut'].map({'Fair': 1, 'Good': 2, 'Very Good': 3, 'Ideal': 4, 'Premium': 5})
print(df.head(10))