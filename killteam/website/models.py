from django.db import models

class Member(models.Model):
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.uname
    
class Xeno(models.Model):
    Fac_name = models.CharField(max_length=50)
    Fac_rule = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.Fac_name
    
class Imperium(models.Model):
    Fac_name = models.CharField(max_length=50)
    Fac_rule = models.CharField(max_length=5000)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.Fac_name
    
class Chao(models.Model):
    Fac_name = models.CharField(max_length=50)
    Fac_rule = models.CharField(max_length=5000)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.Fac_name
    
# KOMMANDOS
class Kommando(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit
    
class Kommand_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Kommando, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
    
    class meta:
        db_table = "website_kommand_list"    
    def __str__(self):
        return self.name
    
#KRIEG
    
class Krieg(models.Model):
    unit = models.CharField(max_length=50)
    m = models.IntegerField()
    apl = models.IntegerField()
    ga = models.IntegerField()
    df = models.IntegerField()
    sv = models.IntegerField()
    w = models.IntegerField()
    
    def __str__(self):
        return self.unit
    
class Sister(models.Model):
    unit = models.CharField(max_length=50)
    m = models.IntegerField()
    apl = models.IntegerField()
    ga = models.IntegerField()
    df = models.IntegerField()
    sv = models.IntegerField()
    w = models.IntegerField()
    
    def __str__(self):
        return self.unit
    
    
    