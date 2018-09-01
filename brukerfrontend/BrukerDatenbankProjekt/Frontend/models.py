# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_key = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dnasequence(models.Model):
    dna_id = models.IntegerField(primary_key=True)
    sequence = models.CharField(max_length=9999, blank=True, null=True)
    sequence_no = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequence'


class Logcustomer(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    customer_id = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_key = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logcustomer'


class Logdnasequence(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    dna_id = models.IntegerField(blank=True, null=True)
    sequence = models.CharField(max_length=9999, blank=True, null=True)
    sequence_no = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logdnasequence'


class Logmeasurement(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    measurement_id = models.IntegerField(blank=True, null=True)
    extraction_method = models.CharField(max_length=255, blank=True, null=True)
    maldi_matrix = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    maldi_run = models.CharField(max_length=255, blank=True, null=True)
    changes_of_types = models.CharField(max_length=255, blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logmeasurement'


class Logmeasuringdevice(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    md_id = models.IntegerField(blank=True, null=True)
    instrument = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkeymeasurement = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logmeasuringdevice'


class Logmsp(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    msp_id = models.IntegerField(blank=True, null=True)
    msp_name = models.CharField(max_length=255, blank=True, null=True)
    msp_id_db7311 = models.CharField(max_length=255, blank=True, null=True)
    change_since_version = models.CharField(max_length=255, blank=True, null=True)
    fkeymeasurement = models.ForeignKey(Logmeasurement, models.DO_NOTHING, db_column='fkeymeasurement', blank=True, null=True)
    fkeysynonym = models.ForeignKey('Logsynonym', models.DO_NOTHING, db_column='fkeysynonym', blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logmsp'


class Logspeciesgenus(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    species_id = models.IntegerField(blank=True, null=True)
    gram_information = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    oxygen = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logspeciesgenus'


class Logstrain(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    strain_id = models.IntegerField(blank=True, null=True)
    strain_name = models.CharField(max_length=255, blank=True, null=True)
    growing_conditions = models.CharField(max_length=255, blank=True, null=True)
    method_of_identification_key = models.CharField(max_length=255, blank=True, null=True)
    method_of_identification = models.CharField(max_length=255, blank=True, null=True)
    conserve = models.CharField(max_length=255, blank=True, null=True)
    sample_submission = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkeyspeciesgenus = models.IntegerField(blank=True, null=True)
    fkeymsp = models.IntegerField(blank=True, null=True)
    fkeycustomer = models.IntegerField(blank=True, null=True)
    fkeysequence = models.IntegerField(blank=True, null=True)
    fkeymeasurement = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logstrain'


class Logsynonym(models.Model):
    log_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=1)
    stamp = models.DateTimeField()
    synonym_id = models.IntegerField(blank=True, null=True)
    synonym_name = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    matching_hints_metadata = models.CharField(max_length=255, blank=True, null=True)
    ivd = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logsynonym'


class Measurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    extraction_method = models.CharField(max_length=255, blank=True, null=True)
    maldi_matrix = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    maldi_run = models.CharField(max_length=255, blank=True, null=True)
    changes_of_types = models.CharField(max_length=255, blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurement'


class Measuringdevice(models.Model):
    md_id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=255, blank=True, null=True)
    fkeymeasurement = models.ForeignKey(Measurement, models.DO_NOTHING, db_column='fkeymeasurement', blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measuringdevice'


class Msp(models.Model):
    msp_id = models.IntegerField(primary_key=True)
    msp_name = models.CharField(max_length=255, blank=True, null=True)
    msp_id_db7311 = models.CharField(max_length=255, blank=True, null=True)
    change_since_version = models.CharField(max_length=255, blank=True, null=True)
    fkeymeasurement = models.IntegerField(blank=True, null=True)
    fkeysynonym = models.IntegerField(blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msp'


class Speciesgenus(models.Model):
    species_id = models.IntegerField(primary_key=True)
    gram_information = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    oxygen = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'speciesgenus'


class Strain(models.Model):
    strain_id = models.IntegerField(primary_key=True)
    strain_name = models.CharField(max_length=255, blank=True, null=True)
    growing_conditions = models.CharField(max_length=255, blank=True, null=True)
    method_of_identification_key = models.CharField(max_length=255, blank=True, null=True)
    method_of_identification = models.CharField(max_length=255, blank=True, null=True)
    conserve = models.CharField(max_length=255, blank=True, null=True)
    sample_submission = models.CharField(max_length=255, blank=True, null=True)
    fkeyspeciesgenus = models.ForeignKey(Speciesgenus, models.DO_NOTHING, db_column='fkeyspeciesgenus', blank=True, null=True)
    fkeymsp = models.ForeignKey(Msp, models.DO_NOTHING, db_column='fkeymsp', blank=True, null=True)
    fkeycustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fkeycustomer', blank=True, null=True)
    fkeysequence = models.ForeignKey(Dnasequence, models.DO_NOTHING, db_column='fkeysequence', blank=True, null=True)
    fkeymeasurement = models.ForeignKey(Measurement, models.DO_NOTHING, db_column='fkeymeasurement', blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'strain'


class Synonym(models.Model):
    synonym_id = models.IntegerField(primary_key=True)
    synonym_name = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    matching_hints_metadata = models.CharField(max_length=255, blank=True, null=True)
    ivd = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(db_column='DB_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'synonym'
