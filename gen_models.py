import sys
import re
import itertools
from field_tree import FieldTree, remove_field_index

DEBUG = True

def to_camel_case(field):
	s = ""
	for tok in field.split("_"):
		s += tok[0].upper()
		if len(tok) > 0:
			 s += tok[1:]
	return s

def gen_model_str(field_name, many, subfields):
	if len(subfields) == 0:
		if many:
			s = "%s(Model):\n" % to_camel_case(field_name)
			s += "    str = CharField(max_length=64)\n"
			print(s)
		return

	s = "%s(Model):\n" % to_camel_case(field_name)
	for name, subfield in subfields.items():
		if subfield.many:
			s += "    %s = ManyToMany(%s)\n" % (name, to_camel_case(name))
		else:
			s += "    %s = CharField(max_length=32)\n" % name
	print(s)


table_fn = sys.argv[1]
txt = open(table_fn).read()
lines = txt.strip().split("\n")
fields = [line.split("\t")[0] for line in lines[1:]]

# change some field names
for i in range(len(fields)):
	fields[i] = fields[i].replace("patient.cytogenetic_abnormalities.cytogenetic_abnormality",
		"patient.cytogenetic_abnormality")
	fields[i] = fields[i].replace("patient.fish_test_component_results.fish_test_component_result",
		"patient.fish_test_component_result")
	fields[i] = fields[i].replace("molecular_analysis_abnormality_testing_results.molecular_analysis_abnormality_testing_result_values",
		"molecular_analysis_abnormality_testing_result")
	fields[i] = fields[i].replace("immunophenotype_cytochemistry_testing_results.immunophenotype_cytochemistry_testing_result_values",
		"immunophenotype_cytochemistry_testing_result")

# fields_map = {}
# for field in fields:
# 	fields_map.setdefault(remove_field_index(field), []).append(field)

# if DEBUG:
# 	for uniq_field, fields in fields_map.items():
# 		print(len(fields), uniq_field)

# construct field tree
field_tree = FieldTree()
for field in fields:
	print(field)
	field_tree.add_field(field)

if DEBUG:
	print(field_tree)

print()
field_tree.walk(gen_model_str)
