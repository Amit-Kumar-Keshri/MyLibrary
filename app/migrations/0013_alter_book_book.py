# Generated by Django 3.2 on 2021-06-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_book_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(upload_to='books/'),
        ),
    ]
