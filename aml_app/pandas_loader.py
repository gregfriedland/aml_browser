# Load data from the file into a pandas dataframe

import pandas as pd
import sys
import numpy as np
import re

# Simplify some fields that are needlessly verbose
def simplify_field(f):
    f = f.replace("patient.cytogenetic_abnormalities.cytogenetic_abnormality",
        "patient.cytogenetic_abnormality")
    f = f.replace("patient.fish_test_component_results.fish_test_component_result",
        "patient.fish_test_component_result")
    f = f.replace("molecular_analysis_abnormality_testing_results.molecular_analysis_abnormality_testing_result_values",
        "molecular_analysis_abnormality_testing_result_values")
    f = f.replace("immunophenotype_cytochemistry_testing_results.immunophenotype_cytochemistry_testing_result_values",
        "immunophenotype_cytochemistry_testing_result")
    f = f.replace("race_list.race", "race")
    f = f.replace("patient.", "")
    return f

# Create the pandas dataframe from a file
def load_dataframe(fn):
    df = pd.read_csv(open(fn), sep="\t").transpose()
    df.columns = df.iloc[0]
    df = df.drop(df.index[0]) # drop the row with the columns names

    df.columns = [simplify_field(c) for c in df.columns]

    # Remove some empty fields
    for field in ["molecular_analysis_abnormality_testing_results",
         "fish_test_component_results"]:
        del df[field]

    # Use strings for missing values
    df = df.fillna("")

    return df

if __name__ == "__main__":
    fn = sys.argv[1]

    df = load_dataframe(fn)

    pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 250)

    print(df.describe())
    print(df)
