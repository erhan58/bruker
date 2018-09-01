from django.contrib import admin
from .models import Customer, Logcustomer, Dnasequence, Logdnasequence, Measurement, Logmeasurement, Measuringdevice, Logmeasuringdevice, Msp,  Logmsp, Speciesgenus, Logspeciesgenus, Strain, Logstrain, Synonym, Logsynonym 
# Register your models here.
admin.site.site_header = "Administration ";
admin.site.site_title = "Bruker Data ";

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 'customer_key', 'db_version']
    ordering = ['customer_id']

class LogcustomerAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'customer_id', 'customer_name', 'customer_key', 'db_version']
    ordering = ['log_id']

class DnasequenceAdmin(admin.ModelAdmin):
    list_display = ['dna_id', 'sequence', 'sequence_no', 'db_version']
    ordering = ['dna_id']

class LogdnasequenceAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'dna_id', 'sequence', 'sequence_no', 'db_version']
    ordering = ['log_id']

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['measurement_id', 'extraction_method', 'maldi_matrix', 'operator', 'maldi_run', 'changes_of_types', 'mass', 'db_version']
    ordering = ['measurement_id']

class LogmeasurementAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'measurement_id', 'extraction_method', 'maldi_matrix', 'operator', 'maldi_run', 'changes_of_types', 'mass', 'db_version']
    ordering = ['log_id']

class MeasuringdeviceAdmin(admin.ModelAdmin):
    list_display = ['md_id', 'instrument', 'fkeymeasurement', 'db_version']
    ordering = ['md_id']

class LogmeasuringdeviceAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'md_id', 'instrument', 'fkeymeasurement', 'db_version']
    ordering = ['log_id']

class MspAdmin(admin.ModelAdmin):
    list_display = ['msp_id', 'msp_name', 'msp_id_db7311', 'change_since_version', 'fkeymeasurement', 'fkeysynonym', 'db_version']
    ordering = ['msp_id']

class LogmspAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'msp_id', 'msp_name', 'msp_id_db7311', 'change_since_version', 'fkeymeasurement', 'fkeysynonym', 'db_version']
    ordering = ['log_id']

class SpeciesgenusAdmin(admin.ModelAdmin):
    list_display = ['species_id', 'gram_information', 'name', 'oxygen', 'db_version']
    ordering = ['species_id']

class LogspeciesgenusAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'species_id', 'gram_information', 'name', 'oxygen', 'db_version']
    ordering = ['log_id']

class StrainAdmin(admin.ModelAdmin):
    list_display = ['strain_id', 'strain_name', 'growing_conditions', 'method_of_identification_key', 'method_of_identification', 'conserve', 'sample_submission', 'fkeyspeciesgenus', 'fkeymsp', 'fkeycustomer', 'fkeysequence', 'fkeymeasurement', 'db_version']
    ordering = ['strain_id']

class LogstrainAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'strain_id', 'strain_name', 'growing_conditions', 'method_of_identification_key', 'method_of_identification', 'conserve', 'sample_submission', 'fkeyspeciesgenus', 'fkeymsp', 'fkeycustomer', 'fkeysequence', 'fkeymeasurement', 'db_version']
    ordering = ['log_id']

class SynonymAdmin(admin.ModelAdmin):
    list_display = ['synonym_id', 'synonym_name', 'comments', 'matching_hints_metadata', 'ivd', 'db_version']
    ordering = ['synonym_id']

class LogsynonymAdmin(admin.ModelAdmin):
    list_display = ['log_id', 'operation', 'stamp', 'synonym_id', 'synonym_name', 'comments', 'matching_hints_metadata', 'ivd', 'db_version']
    ordering = ['log_id']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Logcustomer, LogcustomerAdmin)
admin.site.register(Dnasequence, DnasequenceAdmin)
admin.site.register(Logdnasequence, LogdnasequenceAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Logmeasurement, LogmeasurementAdmin)
admin.site.register(Measuringdevice)
admin.site.register(Logmeasuringdevice)
admin.site.register(Msp, MspAdmin)
admin.site.register(Logmsp, LogmspAdmin)
admin.site.register(Speciesgenus, SpeciesgenusAdmin)
admin.site.register(Logspeciesgenus, LogspeciesgenusAdmin)
admin.site.register(Strain, StrainAdmin)
admin.site.register(Logstrain, LogstrainAdmin)
admin.site.register(Synonym, SynonymAdmin)
admin.site.register(Logsynonym, LogsynonymAdmin)

