"""
from django.contrib import admin

# Register your models here.
"""

from django.contrib import admin
from .models        import Post, Product
from .models import DegradomeResult
#from Post          import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pumps', 'pub_date')

class DegradomeAdmin(admin.ModelAdmin):
    list_display = ('DataSet' , 'Tissue', 'Transcript_ID', 'BLAST_ATH_protein', 'Category', 'Cleavage_Position'	,'miRNA_ID'	,'FM_miRNA'	,'x5BL_miRNA', 'x5BP_miRNA', 'x5BS_miRNA', 'FM_target', 'x5BL_target', 'x5BP_target', 'x5BS_target', 'miRNA_aligned_fragment', 'alignment', 'Target_aligned_fragment', 'Target_Desc')
    # list_display = ('Set' , 'Tissue', 'BLAST_ATH_protein', 'Category', 'Cleavage_Position'	,'miRNA_ID'	,'FM_miRNA'	,'x5BL_miRNA', 'x5BP_miRNA', 'x5BS_miRNA', 'FM_target', 'x5BL_target', 'x5BP_target', 'x5BS_target', 'miRNA_aligned_fragment', 'alignment', 'Target_aligned_fragment', 'Target_Desc')
    # list_display = ('Set' , 'Tissue', 'Transcript_ID', 'blast_protein', 'Category', 'Cleavage_Position'	,'miRNA_ID'	,'FM_miRNA'	,'x5BL_miRNA', 'x5BP_miRNA', 'x5BS_miRNA', 'FM_target', 'x5BL_target', 'x5BP_target', 'x5BS_target', 'miRNA_aligned_fragment', 'alignment', 'Target_aligned_fragment', 'Target_Desc')

admin.site.register(Post   , PostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(DegradomeResult, DegradomeAdmin)

