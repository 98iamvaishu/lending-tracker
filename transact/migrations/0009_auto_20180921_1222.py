# Generated by Django 2.1 on 2018-09-21 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0008_borrower_lender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lender',
            name='borrow',
        ),
        migrations.AddField(
            model_name='borrower',
            name='borrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transact.Lender'),
        ),
    ]
