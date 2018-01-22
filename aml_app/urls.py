from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets
from . import models

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('patient_id', 'gender', 'ethnicity', 'platelet_result_count', 'vital_status')

class PatientListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientListSerializer

class FishTestComponentResultSerializer(serializers.ModelSerializer):
   class Meta:
        model = models.FishTestComponentResult
        fields = ('fish_test_component', 'fish_test_component_percentage_value')

class PatientDetailSerializer(serializers.ModelSerializer):
    cytogenetic_abnormality = serializers.SlugRelatedField(many=True,
        read_only=True, slug_field='cytogenetic_abnormality')

    immunophenotype_cytochemistry_testing_result = serializers.SlugRelatedField(many=True,
        read_only=True, slug_field='immunophenotype_cytochemistry_testing_result')

    molecular_analysis_abnormality_testing_result = serializers.SlugRelatedField(many=True,
        read_only=True, slug_field='molecular_analysis_abnormality_testing_result')

    fish_test_component = FishTestComponentResultSerializer(read_only=True, many=True)

    class Meta:
        model = models.Patient
        fields = ("acute_myeloid_leukemia_calgb_cytogenetics_risk_category", "additional_studies", "age_at_initial_pathologic_diagnosis", "assessment_timepoint_category", "atra_exposure", "bcr_patient_barcode", "bcr_patient_uuid", "cumulative_agent_total_dose", "cytogenetic_abnormality_other", "cytogenetic_analysis_performed_ind", "day_of_form_completion", "days_to_birth", "days_to_death", "days_to_initial_pathologic_diagnosis", "days_to_last_followup", "days_to_last_known_alive", "disease_detection_molecular_analysis_method_type", "disease_detection_molecular_analysis_method_type_other_text", "drugs", "eastern_cancer_oncology_group", "ethnicity", "fish_evaluation_performed_ind", "fluorescence_in_situ_hybrid_cytogenetics_metaphase_nucleus_result_count", "fluorescence_in_situ_hybridization_abnormal_result_indicator", "follow_ups", "gender", "germline_testing_performed", "history_of_neoadjuvant_treatment", "hydroxyurea_administration_prior_registration_clinical_study_indicator", "hydroxyurea_agent_administered_day_count", "icd_10", "icd_o_3_histology", "icd_o_3_site", "informed_consent_verified", "initial_pathologic_diagnosis_method", "karnofsky_performance_score", "lab_procedure_abnormal_lymphocyte_result_percent_value", "lab_procedure_blast_cell_outcome_percentage_value", "lab_procedure_bone_marrow_band_cell_result_percent_value", "lab_procedure_bone_marrow_basophil_result_percent_value", "lab_procedure_bone_marrow_blast_cell_outcome_percent_value", "lab_procedure_bone_marrow_cellularity_outcome_percent_value", "lab_procedure_bone_marrow_diff_not_reported_reason", "lab_procedure_bone_marrow_lab_eosinophil_result_percent_value", "lab_procedure_bone_marrow_lymphocyte_outcome_percent_value", "lab_procedure_bone_marrow_metamyelocyte_result_value", "lab_procedure_bone_marrow_myelocyte_result_percent_value", "lab_procedure_bone_marrow_neutrophil_result_percent_value", "lab_procedure_bone_marrow_prolymphocyte_result_percent_value", "lab_procedure_bone_marrow_promonocyte_count_result_percent_value", "lab_procedure_bone_marrow_promyelocyte_result_percent_value", "lab_procedure_hematocrit_outcome_percent_value", "lab_procedure_hemoglobin_result_specified_value", "lab_procedure_leukocyte_result_unspecified_value", "lab_procedure_monocyte_result_percent_value", "leukemia_french_american_british_morphology_code", "leukemia_specimen_cell_source_type", "molecular_analysis_abnormal_result_indicator", "month_of_form_completion", "other_dx", "patient_id", "performance_status_scale_timing", "person_history_leukemogenic_agent_other_exposure_text", "person_history_nonmedical_leukemia_causing_agent_type", "platelet_result_count", "prior_hematologic_disorder_diagnosis_indicator", "race", "radiations", "steroid_therapy_administered", "tissue_source_site", "total_dose_units", "tumor_tissue_site", "tumor_tissue_site_other", "vital_status", "year_of_form_completion", "year_of_initial_pathologic_diagnosis",
                "cytogenetic_abnormality", "immunophenotype_cytochemistry_testing_result", "molecular_analysis_abnormality_testing_result", "fish_test_component")

class PatientDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientDetailSerializer

urlpatterns = [
    # API endpoints
    path('patient/v1', PatientListViewSet.as_view({'get': 'list'})),
    path('patient/<int:pk>/v1', PatientDetailViewSet.as_view({'get': 'retrieve'})),

    # pages
    # ex: /aml
    path('', views.index, name='index'),
    # ex: /aml/5/
    path('<int:patient_pk>/', views.detail, name='detail'),
]
