import pandas as pd
import sys
import numpy as np

def simplify_field(f):
	f = f.replace("patient.cytogenetic_abnormalities.cytogenetic_abnormality",
		"patient.cytogenetic_abnormality")
	f = f.replace("patient.fish_test_component_results.fish_test_component_result",
		"patient.fish_test_component_result")
	f = f.replace("molecular_analysis_abnormality_testing_results.molecular_analysis_abnormality_testing_result_values",
		"molecular_analysis_abnormality_testing_result")
	f = f.replace("immunophenotype_cytochemistry_testing_results.immunophenotype_cytochemistry_testing_result_values",
		"immunophenotype_cytochemistry_testing_result")
	f = f.replace("race_list.race", "race")
	return f


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 250)

fn = sys.argv[1]

df = pd.read_csv(open(fn), sep="\t").transpose()
df.columns = df.iloc[0]
df = df.drop(df.index[0]) # drop the row with the columns names

for field in df.columns:
	if not field.startswith("patient.") or field in \
	 	["patient.molecular_analysis_abnormality_testing_results",
		 "patient.fish_test_component_results"]:
		del df[field]

	df.columns = [simplify_field(c) for c in df.columns]

# simplify cytogenetic abnormality column
cyt_abnorms = set()
for c in df.columns:
	if not c.startswith("patient.cytogenetic_abnormality"):
		continue
	cyt_abnorms = cyt_abnorms.union(df["patient.cytogenetic_abnormality"].unique())
cyt_abnorms = cyt_abnorms.difference(["normal", np.nan])
print(cyt_abnorms)

print(df)