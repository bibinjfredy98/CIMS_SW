#models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from math import isnan
import math
from django.db import IntegrityError
import json
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from datetime import timedelta






class Building(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField('Room', related_name='buildings')


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = Building.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)



class Cluster(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    rooms = models.ManyToManyField('Room', related_name='clusters')

    buildings = models.ManyToManyField('Building', related_name='clusters')  # Group by buildings
    power_modules = models.ManyToManyField('PowerModule', related_name='clusters')  # Group by power modules
    main_admins = models.ManyToManyField('MainAdmin', related_name='clusters', blank=True)  # Main admins managing the cluster
    sub_admins = models.ManyToManyField('SubAdmin', related_name='clusters', blank=True)  # Sub-admins managing the cluster


    

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = Cluster.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)
    
    
class MqttDevice(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='both', default='0.0.0.0')
    topic_name = models.CharField(max_length=255, default='')
    

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = MqttDevice.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)
    


class Room(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='both',default='0.0.0.0') 
    topic_name = models.CharField(max_length=255,default='')
    main_admins = models.ManyToManyField('MainAdmin', related_name='rooms', blank=True)
    sub_admins = models.ManyToManyField('SubAdmin', related_name='rooms', blank=True)
    sensor_data = models.ManyToManyField('SensorData', related_name='rooms', blank=True)  # Add this field
    temperature_threshold = models.FloatField(default=0)
    humidity_threshold = models.FloatField(default=0)
    door_state_threshold = models.CharField(max_length=100)  # Add this field if needed
    flood_state_threshold  = models.CharField(max_length=100) # Add this field if needed
    pir_state_threshold  = models.CharField(max_length=100)  # Add this field if needed
    gas_state_threshold  = models.CharField(max_length=100)  # Add this field if needed
    interval = models.IntegerField(default=0)  # Field to store interval in seconds
    # creator_type = models.CharField(max_length=10)  # Store the type of creator (MainAdmin or SubAdmin)
    # creator_id = models.PositiveIntegerField()     # Store the ID of the creator

    temperature_alerts = models.CharField(max_length=255, blank=True)
    humidity_alerts = models.CharField(max_length=255, blank=True)
    door_alerts = models.CharField(max_length=255, blank=True)
    flood_alerts = models.CharField(max_length=255, blank=True)
    pir_alerts = models.CharField(max_length=255, blank=True)
    gas_alerts = models.CharField(max_length=255, blank=True)


    gsm_alert = models.CharField(max_length=10, default='disable')
    # gsm_numbers = models.CharField(max_length=1000, blank=True)
    gsm_numbers = models.JSONField(default=list, blank=True)  # Modify this field if needed

    alert_mqtt_device = models.ManyToManyField('MqttDevice', related_name='alert_mqtt_devices', blank=True)
    
    



    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = Room.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)


    def is_active(self):
        """Check if the room is active by looking at the latest sensor data."""
        last_5_minutes = timezone.now() - timedelta(minutes=5)
        return self.sensor_data.filter(timestamp__gte=last_5_minutes).exists()

    def is_inactive(self):
        """Check if the room is inactive by checking if it's not active."""
        return not self.is_active()   
    
     



class Alert(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='alerts')
    type = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)  # Add this field  

    marked_by = models.CharField(max_length=255, null=True, blank=True)  # Store the name of the user
    marked_by_type = models.CharField(max_length=50, null=True, blank=True)  # 'MainAdmin' or 'SubAdmin'

    viewed_by = models.CharField(max_length=100, blank=True, null=True)  # New field to store the user who marked as viewed
    viewed_at = models.DateTimeField(blank=True, null=True)  # New field to store when it was viewed



    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = Alert.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)    
  





class GsmModule(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    module_name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='both', default='0.0.0.0')
    topic_name = models.CharField(max_length=255, default='')
    numbers = models.JSONField(default=list)
    mobile_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.module_name
    

    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = GsmModule.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)
    


class SensorData(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField(null=True, blank=True)  # Adjust data types as needed
    humidity = models.FloatField(null=True, blank=True)
    doorState = models.BooleanField(null=True, blank=True)  # Boolean for opened/closed
    floodState = models.BooleanField(null=True, blank=True)  # Boolean for detected/not detected
    pirState = models.BooleanField(null=True, blank=True)  # Boolean for motion detected/not detected
    gasState = models.BooleanField(null=True, blank=True)  # Boolean for motion detected/not detected
    
    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = SensorData.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)    


class MainAdmin(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ManyToManyField(Room, blank=True)  # Allow MainAdmin to have no linked rooms
    @property
    def is_main_admin(self):
        return True
    
    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = MainAdmin.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)




class SubAdmin(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, null=True)
    building = models.ManyToManyField('Building', related_name='sub_admins', blank=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(MainAdmin, on_delete=models.SET_NULL, null=True)

    suspended = models.BooleanField(default=False)  # New field for suspension status

    

    # Add a method to approve the sub-admin

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.username 


    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = SubAdmin.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)
   
    
  
class PowerModule(models.Model):
    custom_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol='both', default='0.0.0.0')
    topic_name = models.CharField(max_length=255, default='')
    rooms = models.ManyToManyField('Room', related_name='powermodule')
    ct1 = models.FloatField(default=0.0)  
    ct2 = models.FloatField(default=0.0)  
    ct3 = models.FloatField(default=0.0)  
    ct4 = models.FloatField(default=0.0)  
    ct1correspondingname =  models.CharField(max_length=100)
    ct2correspondingname =  models.CharField(max_length=100)
    ct3correspondingname =  models.CharField(max_length=100)
    ct4correspondingname =  models.CharField(max_length=100)
    buildings = models.ManyToManyField(Building, related_name='power_modules', blank=True)  # Added field


    def save(self, *args, **kwargs):
        if not self.custom_id:
            max_id = PowerModule.objects.aggregate(max_id=models.Max('custom_id'))['max_id']
            self.custom_id = max_id + 1 if max_id is not None else 1
        super().save(*args, **kwargs)


class PowerData(models.Model):
    power_module = models.ForeignKey(PowerModule, on_delete=models.CASCADE)
    ct1 = models.FloatField()
    ct2 = models.FloatField()
    ct3 = models.FloatField()
    ct4 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

###############################################

