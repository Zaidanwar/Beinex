# Generated by Django 2.2.6 on 2020-11-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201126_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]