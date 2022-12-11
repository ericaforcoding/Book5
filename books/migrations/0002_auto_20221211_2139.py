# Generated by Django 3.2.13 on 2022-12-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookcover',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='class_nm',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=1000),
        ),
    ]
