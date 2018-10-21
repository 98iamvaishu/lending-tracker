# Generated by Django 2.1 on 2018-09-26 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transact', '0016_auto_20180926_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('interest', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('terms', models.CharField(max_length=10)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('Initial_amount', models.IntegerField(blank=True, null=True)),
                ('rec_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='borrower',
            name='borrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transact.Lender'),
        ),
    ]
