# Generated by Django 3.2.13 on 2022-12-02 00:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('publication_year', models.CharField(max_length=100)),
                ('bookcover', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('like_user', models.ManyToManyField(related_name='like_book', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
