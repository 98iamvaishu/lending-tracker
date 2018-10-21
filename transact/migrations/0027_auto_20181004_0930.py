# Generated by Django 2.1 on 2018-10-04 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transact', '0026_auto_20180930_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lender',
            name='rec_amount',
        ),
        migrations.AddField(
            model_name='lender',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]