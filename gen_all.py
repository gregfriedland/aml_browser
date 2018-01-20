from pandas_loader import load_dataframe
from gen_models import gen_models
import sys
import pandas as pd

if __name__ == "__main__":
	fn = sys.argv[1]

	gen_models(fn)

	df = load_dataframe(fn)

	pd.set_option('display.height', 1000)
	pd.set_option('display.max_rows', 500)
	pd.set_option('display.max_columns', 500)
	pd.set_option('display.width', 250)
	print(df)

	gen_inserts(df)