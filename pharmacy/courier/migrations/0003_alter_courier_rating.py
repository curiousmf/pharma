# Generated by Django 4.2.1 on 2023-12-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_remove_courier_name_remove_courier_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]