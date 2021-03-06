# Generated by Django 3.1.13 on 2021-11-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_or_night', models.CharField(blank=True, choices=[('D', 'day'), ('N', 'night')], default='N', max_length=2, null=True)),
                ('favorite_day', models.CharField(blank=True, choices=[('Monday', 'monday'), ('Tuesday', 'tuesday'), ('Wednesday', 'wednesday'), ('Thursday', 'thursday'), ('Friday', 'friday'), ('Saturday', 'saturday'), ('Sunday', 'sunday')], default='friday', max_length=25, null=True)),
                ('favorite_color', models.CharField(blank=True, choices=[('Blue', 'blue'), ('Red', 'red'), ('Pink', 'pink'), ('Orange', 'orange'), ('Black', 'black'), ('White', 'white'), ('Purple', 'purple'), ('Green', 'green'), ('Yellow', 'yellow')], max_length=255, null=True)),
            ],
        ),
    ]
