# Generated by Django 4.0.5 on 2022-08-28 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0001_initial'),
        ('record', '0004_rename_createdby_prison_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prison',
            name='Region',
        ),
        migrations.RemoveField(
            model_name='prison',
            name='admin',
        ),
        migrations.AlterField(
            model_name='criminal',
            name='PrisonName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prison.prison'),
        ),
        migrations.DeleteModel(
            name='CentralPrison',
        ),
        migrations.DeleteModel(
            name='Prison',
        ),
    ]