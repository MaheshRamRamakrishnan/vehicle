# Generated by Django 4.0.5 on 2022-09-28 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_buyer_data_delete_buyer_details_1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buyer_data',
        ),
    ]