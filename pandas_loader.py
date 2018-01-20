import pandas as pd
import sys
import numpy as np
import re

def simplify_field(f):
	# f = f.replace("patient.cytogenetic_abnormalities.cytogenetic_abnormality",
	# 	"patient.cytogenetic_abnormality")
	f = f.replace("patient.fish_test_component_results.fish_test_component_result",
		"patient.fish_test_component_result")
	f = f.replace("molecular_analysis_abnormality_testing_results.molecular_analysis_abnormality_testing_result_values",
		"molecular_analysis_abnormality_testing_result")
	f = f.replace("immunophenotype_cytochemistry_testing_results.immunophenotype_cytochemistry_testing_result_values",
		"immunophenotype_cytochemistry_testing_result")
	f = f.replace("race_list.race", "race")
	f = f.replace("patient.", "")
	return f

def to_camel_case(field):
	s = ""
	for tok in field.split("_"):
		s += tok[0].upper()
		if len(tok) > 0:
			 s += tok[1:]
	return s

def remove_field_index(field):
	return re.sub('\-\d+', '', field)

def load_dataframe(fn):
	df = pd.read_csv(open(fn), sep="\t").transpose()
	df.columns = df.iloc[0]
	df = df.drop(df.index[0]) # drop the row with the columns names

	df.columns = [simplify_field(c) for c in df.columns]

	for field in ["molecular_analysis_abnormality_testing_results",
		 "fish_test_component_results"]:
		del df[field]

	return df

if __name__ == "__main__":
	fn = sys.argv[1]

	df = load_dataframe(fn)

	pd.set_option('display.height', 1000)
	pd.set_option('display.max_rows', 500)
	pd.set_option('display.max_columns', 500)
	pd.set_option('display.width', 250)

	print(df)

# simplify cytogenetic abnormality column
# cyt_abnorm_cols = [c for c in df.columns if c.startswith("patient.cytogenetic_abnormality")]
# cyt_abnorms = set()
# for c in cyt_abnorm_cols:
# 	cyt_abnorms = cyt_abnorms.union(df["patient.cytogenetic_abnormality"].unique())
# cyt_abnorms = cyt_abnorms.difference(["normal", np.nan])
# print(cyt_abnorms)
# for cyt_abnorm in cyt_abnorms:
# 	hasit = df[cyt_abnorm_cols[0]] == cyt_abnorm
# 	for c in cyt_abnorm_cols[1:]:
# 		hasit = hasit | (df[c] == cyt_abnorm)
# 	df["patient.cytogenetic_abnormality." + cyt_abnorm] = hasit

# for c in cyt_abnorm_cols:
# 	del df[c]

# field_map = {}
# for field in df.columns:
# 	field_map.setdefault(remove_field_index(field), []).append(field)

# print("class Patient(Model):")
# for field in df.columns:
# 	if field in field_map:
# 		if len(field_map[field]) > 1:
# 			print("    %s = ManyToMany(%s)" % (field, to_camel_case(field)))
# 		else:
# 			print("    %s = CharField(max_length=32)" % field)

# for row in df.iterrows():
