# Generated by Django 2.2.13 on 2021-02-17 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_home', '0003_auto_20210217_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 18, 24, 24, 360983)),
        ),
    ]
