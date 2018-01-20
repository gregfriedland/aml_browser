from pandas_loader import load_dataframe
import sys
import re
from .models import Patient, FishTestComponentResult
import pandas as pd

def remove_field_index(field):
    return re.sub('\-\d+', '', field)

# def get_many2many_objs(df, mult_field_cols, subfields, class_type):
#     print("mult_field_cols", mult_field_cols)
#     print("subfields", subfields)

#     # get ets of values of the subfields
#     all_vals = pd.DataFrame(columns=[remove_field_index(mult_field_cols[0]) + "." + sf for sf in subfields])
#     print("all_vals", all_vals)
#     for field_col in mult_field_cols:
#         subfield_cols = [field_col + "." + sf for sf in subfields]
#         print("subfield_cols", subfield_cols)
#         vals = df[subfield_cols]
#         print("vals", vals)
#         vals.columns = all_vals.columns
#         all_vals = pd.concat([all_vals, vals], axis=0)
#         print("all_vals", all_vals)

#     print(all_vals)
#     # create objects for the values
#     objs = []
#     for i, row in all_vals.iterrows():
#         print("row", row)
#         obj = class_type()
#         for subfield_col in all_vals.columns:
#             setattr(obj, subfield_col.split(".")[1], row[subfield_col])
#         objs.append(obj)

#     return objs


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
        patients.append(p)


    print(list(df.columns))

    # Fish Test Component
    for i in range(9):
        print("i", i)
        base = "fish_test_component_result" + ("-%d" % (i+1) if i > 0 else "")
        component_col = base + ".fish_test_component"
        pct_val_col = base + ".fish_test_component_percentage_value"
        objs = []
        for i, row in df.iterrows():
            print("row names", list(row.index))
            obj = FishTestComponentResult()
            obj.fish_test_component = row[component_col]
            obj.fish_test_percentage_value = row[pct_val_col]
            objs.append(obj)

        for patient, obj in zip(patients, objs):
            patient.fish_test_component = obj
