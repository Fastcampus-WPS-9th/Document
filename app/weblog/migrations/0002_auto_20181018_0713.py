# Generated by Django 2.1.2 on 2018-10-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
