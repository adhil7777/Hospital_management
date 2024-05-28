from django.db import models

# Create your models here.
class oreg_tbl(models.Model):
    fn = models.CharField(max_length=50)
    ln = models.CharField(max_length=50)
    db = models.DateField()
    email = models.EmailField()
    cltdp = models.CharField(max_length=50)
    cltme = models.TimeField()

class renewal_tbl(models.Model):
    fnm = models.CharField(max_length=50)
    adr = models.CharField(max_length=50)
    db = models.DateField()
    em = models.EmailField(max_length=50)
    phn = models.IntegerField()
    ipdr = models.CharField(max_length=50)
    ipnm = models.IntegerField()

class emergency_tbl(models.Model):
    pnm = models.CharField(max_length=50)
    age = models.IntegerField()
    plc = models.CharField(max_length=50)
    cdn = models.CharField(max_length=50)




