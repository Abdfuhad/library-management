# Generated by Django 5.0.2 on 2024-03-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_publisher_remove_book_publisher_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
