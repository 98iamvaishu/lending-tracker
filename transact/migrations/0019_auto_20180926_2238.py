# Generated by Django 2.1 on 2018-09-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0018_auto_20180926_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='terms',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
