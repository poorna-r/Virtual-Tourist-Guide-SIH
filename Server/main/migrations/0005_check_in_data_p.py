# Generated by Django 3.0.2 on 2020-02-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_check_in_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='check_in_data',
            name='p',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
