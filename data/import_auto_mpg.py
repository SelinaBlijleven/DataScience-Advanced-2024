"""
import_auto_mpg

Use the following code to import the Auto MPG dataset that is missing from the files.
Note: this does not trigger a download, but allows you to use the dataset directly from your script.
"""
import pandas as pd
from datasets import load_dataset

dataset: pd.DataFrame = pd.DataFrame(load_dataset("scikit-learn/auto-mpg")['train'])
