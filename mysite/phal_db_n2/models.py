from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# NOTE: 通過 settings.py 在 DATABASES 和 DATABASE_APPS_MAPPING 的設定可讓我們連結 mysql 的 database
# NOTE: DATABASES 主要設定要連結的 mysql 內的 database 有哪些
# NOTE: DATABASE_APPS_MAPPING 則是設定 APP directory 內使用 models.py 會連結到的 database
# NOTE: models.py 則用來取出前面提到的 database 的 table
# NOTE: 使用 models.py 若要抓到整個 table 要像底下一樣，全部的 column 都要再指定一次
# NOTE: 當然我們也可以用 python manage.py inspectdb 來自動化完成這個步驟
class V3Deg(models.Model):
    id = models.BigAutoField(db_column='Django_id', auto_created=True, primary_key=True, serialize=False)
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
        db_table = 'V3_deg'


