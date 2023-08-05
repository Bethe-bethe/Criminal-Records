# Generated by Django 4.1.1 on 2022-09-20 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0009_criminal_prison_alter_criminal_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.RemoveField(
            model_name='criminal',
            name='Crime',
        ),
        migrations.AlterField(
            model_name='criminal',
            name='Height',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2.5)]),
        ),
        migrations.AddField(
            model_name='criminal',
            name='Crime',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
