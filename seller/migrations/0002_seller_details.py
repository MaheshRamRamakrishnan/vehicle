# Generated by Django 4.0.5 on 2022-09-26 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seller_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('employment', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('zip', models.PositiveBigIntegerField(null=True)),
                ('place', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('code', models.PositiveBigIntegerField(null=True)),
                ('phone', models.PositiveBigIntegerField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
