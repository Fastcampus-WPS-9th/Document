# Generated by Django 2.1.2 on 2018-10-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_table', '0005_ancestor_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ancestor',
            name='name',
            field=models.CharField(db_column='name', max_length=10),
        ),
        migrations.AlterField(
            model_name='child',
            name='name2',
            field=models.CharField(db_column='name', max_length=20),
        ),
    ]
