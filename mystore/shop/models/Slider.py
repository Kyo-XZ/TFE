from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120,blank=False, null=False)
    button_text = models.CharField(max_length=60,blank=False, null=False)
    button_link = models.CharField(max_length=255,blank=False, null=False)
    image = models.ImageField(upload_to="sliders", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
