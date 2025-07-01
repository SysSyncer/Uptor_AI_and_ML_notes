# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd
#
# df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")
#
# one_hot_encoder = OneHotEncoder(sparse_output=False)
#
# cut_encoded = one_hot_encoder.fit_transform(df[['cut']])
# cut_encoded_df = pd.DataFrame(cut_encoded, columns=one_hot_encoder.get_feature_names_out(['cut']))
# df = df.reset_index(drop=True)
# cut_encoded_df = cut_encoded_df.reset_index(drop=True)
# df = pd.concat([df.drop('cut', axis=1), cut_encoded_df], axis=1)
# print(df.head())

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("../../Dataset/Diamonds/diamonds.csv")

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoding_data = one_hot_encoder.fit_transform(df[['cut']])

new_df = pd.DataFrame(encoding_data, columns=one_hot_encoder.get_feature_names_out(['cut']))
final_df = pd.concat([df.drop("Unnamed: 0", axis=1), new_df], axis=1)
print(final_df)