from config import DROP_COLS
from preprocess import drop_cols
import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')
drop_cols(df,DROP_COLS)