# Generated by Django 3.1.13 on 2021-11-28 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0003_auto_20211128_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='favorite_color',
            field=models.CharField(blank=True, choices=[('blue', 'Blue'), ('red', 'Red'), ('pink', 'Pink'), ('orange', 'Orange'), ('black', 'Black'), ('white', 'White'), ('purple', 'Purple'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=255, null=True),
        ),
    ]
