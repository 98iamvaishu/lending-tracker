# Generated by Django 2.1 on 2018-10-15 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0034_auto_20181015_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='lender',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='transact.Lender'),
        ),
    ]