# Generated by Django 4.2.6 on 2023-10-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_cartdetails_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetails',
            name='cusname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
