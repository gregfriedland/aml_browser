from field_tree import Field, FieldTree
import unittest

# patient.molecular_analysis_abnormality_testing_results.molecular_analysis_abnormality_testing_result_values.molecular_analysis_abnormality_testing_percentage_value
class TestField(unittest.TestCase):
    def test_simple_field(self):
        f = Field("patient", [])
        self.assertEqual(f.name, "patient")
        self.assertEqual(f.subfields, {})
        self.assertEqual(f.many, False)

    def test_one_part_field(self):
        ft = FieldTree()
        ft.add_field("patient")
        self.assertEqual(ft.root.name, "")
        self.assertEqual(len(ft.root.subfields), 1)
        self.assertEqual(ft.root.subfields["patient"].name, "patient")
        self.assertEqual(ft.root.subfields["patient"].subfields, {})

    def test_two_part_field(self):
        ft = FieldTree()
        ft.add_field("admin.batch")
        self.assertEqual(len(ft.root.subfields), 1)
        admin = ft.root.subfields["admin"]
        self.assertEqual(admin.name, "admin")
        self.assertEqual(len(admin.subfields), 1)
        batch = admin.subfields["batch"]
        self.assertEqual(batch.name, "batch")
        self.assertEqual(len(batch.subfields), 0)

    def test_two_part_fields(self):
        ft = FieldTree()
        ft.add_field("admin.batch")
        ft.add_field("admin.bcr")
        self.assertEqual(len(ft.root.subfields), 1)
        admin = ft.root.subfields["admin"]
        self.assertEqual(admin.name, "admin")
        self.assertEqual(len(admin.subfields), 2)
        for name in ["batch", "bcr"]:
            field = admin.subfields[name]
            self.assertEqual(field.name, name)
            self.assertEqual(len(field.subfields), 0)

        print(ft)

    def test_two_part_field_with_many(self):
        ft = FieldTree()
        ft.add_field("admin.batch")
        ft.add_field("admin.batch-2")
        self.assertEqual(len(ft.root.subfields), 1)
        admin = ft.root.subfields["admin"]
        self.assertEqual(admin.name, "admin")
        self.assertEqual(len(admin.subfields), 1)
        batch = admin.subfields["batch"]
        self.assertEqual(batch.name, "batch")
        self.assertEqual(len(batch.subfields), 0)
        self.assertEqual(batch.many, True)

if __name__ == '__main__':
    unittest.main()
