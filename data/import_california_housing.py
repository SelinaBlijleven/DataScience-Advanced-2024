import pandas as pd
from datasets import load_dataset

df: pd.DataFrame = pd.DataFrame(load_dataset("leostelon/california-housing")['train'])
print(df.columns)