# Generated by Django 5.0.2 on 2024-04-07 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_alter_book_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateField(default=datetime.date(2024, 4, 7)),
        ),
    ]
