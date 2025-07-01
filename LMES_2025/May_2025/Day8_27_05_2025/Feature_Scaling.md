# Feature Engineering
- It is the concept of doing and making some or more changes to the feature or inputs 
or independent data.

1. Feature Scaling
2. Feature Selection

# Feature Scaling
(Expanding certain numbers to specific range)
1. **MinMaxScaler():** Uniform distribution of data (Normalization)
2. **StandardScaler():** Normal distribution of data (Standardization)
- Process of converting one form of numeric into another form of numeric for better manipulation of data for the models.

| Player | Scores | MinMaxScaler() |
|--------|--------|----------------|
| Dhoni  | 10000  | 0.3            |
| Zaheer | 20     | 0.0            |
| Sachin | 30000  | 1.0            |
| Kohli  | 20000  | 0.6            |
| Kaif   | 5000   | 0.1            |

> Range can be from **0 to 1** (MinMaxScaler) (or) **-1 to 1** (Standard Scaler)