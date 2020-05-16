# Generated by Django 2.0.2 on 2018-04-04 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180317_2019'),
        ('booking', '0007_auto_20180404_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=15)),
                ('pickup_location', models.CharField(max_length=30)),
                ('dropoff_location', models.CharField(max_length=30)),
                ('pickup_date', models.CharField(max_length=15)),
                ('pickup_time', models.CharField(max_length=15)),
                ('dropoff_date', models.CharField(max_length=15)),
                ('dropoff_time', models.CharField(max_length=15)),
                ('driver', models.CharField(max_length=15)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.register')),
            ],
        ),
    ]
