# Generated by Django 2.2.6 on 2020-11-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
