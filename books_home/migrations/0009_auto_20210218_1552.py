# Generated by Django 2.2.13 on 2021-02-18 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_home', '0008_auto_20210218_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 18, 15, 52, 27, 345524)),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(choices=[('programming', 'programming'), ('social', 'social'), ('politics', 'politics'), ('fitness', 'fitness'), ('maths', 'maths')], max_length=100, null=True),
        ),
    ]
