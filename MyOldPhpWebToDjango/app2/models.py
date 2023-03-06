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


class DegradomeResult(models.Model):
    DataSet                 = models.CharField(max_length=200)
    Tissue                  = models.CharField(max_length=200)
    Transcript_ID           = models.CharField(max_length=200)
    BLAST_ATH_protein       = models.CharField(max_length=200)
    Category                = models.IntegerField()
    Cleavage_Position       = models.IntegerField()
    miRNA_ID                = models.CharField(max_length=200)

    FM_miRNA                = models.FloatField()
    x5BL_miRNA              = models.FloatField()
    x5BP_miRNA              = models.FloatField()
    x5BS_miRNA              = models.FloatField()


    FM_target               = models.FloatField()
    x5BL_target             = models.FloatField()
    x5BP_target             = models.FloatField()
    x5BS_target             = models.FloatField()

    miRNA_aligned_fragment  = models.CharField(max_length=200)
    alignment               = models.CharField(max_length=200)
    Target_aligned_fragment = models.CharField(max_length=200)
    Target_Desc             = models.CharField(max_length=200)

    # class Meta:
    #     ordering = ('-pub_date',)

    # def __unicode__(self):
    #     return self.miRNA_ID

    # def __str__(self):
    #     return self.miRNA_ID

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

