# Generated by Django 3.2.7 on 2021-09-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soliproducts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]