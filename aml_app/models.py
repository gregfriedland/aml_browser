from django.db import models

class CytogeneticAbnormality(models.Model):
    cytogenetic_abnormality = models.CharField(max_length=32, default="")

# Note: percentage_value field here is not empty so don't ignore it; fish_test_component should
# be in a separate table
class FishTestComponentResult(models.Model):
    fish_test_component = models.CharField(max_length=32, default="")
    fish_test_component_percentage_value = models.CharField(max_length=32, default="")

# Note: ignore percentage_positive field because it's always empty
class ImmunophenotypeCytochemistryTestingResult(models.Model):
    # immunophenotype_cytochemistry_percent_positive = models.CharField(max_length=32, default="")
    immunophenotype_cytochemistry_testing_result = models.CharField(max_length=32, default="")

# Note: ignore percentage_value field because it's always empty
class MolecularAnalysisAbnormalityTestingResult(models.Model):
    # molecular_analysis_abnormality_testing_percentage_value = models.CharField(max_length=32, default="")
    molecular_analysis_abnormality_testing_result = models.CharField(max_length=32, default="")


class Patient(models.Model):
    acute_myeloid_leukemia_calgb_cytogenetics_risk_category = models.CharField(max_length=32, default="")
    additional_studies = models.CharField(max_length=32, default="")
    age_at_initial_pathologic_diagnosis = models.CharField(max_length=32, default="")
    assessment_timepoint_category = models.CharField(max_length=32, default="")
    atra_exposure = models.CharField(max_length=32, default="")
    bcr_patient_barcode = models.CharField(max_length=32, default="")
    bcr_patient_uuid = models.CharField(max_length=32, default="")
    cumulative_agent_total_dose = models.CharField(max_length=32, default="")
    cytogenetic_abnormality = models.ManyToManyField(CytogeneticAbnormality)
    cytogenetic_abnormality_other = models.CharField(max_length=32, default="")
    cytogenetic_analysis_performed_ind = models.CharField(max_length=32, default="")
    day_of_form_completion = models.CharField(max_length=32, default="")
    days_to_birth = models.CharField(max_length=32, default="")
    days_to_death = models.CharField(max_length=32, default="")
    days_to_initial_pathologic_diagnosis = models.CharField(max_length=32, default="")
    days_to_last_followup = models.CharField(max_length=32, default="")
    days_to_last_known_alive = models.CharField(max_length=32, default="")
    disease_detection_molecular_analysis_method_type = models.CharField(max_length=32, default="")
    disease_detection_molecular_analysis_method_type_other_text = models.CharField(max_length=32, default="")
    drugs = models.CharField(max_length=32, default="")
    eastern_cancer_oncology_group = models.CharField(max_length=32, default="")
    ethnicity = models.CharField(max_length=32, default="")
    fish_evaluation_performed_ind = models.CharField(max_length=32, default="")
    fish_test_component = models.ManyToManyField(FishTestComponentResult)
    fluorescence_in_situ_hybrid_cytogenetics_metaphase_nucleus_result_count = models.CharField(max_length=32, default="")
    fluorescence_in_situ_hybridization_abnormal_result_indicator = models.CharField(max_length=32, default="")
    follow_ups = models.CharField(max_length=32, default="")
    gender = models.CharField(max_length=32, default="")
    germline_testing_performed = models.CharField(max_length=32, default="")
    history_of_neoadjuvant_treatment = models.CharField(max_length=32, default="")
    hydroxyurea_administration_prior_registration_clinical_study_indicator = models.CharField(max_length=32, default="")
    hydroxyurea_agent_administered_day_count = models.CharField(max_length=32, default="")
    icd_10 = models.CharField(max_length=32, default="")
    icd_o_3_histology = models.CharField(max_length=32, default="")
    icd_o_3_site = models.CharField(max_length=32, default="")
    immunophenotype_cytochemistry_testing_result = models.ManyToManyField(ImmunophenotypeCytochemistryTestingResult)
    informed_consent_verified = models.CharField(max_length=32, default="")
    initial_pathologic_diagnosis_method = models.CharField(max_length=32, default="")
    karnofsky_performance_score = models.CharField(max_length=32, default="")
    lab_procedure_abnormal_lymphocyte_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_blast_cell_outcome_percentage_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_band_cell_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_basophil_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_blast_cell_outcome_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_cellularity_outcome_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_diff_not_reported_reason = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_lab_eosinophil_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_lymphocyte_outcome_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_metamyelocyte_result_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_myelocyte_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_neutrophil_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_prolymphocyte_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_promonocyte_count_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_bone_marrow_promyelocyte_result_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_hematocrit_outcome_percent_value = models.CharField(max_length=32, default="")
    lab_procedure_hemoglobin_result_specified_value = models.CharField(max_length=32, default="")
    lab_procedure_leukocyte_result_unspecified_value = models.CharField(max_length=32, default="")
    lab_procedure_monocyte_result_percent_value = models.CharField(max_length=32, default="")
    leukemia_french_american_british_morphology_code = models.CharField(max_length=32, default="")
    leukemia_specimen_cell_source_type = models.CharField(max_length=32, default="")
    molecular_analysis_abnormal_result_indicator = models.CharField(max_length=32, default="")
    molecular_analysis_abnormality_testing_result = models.ManyToManyField(MolecularAnalysisAbnormalityTestingResult)
    month_of_form_completion = models.CharField(max_length=32, default="")
    other_dx = models.CharField(max_length=32, default="")
    patient_id = models.CharField(max_length=32, default="")
    performance_status_scale_timing = models.CharField(max_length=32, default="")
    person_history_leukemogenic_agent_other_exposure_text = models.CharField(max_length=32, default="")
    person_history_nonmedical_leukemia_causing_agent_type = models.CharField(max_length=32, default="")
    platelet_result_count = models.CharField(max_length=32, default="")
    prior_hematologic_disorder_diagnosis_indicator = models.CharField(max_length=32, default="")
    race = models.CharField(max_length=32, default="")
    radiations = models.CharField(max_length=32, default="")
    steroid_therapy_administered = models.CharField(max_length=32, default="")
    tissue_source_site = models.CharField(max_length=32, default="")
    total_dose_units = models.CharField(max_length=32, default="")
    tumor_tissue_site = models.CharField(max_length=32, default="")
    tumor_tissue_site_other = models.CharField(max_length=32, default="")
    vital_status = models.CharField(max_length=32, default="")
    year_of_form_completion = models.CharField(max_length=32, default="")
    year_of_initial_pathologic_diagnosis = models.CharField(max_length=32, default="")

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Patient._meta.fields]
