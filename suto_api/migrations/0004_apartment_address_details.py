# Generated by Django 4.0.4 on 2022-07-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suto_api', '0003_alter_apartment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='address_details',
            field=models.CharField(default='', max_length=250),
        ),
    ]