# Generated by Django 5.0.2 on 2024-03-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
