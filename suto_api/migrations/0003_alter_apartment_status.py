# Generated by Django 4.0.4 on 2022-07-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suto_api', '0002_apartment_photo_10_apartment_photo_11_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.CharField(choices=[('С', 'Свободный'), ('З', 'Занят')], default='С', max_length=1),
        ),
    ]
