from django.db import models

class Member(models.Model):
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.uname

class Home_media(models.Model):
    name = models.CharField(max_length=50) 
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    url = models.CharField(null = True, blank=True, max_length=50000) 
    
    def __str__(self):
        return self.name
    
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
    
# XENOS

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
   
    def __str__(self):
        return str(self.name)
    
#SWARM  
class Tyranid_s(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")   
    def __str__(self):
        return self.unit
    
class Tyranid_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
    unit11 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit11')
    unit12 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit12')
    unit13 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit13')
    unit14 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit14')
    unit15 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit15')
    unit16 = models.ForeignKey(Tyranid_s, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit16')
    
    
    def __str__(self):
        return self.name
    
#ELDAR_G
class Eldar_g(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")   
    def __str__(self):
        return self.unit
    
class Eldarg_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Eldar_g, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')

    def __str__(self):
        return self.name
    
#PATHFINDERS 
class Tau_p(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")   
    def __str__(self):
        return self.unit
    
class Pathfinder_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
    unit11 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit11')
    unit12 = models.ForeignKey(Tau_p, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit12')
    
    def __str__(self):
        return self.name

#IMPERIUM
  
#KRIEG    
class Krieg(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")   
    def __str__(self):
        return self.unit
    
class Krieg_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Krieg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
    
    def __str__(self):
        return self.name
      
#SOB    
class Sister(models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit
    
class sister_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Sister, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
       
    def __str__(self):
        return self.name
    
    
#PRIMARIS MARINES
class Pm (models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit
    
class Pm_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Pm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
     
    def __str__(self):
        return self.name
    
#CHAOS

#CHAOS MARINES
class Cm (models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit
    
class Cm_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Cm, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
     
    def __str__(self):
        return self.name
    
#BLOODIED
class Bloodied (models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit

class Bloodied_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
    unit05 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit05')
    unit06 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit06')
    unit07 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit07')
    unit08 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit08')
    unit09 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit09')
    unit10 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit10')
    unit11 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit11')
    unit12 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit12')
    unit13 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit13')
    unit14 = models.ForeignKey(Bloodied, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit14')
    
    def __str__(self):
        return self.name


#DEATH GUARD
class Dg (models.Model):
    unit = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.unit
    
class Dg_list(models.Model):
    name  = models.CharField(max_length=500)
    unit01 = models.ForeignKey(Dg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit01')
    unit02 = models.ForeignKey(Dg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit02')
    unit03 = models.ForeignKey(Dg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit03')
    unit04 = models.ForeignKey(Dg, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='unit04')
   
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    