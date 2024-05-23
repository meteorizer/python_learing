import gc

# Freeze the garbage collector
gc.freeze()

# Your code here
import pandas as pd
import numpy as np
print("OK")

df = pd.DataFrame(np.random.randn(30000, 100))

print(df.describe())

# Unfreeze the garbage collector
gc.unfreeze()