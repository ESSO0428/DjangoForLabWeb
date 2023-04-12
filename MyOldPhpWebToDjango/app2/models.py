from enum                      import unique
from django.db                 import models
from django.utils              import timezone
from django.db.models.signals  import pre_save
from django.utils.text         import slugify
# Create your models here.

class Post(models.Model):
    title    = models.CharField(max_length=200)
    slug     = models.CharField(max_length=200)
    body     = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



class Product(models.Model):
    PUMPS = (
        ('L', 'Log'   ),
        ('E', 'Erro'  ),
        ('O', 'Other' ),
    )
    title    = models.CharField(max_length=200)
    # slug     = models.SlugField(unique=True)
    body     = models.TextField()
    pumps    = models.CharField(max_length=1, choices=PUMPS)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# class DegradomeResult(models.Model):
#     DataSet                 = models.CharField(max_length=200)
#     Tissue                  = models.CharField(max_length=200)
#     Transcript_ID           = models.CharField(max_length=200)
#     BLAST_ATH_protein       = models.CharField(max_length=200)
#     Category                = models.IntegerField()
#     Cleavage_Position       = models.IntegerField()
#     miRNA_ID                = models.CharField(max_length=200)

#     FM_miRNA                = models.FloatField()
#     x5BL_miRNA              = models.FloatField()
#     x5BP_miRNA              = models.FloatField()
#     x5BS_miRNA              = models.FloatField()


#     FM_target               = models.FloatField()
#     x5BL_target             = models.FloatField()
#     x5BP_target             = models.FloatField()
#     x5BS_target             = models.FloatField()

#     miRNA_aligned_fragment  = models.CharField(max_length=200)
#     alignment               = models.CharField(max_length=200)
#     Target_aligned_fragment = models.CharField(max_length=200)
#     Target_Desc             = models.CharField(max_length=200)

#     # class Meta:
#     #     ordering = ('-pub_date',)

#     # def __unicode__(self):
#     #     return self.miRNA_ID

#     # def __str__(self):
#     #     return self.miRNA_ID

# from django.utils.translation import gettext as _
# class DegradomeResult(models.Model):
#     DataSet                 = models.CharField(_('DataSet'), max_length=200)
#     Tissue                  = models.CharField(_('Tissue'), max_length=200)
#     Transcript_ID           = models.CharField(_('Transcript_ID'), max_length=200)
#     BLAST_ATH_protein       = models.CharField(_('BLAST_ATH_protein'), max_length=200)
#     Category                = models.IntegerField(_('Category'), default=0)
#     Cleavage_Position       = models.IntegerField(_('Cleavage_Position'), default=0)
#     miRNA_ID                = models.CharField(max_length=200)

#     FM_miRNA                = models.FloatField(_('FM_miRNA'), default=0)
#     x5BL_miRNA              = models.FloatField(_('5BL_miRNA'), default=0)
#     x5BP_miRNA              = models.FloatField(_('5BP_miRNA'), default=0)
#     x5BS_miRNA              = models.FloatField(_('5BS_miRNA'), default=0)


#     FM_target               = models.FloatField(_('FM_target'), default=0)
#     x5BL_target             = models.FloatField(_('5BL_target'), default=0)
#     x5BP_target             = models.FloatField(_('5BP_target'), default=0)
#     x5BS_target             = models.FloatField(_('5BS_target'), default=0)

#     miRNA_aligned_fragment  = models.CharField(_('miRNA_aligned_fragment'), max_length=200)
#     alignment               = models.CharField(_('alignment'), max_length=200)
#     Target_aligned_fragment = models.CharField(_('Target_aligned_fragment'), max_length=200)
#     Target_Desc             = models.CharField(_('Target_Desc'), max_length=200)

#     class Meta:
#         db_table = 'DegradomeResult'



# def create_slug(instance):
#     slug = slugify(instance.title)
#     qs = Product.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "{0}-{1}".format(slug, qs.first().id)
#         return new_slug
#     return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, sender=Product)

# def create_slug(instance):
#     slug = slugify(instance.title)
#     qs = Product.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "{0}-{1}".format(slug, qs.first().id)
#         return new_slug
#     return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, sender=Product)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Degradomeresult(models.Model):
    dataset = models.CharField(db_column='DataSet', max_length=100, verbose_name='DataSet')  # Field name made lowercase.
    tissue = models.CharField(db_column='Tissue', max_length=100, verbose_name='Tissue')  # Field name made lowercase.
    transcript_id = models.CharField(db_column='Transcript_ID', max_length=100, verbose_name='Transcript_ID')  # Field name made lowercase.
    blast_ath_protein = models.CharField(db_column='BLAST_ATH_protein', max_length=100, verbose_name='BLAST_ATH_protein')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100, verbose_name='Category')  # Field name made lowercase.
    cleavage_position = models.FloatField(db_column='Cleavage_Position', verbose_name='Cleavage_Position')  # Field name made lowercase.
    mirna_id = models.CharField(db_column='miRNA_ID', max_length=100, verbose_name='miRNA_ID')  # Field name made lowercase.
    fm_mirna = models.FloatField(db_column='FM_miRNA', verbose_name='FM_miRNA')  # Field name made lowercase.
    number_5bl_mirna = models.FloatField(db_column='5BL_miRNA', verbose_name='5BL_miRNA')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5bp_mirna = models.FloatField(db_column='5BP_miRNA', verbose_name='5BP_miRNA')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5bs_mirna = models.FloatField(db_column='5BS_miRNA', verbose_name='5BS_miRNA')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fm_target = models.FloatField(db_column='FM_target', verbose_name='FM_target')  # Field name made lowercase.
    number_5bl_target = models.FloatField(db_column='5BL_target', verbose_name='5BL_target')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5bp_target = models.FloatField(db_column='5BP_target', verbose_name='5BP_target')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5bs_target = models.FloatField(db_column='5BS_target', verbose_name='5BS_target')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    mirna_aligned_fragment = models.CharField(db_column='miRNA_aligned_fragment', max_length=100, verbose_name='miRNA_aligned_fragment')  # Field name made lowercase.
    alignment = models.CharField(max_length=100)
    target_aligned_fragment = models.CharField(db_column='Target_aligned_fragment', max_length=100, verbose_name='Target_aligned_fragment')  # Field name made lowercase.
    target_desc = models.CharField(db_column='Target_Desc', max_length=5000, verbose_name='Target_Desc')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DegradomeResult'
