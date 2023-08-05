from django.db import models

# Create your models here.
 
class CentralPrison(models.Model):
    Name=models.CharField(max_length=100,default="Amhara Prison commision") 
    
    def __str__(self):
        return self.Name
        
 
class Prison(models.Model): 
    PrisonName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Region = models.ForeignKey(CentralPrison,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.PrisonName