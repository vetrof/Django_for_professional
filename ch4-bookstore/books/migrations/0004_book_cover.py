# Generated by Django 4.0.10 on 2023-06-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers'),
        ),
    ]
