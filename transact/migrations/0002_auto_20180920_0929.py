# Generated by Django 2.1 on 2018-09-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lender',
            name='Interest',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='lender',
            name='amount',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lender',
            name='duration',
            field=models.IntegerField(max_length=5),
        ),
    ]
