# Generated by Django 3.2.7 on 2021-09-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soliproducts', '0003_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
