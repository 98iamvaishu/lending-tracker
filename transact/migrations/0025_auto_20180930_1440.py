# Generated by Django 2.1 on 2018-09-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0024_auto_20180930_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='terms',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
