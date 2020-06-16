from django.db import models
from django.urls import reverse 
# Create your models here.

class Item(models.Model):
	item_text = models.CharField(max_length=32)
	done = models.BooleanField(default=False)
	
	def __str__(self):
		return self.item_text
		
	#def get_absolute_url(self):
	#	return reverse('item-detail', kwargs={'pk':self.pk})
		
		
	

	
	
	

