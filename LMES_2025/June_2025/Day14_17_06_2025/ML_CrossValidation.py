import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

data = {
    "year": [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    "price": [100,200,300,400,500,600,700,800,900,1000,1100],
    "purchased": [1,0,1,0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

x = df[["year", "price"]]
y = df["purchased"]
print(x)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression()
cross_validation_score = cross_val_score(model, x, y, cv=5, scoring="accuracy")
print(cross_validation_score)