# Generated by Django 4.0.5 on 2022-09-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_seller_details_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_details',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
