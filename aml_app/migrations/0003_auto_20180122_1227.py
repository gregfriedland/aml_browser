# Generated by Django 2.0.1 on 2018-01-22 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aml_app', '0002_auto_20180120_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cytogeneticabnormality',
            old_name='abnormality',
            new_name='cytogenetic_abnormality',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='fish_test_component_result',
            new_name='fish_test_component',
        ),
        migrations.RemoveField(
            model_name='immunophenotypecytochemistrytestingresult',
            name='immunophenotype_cytochemistry_percent_positive',
        ),
        migrations.RemoveField(
            model_name='molecularanalysisabnormalitytestingresult',
            name='molecular_analysis_abnormality_testing_percentage_value',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='fish_test_component_results',
        ),
    ]
