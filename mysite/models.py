from django.db import models
import datetime

class Inventory(models.Model):
    title=models.CharField(max_length=200)
    csv_file=models.FileField(upload_to='inventory')
    date=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
class Raw_material(models.Model):
    csv_file=models.FileField(upload_to='raw_material',default='settings.MEDIA_ROOT/my_stock.csv')

