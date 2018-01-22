from pandas_loader import load_dataframe
import sys
import re
from .models import Patient, FishTestComponentResult, CytogeneticAbnormality, \
    ImmunophenotypeCytochemistryTestingResult, \
    MolecularAnalysisAbnormalityTestingResult
import pandas as pd
import numpy as np

def remove_field_index(field):
    return re.sub('\-\d+', '', field)

def load_db(fn):
    df = load_dataframe(fn)

    field_map = {}
    for field in df.columns:
        field_map.setdefault(remove_field_index(field), []).append(field)

    patients = []
    for rowindex, row in df.iterrows():
        p = Patient()
        for i, (field, val) in enumerate(row.iteritems()):
            if len(field_map[remove_field_index(field)]) == 1:
                setattr(p, field, val)
        p.save()
        patients.append(p)

    print(list(df.columns))

    obj_map = {}

    # MolecularAnalysisAbnormalityTestingResult
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

    # Cytogenetic abnormality
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

    # Fish Test Component
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

    # Immunophenotype Cytochemistry
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

