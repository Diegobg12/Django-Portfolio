# Generated by Django 3.0.4 on 2020-05-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200316_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagecp',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
