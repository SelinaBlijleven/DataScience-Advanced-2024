"""
import_auto_mpg

Use the following code to import the Auto MPG dataset that is missing from the files.
Note: this does not trigger a download, but allows you to use the dataset directly from your script.
"""
from datasets import load_dataset

dataset = load_dataset("scikit-learn/auto-mpg")
