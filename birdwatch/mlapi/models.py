import os
from django.db import models
from datetime import datetime

# Create your models here.


class Birds(models.Model):
    common_name = models.CharField(max_length=254)
    scientific_name = models.CharField(max_length=254)
    probable_age =  models.CharField(max_length=254)
    

class BirdsStatus(models.Model):
    status_code = models.CharField(max_length=50, primary_key=True)
    status_name = models.CharField(max_length=254)
    # status_image = models.ImageField()

class BirdsDetail(models.Model):
    status_code = models.ForeignKey(BirdsStatus, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=254)
    scientific_name = models.CharField(max_length=254, primary_key=True)  # Set primary_key to CharField
    birds_description = models.TextField()
    birds_image = models.ImageField()
    
    def save(self, *args, **kwargs):
        # Append current datetime to the filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename, file_extension = os.path.splitext(self.birds_image.name)
        new_filename = f"{filename}_{timestamp}{file_extension}"

        # Update the birds_image field with the new filename
        self.birds_image.name = new_filename

        super().save(*args, **kwargs)


class NodeDevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    scientific_name = models.ForeignKey(
        BirdsDetail,
        on_delete=models.CASCADE,
        to_field='scientific_name'  # Add this line
    )
    node_id = models.CharField(max_length=254)
    node_location = models.CharField(max_length=254)
    node_date = models.CharField(max_length=254)
    node_time = models.CharField(max_length=254)
    node_image = models.ImageField() 
    
    
    #The following function appends current date time upto seconds so that every image will be uniquely stored in the database
    def save(self, *args, **kwargs):
        # Append current datetime to the filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename, file_extension = os.path.splitext(self.node_image.name)
        new_filename = f"{filename}_{timestamp}{file_extension}"

        # Update the birds_image field with the new filename
        self.node_image.name = new_filename

        super().save(*args, **kwargs)  

  
# class ReceivedBirdsCollection(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     node_id = models.ForeignKey(NodeDevice, on_delete=models.CASCADE)
#     scientific_name = models.ForeignKey(BirdsDetail, on_delete=models.CASCADE)
    
    
    
    
    

    
    