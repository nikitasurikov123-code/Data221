import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
#creates the data frame
data_frame = pd.DataFrame(data)
#makes a new column in the data frame that is column A ^ (column C / column B)
data_frame["New column"] = data_frame["A"] ** (data_frame["C"] / data_frame["B"])
print(data_frame)