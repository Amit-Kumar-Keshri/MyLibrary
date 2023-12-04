# Generated by Django 3.2 on 2021-06-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_book_book_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_file',
        ),
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.FileField(default='lol', upload_to='books/'),
            preserve_default=False,
        ),
    ]