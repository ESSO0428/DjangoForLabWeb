# Generated by Django 3.2 on 2023-03-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phal_db_n2', '0002_alter_v3deg_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='v3deg',
            name='id',
        ),
        migrations.AddField(
            model_name='v3deg',
            name='django_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
