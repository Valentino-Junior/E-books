# Generated by Django 3.2.9 on 2022-01-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_remove_book_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='library.Tag'),
        ),
    ]
