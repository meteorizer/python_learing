import pandas as pd
import numpy as np

# Create sample data
# num_rows = 500
# num_cols = 20
data = np.random.randint(0, 10, size=(num_rows, num_cols))
columns = [f'Column{i}' for i in range(num_cols)]
df = pd.DataFrame(data, columns=columns)

# Calculate sum and average of each row
df['Row Sum'] = df.sum(axis=1)
df['Row Average'] = df.mean(axis=1)

print(df)

output = df