# Generated by Django 2.1.dev20180404232150 on 2018-04-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0002_auto_20180406_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='values',
            field=models.TextField(),
        ),
    ]
