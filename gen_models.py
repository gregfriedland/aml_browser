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
			s += "    str = CharField(max_length=32)\n"
			print(s)
		return

	s = "%s(Model):\n" % to_camel_case(field_name)
	for name, subfield in subfields.items():
		if subfield.many:
			s += "    %s = ManyToMany(%s)\n" % (name, to_camel_case(name))
		else:
			s += "    %s = CharField(max_length=32)\n" % name
	print(s)

def ignore_field(f):
	return f in [
		"patient.molecular_analysis_abnormality_testing_results",
		"fish_test_component_results"
	]

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

table_fn = sys.argv[1]
txt = open(table_fn).read()
lines = txt.strip().split("\n")

data = {}
for line in lines[1:]:
	toks = line.split("\t")
	field = toks[0]
	if not field.startswith("patient.") or ignore_field(field):
		continue

	# change some field names to remove redundancy
	simple_field = simplify_field(field)

	data[simple_field] = toks[1:]

# construct field tree
field_tree = FieldTree()
for field in data:
	print(field)
	field_tree.add_field(field)

if DEBUG:
	print(field_tree)

print()
field_tree.walk(gen_model_str)


