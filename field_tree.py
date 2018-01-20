import re

class Field:
	def __init__(self, name, subfields):
		simple_name = remove_field_index(name)
		self.name = simple_name
		self.subfields = {}
		self.many = simple_name != name

	def tostr(self, indent=0):
		s = " "*indent + self.name + "\n"
		s += "".join([f.tostr(indent+2) for name, f in self.subfields.items()])
		return s

	def walk(self, func):
		func(self.name, self.many, self.subfields)
		for name, f in self.subfields.items():
			f.walk(func)

	def __str__(self):
		return self.tostr(0)

class FieldTree:
	def __init__(self):
		self.root = Field("", [])

	def add_field(self, compound_name):
		node = self.root
		toks = compound_name.split(".")
		for tok in toks:
			simple_tok = remove_field_index(tok)
			node = node.subfields.setdefault(simple_tok, Field(tok, []))
			if simple_tok != tok:
				node.many = True

	def walk(self, func):
		for name, subfield in self.root.subfields.items():
			subfield.walk(func)

	def __str__(self):
		return str(self.root)


def remove_field_index(field):
	return re.sub('\-\d+', '', field)
