# Generated by Django 4.2.7 on 2023-12-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacist', '0002_remove_medicine_pharmacies_alter_pharmacy_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]