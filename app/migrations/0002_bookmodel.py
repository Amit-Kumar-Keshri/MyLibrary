# Generated by Django 3.2.3 on 2021-06-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
    ]
