# Generated by Django 2.1 on 2018-10-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0030_auto_20181014_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]