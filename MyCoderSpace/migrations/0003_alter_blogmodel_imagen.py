# Generated by Django 4.0.4 on 2022-06-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCoderSpace', '0002_blogmodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
