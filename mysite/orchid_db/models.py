from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class Assignment(models.Model):
    orchid = models.ForeignKey('Orchid', models.DO_NOTHING)
    assign = models.IntegerField()
    label = models.IntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    alter_time = models.DateTimeField()
    m_user = models.ForeignKey('User', models.DO_NOTHING)
    m_alter_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'assignment'


class Award(models.Model):
    award_id = models.PositiveIntegerField(primary_key=True)
    orchid = models.IntegerField()
    org = models.ForeignKey('Organization', models.DO_NOTHING)
    award_name = models.CharField(max_length=5)
    point = models.PositiveIntegerField()
    jdate = models.DateField()
    cultivar = models.CharField(max_length=90)
    exhibition = models.CharField(max_length=130)
    ns = models.DecimalField(max_digits=3, decimal_places=1)
    nsv = models.DecimalField(max_digits=3, decimal_places=1)
    dsw = models.DecimalField(max_digits=3, decimal_places=1)
    dsl = models.DecimalField(max_digits=3, decimal_places=1)
    pw = models.DecimalField(max_digits=3, decimal_places=1)
    pl = models.DecimalField(max_digits=3, decimal_places=1)
    lsw = models.DecimalField(max_digits=3, decimal_places=1)
    lsl = models.DecimalField(max_digits=3, decimal_places=1)
    lpw = models.DecimalField(max_digits=3, decimal_places=1)
    lpl = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'award'


class Feature(models.Model):
    orchid = models.ForeignKey('Orchid', models.DO_NOTHING)
    feature_1 = models.CharField(max_length=5)
    feature_2 = models.CharField(max_length=5)
    feature_3 = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'feature'


class FeatureBook(models.Model):
    feature_id = models.CharField(primary_key=True, max_length=5)
    feature_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'feature_book'


class Genera(models.Model):
    genus_id = models.CharField(primary_key=True, max_length=5)
    genus_name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'genera'


class Image(models.Model):
    image_id = models.PositiveIntegerField(primary_key=True)
    orchid = models.ForeignKey('Orchid', models.DO_NOTHING)
    source = models.ForeignKey('Source', models.DO_NOTHING)
    award = models.ForeignKey(Award, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'image'


class NativeSpecies(models.Model):
    native_species_id = models.PositiveIntegerField(primary_key=True)
    accepted_id = models.PositiveIntegerField()
    orchid = models.ForeignKey('Orchid', models.DO_NOTHING)
    genus = models.ForeignKey(Genera, models.DO_NOTHING)
    species_name = models.CharField(max_length=50)
    accepted = models.IntegerField()
    var = models.IntegerField()
    ryear = models.PositiveSmallIntegerField()
    author = models.CharField(max_length=70, blank=True, null=True)
    publish = models.CharField(max_length=110, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'native_species'


class Orchid(models.Model):
    orchid_id = models.IntegerField(primary_key=True)
    genus = models.ForeignKey(Genera, models.DO_NOTHING)
    species_name = models.CharField(max_length=50)
    parent_seed = models.IntegerField()
    parent_pollen = models.IntegerField()
    ryear = models.SmallIntegerField()
    native_species = models.ForeignKey(NativeSpecies, models.DO_NOTHING)
    distribution = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'orchid'


class Organization(models.Model):
    org_id = models.CharField(primary_key=True, max_length=2)
    org_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'organization'


class Source(models.Model):
    source_id = models.PositiveIntegerField(primary_key=True)
    source_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'source'


class User(models.Model):
    user_id = models.PositiveSmallIntegerField(primary_key=True)
    user_name = models.CharField(max_length=10)
    user_passwords = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'

