# Generated by Django 2.2.5 on 2019-10-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyInfo', '0006_remove_newbuilding_micro_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbuilding',
            name='micro_district',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
