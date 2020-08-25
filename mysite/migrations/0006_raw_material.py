# Generated by Django 3.0.7 on 2020-08-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_delete_raw_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raw_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(default='media/my_stock.csv', upload_to='raw_material')),
            ],
        ),
    ]