# Generated by Django 2.1 on 2018-09-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0023_paid_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='terms',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]
