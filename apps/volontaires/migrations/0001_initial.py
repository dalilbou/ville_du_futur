# Generated by Django 5.0 on 2024-08-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(verbose_name='Heure de début')),
                ('end_date', models.DateField(verbose_name='Heure de fin')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('monday_all_day', models.BooleanField(default=False)),
                ('monday_morning', models.BooleanField(default=False)),
                ('monday_afternoon', models.BooleanField(default=False)),
                ('monday_evening', models.BooleanField(default=False)),
                ('tuesday_all_day', models.BooleanField(default=False)),
                ('tuesday_morning', models.BooleanField(default=False)),
                ('tuesday_afternoon', models.BooleanField(default=False)),
                ('tuesday_evening', models.BooleanField(default=False)),
                ('wednesday_all_day', models.BooleanField(default=False)),
                ('wednesday_morning', models.BooleanField(default=False)),
                ('wednesday_afternoon', models.BooleanField(default=False)),
                ('wednesday_evening', models.BooleanField(default=False)),
                ('thursday_all_day', models.BooleanField(default=False)),
                ('thursday_morning', models.BooleanField(default=False)),
                ('thursday_afternoon', models.BooleanField(default=False)),
                ('thursday_evening', models.BooleanField(default=False)),
                ('friday_all_day', models.BooleanField(default=False)),
                ('friday_morning', models.BooleanField(default=False)),
                ('friday_afternoon', models.BooleanField(default=False)),
                ('friday_evening', models.BooleanField(default=False)),
                ('saturday_all_day', models.BooleanField(default=False)),
                ('saturday_morning', models.BooleanField(default=False)),
                ('saturday_afternoon', models.BooleanField(default=False)),
                ('saturday_evening', models.BooleanField(default=False)),
                ('sunday_all_day', models.BooleanField(default=False)),
                ('sunday_morning', models.BooleanField(default=False)),
                ('sunday_afternoon', models.BooleanField(default=False)),
                ('sunday_evening', models.BooleanField(default=False)),
            ],
        ),
    ]
