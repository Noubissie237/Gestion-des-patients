# Generated by Django 4.2.6 on 2023-12-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]