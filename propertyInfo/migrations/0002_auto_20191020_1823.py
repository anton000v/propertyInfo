# Generated by Django 2.2.5 on 2019-10-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbuilding',
            name='micro_district',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Микрорайон'),
        ),
    ]