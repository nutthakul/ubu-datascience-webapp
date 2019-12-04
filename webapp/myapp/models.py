from django.db import models

# Create your models here.
class PrimeMinister(models.Model):
    #fields
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 500)
    bod = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField()
    imgurl = models.CharField(max_length= 500, default='')
    party = models.CharField(max_length= 500, default='')
    def __str__(self):
        return f'{self.name} จากพรรค {self.party}'