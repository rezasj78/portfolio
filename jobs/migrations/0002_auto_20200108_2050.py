# Generated by Django 2.2.9 on 2020-01-08 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='image',
            new_name='imagefun',
        ),
    ]
