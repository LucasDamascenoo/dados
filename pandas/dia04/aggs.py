#%%
import pandas as pd


df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

result = df.agg({
    'A': ['sum', 'mean'],
    'B': ['min', 'max']
})

print(result)
# %%
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [1, 2, 3, 4]
})

result = df.groupby('Category').agg({
    'Values': ['sum', 'mean']
})

print(result)

# %%
def range_func(x):
    return x.max() - x.min()

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

result = df.agg({
    'A': ['sum', range_func],
    'B': ['min', 'max']
})

print(result)