# Generated by Django 2.1 on 2018-10-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0029_auto_20181014_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
