# Generated by Django 2.1 on 2018-09-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0021_borrower_intamt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paid',
            fields=[
                ('pay', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='transact.Borrower')),
                ('pamt', models.FloatField(blank=True, null=True)),
                ('iamt', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
