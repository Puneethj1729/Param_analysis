# Generated by Django 3.0.7 on 2020-08-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_raw_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material',
            name='csv_file',
            field=models.FileField(default='settings.MEDIA_ROOT/my_stock.csv', upload_to='raw_material'),
        ),
    ]