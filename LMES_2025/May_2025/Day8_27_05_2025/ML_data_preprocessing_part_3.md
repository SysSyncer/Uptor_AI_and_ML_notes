### Conversion of Categorical data into numerical Data

#### 1.1 One Hot Encoding

| Name  | Runs  | Team |
|-------|-------|------|
| Dhoni | 10000 | CSK  |
| Kohli | 8000  | RCB  |
| Rohit | 9000  | MI   |

#### Label Encoding

| Name  | Runs  | Team |
|-------|-------|------|
| Dhoni | 10000 | 0    |
| Kohli | 8000  | 1    |
| Rohit | 9000  | 2    |

#### One Hot Encoding (after performing one-hot encoding)

| Name  | Runs  | CSK | RCB | MI |
|-------|-------|-----|-----|----|
| Dhoni | 10000 | 1   | 0   | 0  |
| Kohli | 8000  | 0   | 1   | 0  |
| Rohit | 9000  | 0   | 0   | 1  |

### One Hot encoding can be achieved with two libraries
1. Pandas - get_dummies()
2. sklearn - OneHotEncoder()