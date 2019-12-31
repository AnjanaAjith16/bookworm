# Generated by Django 2.2.6 on 2019-12-22 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]