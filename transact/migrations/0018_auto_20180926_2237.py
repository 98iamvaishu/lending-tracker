# Generated by Django 2.1 on 2018-09-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0017_auto_20180926_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='terms',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
