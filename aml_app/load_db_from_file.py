# Load the database into the DB from a file.
# Most fields are loaded as text fields into Patient while 4 of the fields
# are given ManyToMany relationships to Patient.
# This code is dependent on the structure of the file not changing.

from aml_app.pandas_loader import load_dataframe
import sys
import re
from .models import Patient, FishTestComponentResult, CytogeneticAbnormality, \
    ImmunophenotypeCytochemistryTestingResult, \
    MolecularAnalysisAbnormalityTestingResult
import pandas as pd
import numpy as np

# Remove a field index such as "-2" from a field
def remove_field_index(field):
    return re.sub('\-\d+', '', field)

# Load data into the DB
def load_db(fn):
    # Load the data into a pandas DataFrame
    df = load_dataframe(fn)

    # Find fields with multiple indices
    field_map = {}
    for field in df.columns:
        field_map.setdefault(remove_field_index(field), []).append(field)

    # Assign simple fields from the dataframe to the Patient object
    patients = []
    for rowindex, row in df.iterrows():
        p = Patient()
        for i, (field, val) in enumerate(row.iteritems()):
            if len(field_map[remove_field_index(field)]) == 1:
                setattr(p, field, val)
        p.save()
        patients.append(p)

    # print(list(df.columns))

    obj_map = {}

    # Create MolecularAnalysisAbnormalityTestingResult objects and relationships
    print("MolecularAnalysisAbnormalityTestingResult")
    for i in range(8):
        print("i", i)
        base = "molecular_analysis_abnormality_testing_result_values" + ("-%d" % (i+1) if i > 0 else "")
        pct_val_col = base + ".molecular_analysis_abnormality_testing_percentage_value"
        result_col = base + ".molecular_analysis_abnormality_testing_result"
        objs = []
        for i, row in df.iterrows():
            key = row[result_col]
            if key not in obj_map:
                obj = MolecularAnalysisAbnormalityTestingResult()
                # obj.molecular_analysis_abnormality_testing_percentage_value = str(row[pct_val_col])
                obj.molecular_analysis_abnormality_testing_result = row[result_col]
                obj.save()
                obj_map[key] = obj
            objs.append(obj_map[key])

        for patient, obj in zip(patients, objs):
            if obj.molecular_analysis_abnormality_testing_result != "":
                patient.molecular_analysis_abnormality_testing_result.add(obj)

    # Create CytogeneticAbnormality objects and relationships
    print("CytogenicAbnormality")
    obj_map = {}
    for i in range(4):
        print("i", i)
        col = "cytogenetic_abnormality" + ("-%d" % (i+1) if i > 0 else "")
        objs = []
        for i, row in df.iterrows():
            key = row[col]
            if key not in obj_map:
                obj = CytogeneticAbnormality()
                obj.cytogenetic_abnormality = row[col]
                obj.save()
                obj_map[key] = obj
            objs.append(obj_map[key])

        for patient, obj in zip(patients, objs):
            if obj.cytogenetic_abnormality != "":
                patient.cytogenetic_abnormality.add(obj)

    # Create FishTestComponent objects and relationships
    print("Fish")
    obj_map = {}
    for i in range(9):
        print("i", i)
        base = "fish_test_component_result" + ("-%d" % (i+1) if i > 0 else "")
        component_col = base + ".fish_test_component"
        pct_val_col = base + ".fish_test_component_percentage_value"
        objs = []
        for i, row in df.iterrows():
            key = (row[component_col], row[pct_val_col])
            if key not in obj_map:
                obj = FishTestComponentResult()
                obj.fish_test_component = row[component_col]
                obj.fish_test_component_percentage_value = row[pct_val_col]
                obj.save()
                obj_map[key] = obj
            objs.append(obj_map[key])

        for patient, obj in zip(patients, objs):
            if obj.fish_test_component != "":
                patient.fish_test_component.add(obj)

    # Create ImmunophenotypeCytochemistry objects and relationships
    print("Immunophenotype")
    obj_map = {}
    for i in range(21):
        print("i", i)
        base = "immunophenotype_cytochemistry_testing_result" + ("-%d" % (i+1) if i > 0 else "")
        pct_pos_col = base + ".immunophenotype_cytochemistry_percent_positive"
        result_col = base + ".immunophenotype_cytochemistry_testing_result"
        objs = []
        for i, row in df.iterrows():
            key = row[result_col]
            if key not in obj_map:
                obj = ImmunophenotypeCytochemistryTestingResult()
                # obj.immunophenotype_cytochemistry_percent_positive = row[pct_pos_col]
                obj.immunophenotype_cytochemistry_testing_result = row[result_col]
                obj.save()
                obj_map[key] = obj
            objs.append(obj_map[key])

        for patient, obj in zip(patients, objs):
            if obj.immunophenotype_cytochemistry_testing_result != "":
                patient.immunophenotype_cytochemistry_testing_result.add(obj)
