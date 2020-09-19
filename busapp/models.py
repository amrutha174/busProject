from django.db import models

# Create your models here.
class Busbooking(models.Model):
	NAME = models.CharField( max_length=50)
	EMAIL = models.EmailField()
	PH_NO  = models.CharField( max_length=12)
	class Meta:
		verbose_name = "Busbooking"
		verbose_name_plural = "Busbookings"
	def __str__(self):
		return NAME

class Welcome_Form(models.Model):
	FROM= models.CharField(max_length=50)
	TO= models.CharField(max_length=50)
	BUSNAME = models.CharField(max_length=50)
	BUSTIME = models.DecimalField( max_digits=5, decimal_places=2)
	class Meta:
		verbose_name = "Welcome_Form"
		verbose_name_plural = "Welcome_Forms"
    