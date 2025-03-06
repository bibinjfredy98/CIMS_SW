
#views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import SubAdmin
from .models import MainAdmin
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseServerError
from django.contrib.auth import logout
from django.contrib import messages
from .forms import AddRoomForm
from .models import Room
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import SensorData
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import paho.mqtt.client as mqtt
from .models import Room, SensorData
import json
from django.conf import settings
import logging
import time
import threading
from math import isnan
import math
from .models import Room, Alert
from django.template.loader import render_to_string
from .models import Alert
from django.views.decorators.http import require_POST
from django.utils.timezone import localtime
from datetime import datetime
import paho.mqtt.publish as publish
import datetime
from django.utils import timezone
from django.utils.timezone import is_aware
from datetime import timedelta
from datetime import datetime, timedelta
from threading import Timer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.views.decorators.http import require_GET
import random
from .models import MqttDevice, GsmModule
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import Q
# from .models import PowerMqttDevice, PowerSourceConfig
from django.core.cache import cache
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import EditThresholdForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from .models import Building, Room, MainAdmin, SubAdmin, Alert, MqttDevice, GsmModule,PowerModule
from .forms import AddBuildingForm, EditBuildingForm, AddRoomForm
from .forms import AddClusterForm
from .models import Cluster
from .forms import AddClusterForm, EditClusterForm,SelectBuildingsForm
from django.utils.timezone import now, timedelta
from django.db.models import Count
from django.db.models import Avg
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import localtime
import csv
import io
from django.db.models import Avg, F
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.utils.timezone import localtime
from .models import Alert, Room, SubAdmin, Building
from django.db import models
from django.db.models import Avg, Count, Q
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
from .models import SubAdmin, Building, Room, MainAdmin, SensorData
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta
from django.core.paginator import Paginator
from django.utils.timezone import localtime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SubAdmin, Room, Alert
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import PowerModule
from .forms import PowerModuleForm
from .models import Room, SensorData, PowerModule, PowerData, MqttDevice, GsmModule
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateparse import parse_datetime
from django.db.models import Q
from datetime import datetime, timedelta
import json









@receiver(post_delete, sender=Room)
def renumber_custom_ids(sender, instance, **kwargs):
    rooms = Room.objects.all().order_by('custom_id')
    for i, room in enumerate(rooms, start=1):
        if room.custom_id != i:
            room.custom_id = i
            room.save(update_fields=['custom_id'])


@receiver(post_delete, sender=Building)
def renumber_building_custom_ids(sender, instance, **kwargs):
    buildings = Building.objects.all().order_by('custom_id')
    for i, building in enumerate(buildings, start=1):
        if building.custom_id != i:
            building.custom_id = i
            building.save(update_fields=['custom_id'])

@receiver(post_delete, sender=Cluster)
def renumber_cluster_custom_ids(sender, instance, **kwargs):
    clusters = Cluster.objects.all().order_by('custom_id')
    for i, cluster in enumerate(clusters, start=1):
        if cluster.custom_id != i:
            cluster.custom_id = i
            cluster.save(update_fields=['custom_id'])



# The error you're encountering is related to a Duplicate entry issue with the custom_id field when attempting to delete a room. The root cause of the problem is that during the deletion process, the renumber_alert_custom_ids function is likely being triggered, which tries to update the custom_id field of alerts. However, this update is resulting in duplicate custom_id values in the database, which is causing the IntegrityError.


# @receiver(post_delete, sender=Alert)
# def renumber_alert_custom_ids(sender, instance, **kwargs):
#     alerts = Alert.objects.all().order_by('custom_id')
#     for i, alert in enumerate(alerts, start=1):
#         if alert.custom_id != i:
#             alert.custom_id = i
#             alert.save(update_fields=['custom_id'])

@receiver(post_delete, sender=MqttDevice)
def renumber_mqtt_device_custom_ids(sender, instance, **kwargs):
    mqtt_devices = MqttDevice.objects.all().order_by('custom_id')
    for i, mqtt_device in enumerate(mqtt_devices, start=1):
        if mqtt_device.custom_id != i:
            mqtt_device.custom_id = i
            mqtt_device.save(update_fields=['custom_id'])

@receiver(post_delete, sender=GsmModule)
def renumber_gsm_module_custom_ids(sender, instance, **kwargs):
    gsm_modules = GsmModule.objects.all().order_by('custom_id')
    for i, gsm_module in enumerate(gsm_modules, start=1):
        if gsm_module.custom_id != i:
            gsm_module.custom_id = i
            gsm_module.save(update_fields=['custom_id'])

@receiver(post_delete, sender=SensorData)
def renumber_sensor_data_custom_ids(sender, instance, **kwargs):
    sensor_data = SensorData.objects.all().order_by('custom_id')
    for i, sensor in enumerate(sensor_data, start=1):
        if sensor.custom_id != i:
            sensor.custom_id = i
            sensor.save(update_fields=['custom_id'])

@receiver(post_delete, sender=MainAdmin)
def renumber_main_admin_custom_ids(sender, instance, **kwargs):
    main_admins = MainAdmin.objects.all().order_by('custom_id')
    for i, main_admin in enumerate(main_admins, start=1):
        if main_admin.custom_id != i:
            main_admin.custom_id = i
            main_admin.save(update_fields=['custom_id'])

@receiver(post_delete, sender=SubAdmin)
def renumber_sub_admin_custom_ids(sender, instance, **kwargs):
    sub_admins = SubAdmin.objects.all().order_by('custom_id')
    for i, sub_admin in enumerate(sub_admins, start=1):
        if sub_admin.custom_id != i:
            sub_admin.custom_id = i
            sub_admin.save(update_fields=['custom_id'])

@receiver(post_delete, sender=PowerModule)
def renumber_power_module_custom_ids(sender, instance, **kwargs):
    power_modules = PowerModule.objects.all().order_by('custom_id')
    for i, power_module in enumerate(power_modules, start=1):
        if power_module.custom_id != i:
            power_module.custom_id = i
            power_module.save(update_fields=['custom_id'])









def admin_login(request):
    template_name = 'authentification/combined_login.html'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            main_admin = MainAdmin.objects.filter(user=user).first()
            if main_admin is not None:
                login(request, user)
                return redirect('main_admin_dashboard')
            
            sub_admin = SubAdmin.objects.filter(user=user).first()
            if sub_admin:
                if sub_admin.suspended:
                    context = {'msg': 'Your account is suspended. Please contact the administrator.'}
                    return render(request, template_name, context)
                elif sub_admin.approved:
                    login(request, user)
                    return redirect('sub_admin_dashboard')
                else:
                    context = {'msg': 'Your account is not approved yet. Please contact the administrator.'}
                    return render(request, template_name, context)
            
            context = {'msg': 'Your request is rejected by the admin.'}
            return render(request, template_name, context)
        else:
            context = {'msg': 'Invalid credentials.'}
            return render(request, template_name, context)
    
    return render(request, template_name)




@login_required
def delete_sub_admin(request, sub_admin_id):
    sub_admin = get_object_or_404(SubAdmin, id=sub_admin_id)
    sub_admin.user.delete()
    sub_admin.delete()
    return redirect('room')  # Redirect back to the room page or appropriate page

@login_required
def toggle_suspend_sub_admin(request, sub_admin_id):
    sub_admin = get_object_or_404(SubAdmin, id=sub_admin_id)
    sub_admin.suspended = not sub_admin.suspended
    sub_admin.save()
    return redirect('room')  # Redirect back to the room page or appropriate page







def room(request):
    add_room_form = AddRoomForm()
    add_cluster_form = AddClusterForm()
    clusters = Cluster.objects.all()
    mqtt_devices = MqttDevice.objects.all()
    gsm_modules = GsmModule.objects.all()
    filter_option = request.GET.get('filter', 'all')

    if filter_option == 'main_admin':
        rooms = Room.objects.filter(main_admins__user=request.user)
    elif filter_option == 'sub_admin':
        rooms = Room.objects.filter(sub_admins__user=request.user)
    else:
        rooms = Room.objects.all()

    buildings = Building.objects.all()

    approved_sub_admins = SubAdmin.objects.filter(approved=True)
    select_buildings_form = SelectBuildingsForm()
    sub_admin_requests = SubAdmin.objects.filter(approved=False)

    power_modules = PowerModule.objects.all()  # Add this line
    power_data = PowerData.objects.all()

    main_admins = MainAdmin.objects.all()
    sub_admins = SubAdmin.objects.all()


    context = {
        'main_admins' : main_admins,
        'sub_admins' : sub_admins,

        'add_room_form': add_room_form,
        'add_cluster_form': add_cluster_form,
        'rooms': rooms,
        'filter_option': filter_option,
        'mqtt_devices': mqtt_devices,
        'gsm_modules': gsm_modules,
        'buildings': buildings,
        'clusters': clusters,
        'approved_sub_admins': approved_sub_admins,
        'select_buildings_form': select_buildings_form,
        'sub_admin_requests': sub_admin_requests,
        'power_modules': power_modules,  # Pass power_modules to the template
        'power_data':power_data,
    }
    return render(request, 'Room/room-index.html', context)



@csrf_exempt
def select_mqtt_device(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        room_id = data.get('room_id')
        mqtt_device_id = data.get('mqtt_device_id')

        try:
            room = Room.objects.get(id=room_id)
            if mqtt_device_id:
                mqtt_device = MqttDevice.objects.get(id=mqtt_device_id)
                room.alert_mqtt_device.clear()  # Clear previous device selection
                room.alert_mqtt_device.add(mqtt_device)  # Add the new selection
            else:
                room.alert_mqtt_device.clear()  # Clear selection if no device is chosen
            room.save()

            return JsonResponse({'success': True})
        except (Room.DoesNotExist, MqttDevice.DoesNotExist):
            return JsonResponse({'success': False, 'error': 'Room or MQTT device not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})




def power_data_api(request):
    power_data = PowerData.objects.all().values('power_module_id', 'ct1', 'ct2', 'ct3', 'ct4')
    return JsonResponse(list(power_data), safe=False)



# def add_power_module(request):
#     if request.method == 'POST':
#         form = PowerModuleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('room')  # Redirect to the rooms page or another appropriate page
#     else:
#         form = PowerModuleForm()

#     buildings = Building.objects.all()  # Fetch all buildings

#     return render(request, 'Room/room-index.html', {'form': form, 'buildings': buildings})

def add_power_module(request):
    if request.method == 'POST':
        form = PowerModuleForm(request.POST)
        if form.is_valid():
            power_module = form.save(commit=False)
            power_module.save()
            # Update buildings
            power_module.buildings.set(form.cleaned_data['buildings'])
            power_module.save()
            return redirect('room')  # Redirect to the rooms page or another appropriate page
    else:
        form = PowerModuleForm()

    buildings = Building.objects.all()  # Fetch all buildings

    return render(request, 'Room/room-index.html', {'form': form, 'buildings': buildings})

# def view_power_module(request, pk):
#     """View details of a specific PowerModule."""
#     power_module = get_object_or_404(PowerModule, pk=pk)
#     data = {
#         'id': power_module.id,
#         'name': power_module.name,
#         'ip_address': power_module.ip_address,
#         'topic_name': power_module.topic_name,
#     }
#     return JsonResponse(data)

def view_power_module(request, pk):
    """View details of a specific PowerModule."""
    power_module = get_object_or_404(PowerModule, pk=pk)
    data = {
        'id': power_module.id,
        'name': power_module.name,
        'ip_address': power_module.ip_address,
        'topic_name': power_module.topic_name,
        'ct1correspondingname': power_module.ct1correspondingname,  # Add this line
        'ct2correspondingname': power_module.ct2correspondingname,  # Add this line
        'ct3correspondingname': power_module.ct3correspondingname,  # Add this line
        'ct4correspondingname': power_module.ct4correspondingname,  # Add this line
        'buildings': list(power_module.buildings.values_list('id', flat=True)),  # Include selected building IDs
    }
    return JsonResponse(data)


# @csrf_exempt
# def edit_power_module(request):
#     """Edit a PowerModule."""
#     if request.method == 'POST':
#         pk = request.POST.get('id')
#         power_module = get_object_or_404(PowerModule, pk=pk)
#         form = PowerModuleForm(request.POST, instance=power_module)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors})

@csrf_exempt
def edit_power_module(request):
    """Edit a PowerModule."""
    if request.method == 'POST':
        pk = request.POST.get('id')
        power_module = get_object_or_404(PowerModule, pk=pk)
        form = PowerModuleForm(request.POST, instance=power_module)
        if form.is_valid():
            power_module = form.save(commit=False)
            power_module.buildings.set(form.cleaned_data['buildings'])  # Update buildings
            power_module.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})



@csrf_exempt
def delete_power_module(request):
    """Delete a PowerModule."""
    if request.method == 'POST':
        pk = request.POST.get('id')
        power_module = get_object_or_404(PowerModule, pk=pk)
        power_module.delete()
        return JsonResponse({'success': True})








#####################################################

@csrf_exempt
@login_required
def assign_buildings(request):
    if request.method == 'POST':
        sub_admin_id = request.POST.get('sub_admin_id')
        building_ids = request.POST.getlist('buildings[]')

        sub_admin = get_object_or_404(SubAdmin, id=sub_admin_id)
        buildings = Building.objects.filter(id__in=building_ids)

        if buildings.exists():
            sub_admin.building.set(buildings)  # Replace existing related buildings
            sub_admin.save()

            # Prepare the response with updated building data
            updated_buildings = [{'id': b.id, 'name': b.name} for b in buildings]
            return JsonResponse({'success': True, 'sub_admin_id': sub_admin_id, 'buildings': updated_buildings})
        else:
            return JsonResponse({'success': False, 'error': 'No buildings found with provided IDs'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})




@csrf_exempt
@login_required
def add_room(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            room = Room.objects.create(
                name=form.cleaned_data['name'],
                ip_address=form.cleaned_data['ip_address'],
                topic_name=form.cleaned_data['topic_name']
            )
            main_admin = MainAdmin.objects.get(user=request.user)
            room.main_admins.add(main_admin)
            return JsonResponse({
                'success': True,
                'room': {
                    'id': room.id,
                    'name': room.name,
                    'ip_address': room.ip_address,
                    'topic_name': room.topic_name,
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@csrf_exempt
@login_required
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.name = request.POST.get('name')
        room.ip_address = request.POST.get('ip_address')
        room.topic_name = request.POST.get('topic_name')
        room.save()
        return JsonResponse({'success': True, 'room': {
            'id': room.id,
            'name': room.name,
            'ip_address': room.ip_address,
            'topic_name': room.topic_name,
        }})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
@login_required
def delete_rooom(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
@login_required
def delete_rooom(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        print(f"Deleting room: {room.id}")  # Debug log
        room.delete()
        return JsonResponse({'success': True})
    print("Invalid request method")  # Debug log
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

#############################################################################

@csrf_exempt
def edit_threshold(request):
    if request.method == 'POST':
        form = EditThresholdForm(request.POST)
        if form.is_valid():
            room_id = form.cleaned_data['room_id']
            threshold_type = form.cleaned_data['threshold_type']
            threshold_value = form.cleaned_data['threshold_value']
            try:
                room = Room.objects.get(id=room_id)
                setattr(room, threshold_type + '_threshold', threshold_value)
                room.save()
                return JsonResponse({'success': True})
            except Room.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Room not found'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})






@csrf_exempt
def toggle_sensor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        room_id = data.get('room_id')
        sensor_type = data.get('type')
        sensor_state = data.get('value')
        try:
            room = Room.objects.get(id=room_id)
            setattr(room, sensor_type, sensor_state)
            room.save()
            return JsonResponse({'success': True})
        except Room.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Room not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def update_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        room_id = data.get('room_id')
        alert_type = data.get('type')
        alert_value = data.get('value')
        try:
            room = Room.objects.get(id=room_id)
            if alert_type == 'temperature':
                room.temperature_alerts = alert_value
            elif alert_type == 'humidity':
                room.humidity_alerts = alert_value
            elif alert_type == 'pir_state':
                room.pir_alerts = alert_value
            elif alert_type == 'door_state':
                room.door_alerts = alert_value
            elif alert_type == 'flood_state':
                room.flood_alerts = alert_value
            elif alert_type == 'gas_state':
                room.gas_alerts = alert_value
            room.save()
            return JsonResponse({'success': True})
        except Room.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Room not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



####################################################################


###########################


@login_required
def add_building(request):
    if request.method == 'POST':
        form = AddBuildingForm(request.POST)
        if form.is_valid():
            building = form.save()
            return JsonResponse({
                'success': True,
                'building': {
                    'id': building.id,
                    'name': building.name,
                    'rooms': [room.name for room in building.rooms.all()],
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})





@login_required
def edit_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        form = EditBuildingForm(request.POST, instance=building)
        if form.is_valid():
            building = form.save()
            return JsonResponse({
                'success': True,
                'building': {
                    'id': building.id,
                    'name': building.name,
                    'rooms': [room.name for room in building.rooms.all()],
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def delete_building(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def building_config(request):
    buildings = Building.objects.all()
    rooms = Room.objects.all()
    context = {
        'buildings': buildings,
        'rooms': rooms,
    }
    return render(request, 'Room/room-index.html', context)




##########################################################################33



# @csrf_exempt
# @login_required
# def add_cluster(request):
#     if request.method == 'POST':
#         form = AddClusterForm(request.POST)
#         if form.is_valid():
#             cluster = form.save()
#             return JsonResponse({'success': True, 'cluster': {
#                 'id': cluster.id,
#                 'name': cluster.name,
#                 'description': cluster.description,
#             }})
#         return JsonResponse({'success': False, 'errors': form.errors})
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})



# @csrf_exempt
# @login_required
# def edit_cluster(request, cluster_id):
#     cluster = get_object_or_404(Cluster, id=cluster_id)
#     if request.method == 'POST':
#         form = EditClusterForm(request.POST, instance=cluster)
#         if form.is_valid():
#             cluster = form.save()
#             return JsonResponse({'success': True, 'cluster': {
#                 'id': cluster.id,
#                 'name': cluster.name,
#                 'description': cluster.description,
#             }})
#         return JsonResponse({'success': False, 'errors': form.errors})
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
@login_required
def add_cluster(request):
    if request.method == 'POST':
        form = AddClusterForm(request.POST)
        if form.is_valid():
            cluster = form.save()
            return JsonResponse({
                'success': True, 
                'cluster': {
                    'id': cluster.id,
                    'name': cluster.name,
                    'description': cluster.description,
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@csrf_exempt
@login_required
def edit_cluster(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)
    if request.method == 'POST':
        form = EditClusterForm(request.POST, instance=cluster)
        if form.is_valid():
            cluster = form.save()
            return JsonResponse({
                'success': True, 
                'cluster': {
                    'id': cluster.id,
                    'name': cluster.name,
                    'description': cluster.description,
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})





@csrf_exempt
@login_required
def delete_cluster(request, cluster_id):
    cluster = get_object_or_404(Cluster, id=cluster_id)
    if request.method == 'POST':
        cluster.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

############################################################


def device(request):
    mqtt_devices = MqttDevice.objects.all()
    gsm_modules = GsmModule.objects.all()
    context = {
        'mqtt_devices': mqtt_devices,
        'gsm_modules': gsm_modules,
    }
    return render(request, 'Room/room-index.html', context)



@csrf_exempt
def add_mqtt_device(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        MqttDevice.objects.create(
            name=data['device_name'],
            ip_address=data['ip_address'],
            topic_name=data['topic_name']
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})




@csrf_exempt
def edit_mqtt_device(request, device_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        device = get_object_or_404(MqttDevice, id=device_id)
        device.name = data['device_name']
        device.ip_address = data['ip_address']
        device.topic_name = data['topic_name']
        device.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})




@csrf_exempt
def delete_mqtt_device(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        device = get_object_or_404(MqttDevice, id=data['device_id'])
        device.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



def get_mqtt_device(request, device_id):
    device = get_object_or_404(MqttDevice, id=device_id)
    data = {
        'id': device.id,
        'name': device.name,
        'ip_address': device.ip_address,
        'topic_name': device.topic_name
    }
    return JsonResponse(data)





#####################################################################################################################




@csrf_exempt
def add_gsm_module(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        numbers_list = json.loads(data['numbers'])  # Load the JSON list of numbers
        
        GsmModule.objects.create(
            module_name=data['module_name'],
            ip_address=data['ip_address'],
            topic_name=data['topic_name'],
            numbers=numbers_list  # Save as a list
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def edit_gsm_module(request, module_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        module = get_object_or_404(GsmModule, id=module_id)
        numbers_list = json.loads(data['numbers'])  # Load the JSON list of numbers
        
        module.module_name = data['module_name']
        module.ip_address = data['ip_address']
        module.topic_name = data['topic_name']
        module.numbers = numbers_list  # Save as a list
        module.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})





@csrf_exempt
def delete_gsm_module(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        module = get_object_or_404(GsmModule, id=data['module_id'])
        module.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_gsm_module(request, module_id):
    module = get_object_or_404(GsmModule, id=module_id)
    data = {
        'id': module.id,
        'module_name': module.module_name,
        'ip_address': module.ip_address,
        'topic_name': module.topic_name,
        'numbers': module.numbers
    }
    return JsonResponse(data)





##############################################################################################################################################################################################
###############################################################################################################################################################################################


def get_active_inactive_rooms(request):
    rooms = Room.objects.all()
    active_rooms = sum(room.is_active() for room in rooms)
    inactive_rooms = sum(room.is_inactive() for room in rooms)

    return JsonResponse({
        'active_numbers': active_rooms,
        'inactive_numbers': inactive_rooms,
    })













# @login_required
# def main_admin_dashboard(request):
#     template_name = 'dashboard/maindashboard.html'

#     # Fetch counts and averages
#     sub_admin_count = SubAdmin.objects.count()
#     building_count = Building.objects.count()
#     room_count = Room.objects.count()

#     cluster_count = Cluster.objects.count()  # Add cluster count

#     try:
#         main_admin = MainAdmin.objects.get(user=request.user)
#     except MainAdmin.DoesNotExist:
#         return HttpResponse("You are not authorized to access this page.")

#     # Fetch rooms associated with the main admin and all approved sub admins
#     rooms = Room.objects.filter(Q(main_admins=main_admin) | Q(sub_admins__approved=True)).distinct()
#     sub_admin_requests = SubAdmin.objects.filter(approved=False)

#     # Fetch buildings associated with the main admin
#     buildings = Building.objects.filter(rooms__in=rooms).distinct()

#     clusters = Cluster.objects.filter(rooms__in=rooms).distinct()  # Fetch the clusters
#     clusterss = Cluster.objects.filter(buildings__in=buildings).distinct()  # Fetch the clusters

    

#     context = {
#         'sub_admin_requests': sub_admin_requests,
#         'rooms': rooms,
#         'sub_admin_count': sub_admin_count,
#         'building_count': building_count,
#         'room_count': room_count,
#         'buildings': buildings,

#         'cluster_count': cluster_count,  # Include cluster count in context
#         'clusters': clusters,  # Pass clusters to the template
#         'clusterss' : clusterss,

#     }

#     return render(request, template_name, context)

@login_required
def main_admin_dashboard(request):
    template_name = 'dashboard/maindashboard.html'

    # Fetch counts and averages
    sub_admin_count = SubAdmin.objects.count()
    building_count = Building.objects.count()
    room_count = Room.objects.count()

    try:
        main_admin = MainAdmin.objects.get(user=request.user)
    except MainAdmin.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")

    # Fetch rooms associated with the main admin and all approved sub admins
    rooms = Room.objects.filter(Q(main_admins=main_admin) | Q(sub_admins__approved=True)).distinct()
    sub_admin_requests = SubAdmin.objects.filter(approved=False)

    # Fetch clusters associated with the main admin
    clusters = Cluster.objects.all()

    # Fetch buildings associated with the main admin
    buildings = Building.objects.filter(rooms__in=rooms).distinct()

    

    context = {
        'sub_admin_requests': sub_admin_requests,
        'rooms': rooms,
        'sub_admin_count': sub_admin_count,
        'building_count': building_count,
        'room_count': room_count,
        'clusters': clusters,  # Add clusters to the context
        'buildings': buildings,
    }

    return render(request, template_name, context)






# @login_required
# def get_power_data(request):
#     buildings = Building.objects.prefetch_related('power_modules').all()
    
#     power_data_list = []

#     for building in buildings:
#         for power_module in building.power_modules.all():
#             latest_power_data = PowerData.objects.filter(power_module=power_module).order_by('-timestamp').first()
#             if latest_power_data:
#                 power_data_list.append({
#                     'module_id': power_module.id,
#                     'module_name': power_module.name,
#                     'building_ids': [b.id for b in power_module.buildings.all()],  # Get all associated building IDs
#                     'ct1': latest_power_data.ct1,
#                     'ct2': latest_power_data.ct2,
#                     'ct3': latest_power_data.ct3,
#                     'ct4': latest_power_data.ct4,
    
#                 })

#     return JsonResponse({'power_data': power_data_list})

@login_required
def get_power_data(request):
    buildings = Building.objects.prefetch_related('power_modules').all()

    power_data_list = []

    for building in buildings:
        for power_module in building.power_modules.all():
            latest_power_data = PowerData.objects.filter(power_module=power_module).order_by('-timestamp').first()
            if latest_power_data:
                power_data_list.append({
                    'module_id': power_module.id,
                    'module_name': power_module.name,
                    'building_ids': [b.id for b in power_module.buildings.all()],  # Get all associated building IDs
                    'ct1': latest_power_data.ct1,
                    'ct2': latest_power_data.ct2,
                    'ct3': latest_power_data.ct3,
                    'ct4': latest_power_data.ct4,
                    'ct1_name': power_module.ct1correspondingname,
                    'ct2_name': power_module.ct2correspondingname,
                    'ct3_name': power_module.ct3correspondingname,
                    'ct4_name': power_module.ct4correspondingname,
                })

    return JsonResponse({'power_data': power_data_list})






from django.utils import timezone
from django.http import JsonResponse
from .models import Room, SensorData
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min

@login_required
def get_peaksensor_dataa(request):
    rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    # Get the current time and 24 hours ago
    now = timezone.now()
    past_24_hours = now - timezone.timedelta(hours=24)

    for room in rooms:
        # Filter sensor data for the last 24 hours for each room
        sensor_data_last_24h = room.sensor_data.filter(timestamp__gte=past_24_hours)

        if sensor_data_last_24h.exists():
            # Get peak and lowest values for temperature and humidity
            peak_temperature = sensor_data_last_24h.aggregate(Max('temperature'))['temperature__max']
            lowest_temperature = sensor_data_last_24h.aggregate(Min('temperature'))['temperature__min']
            peak_humidity = sensor_data_last_24h.aggregate(Max('humidity'))['humidity__max']
            lowest_humidity = sensor_data_last_24h.aggregate(Min('humidity'))['humidity__min']

            # Get timestamps of these peak/lowest values
            peak_temperature_time = sensor_data_last_24h.filter(temperature=peak_temperature).first().timestamp
            lowest_temperature_time = sensor_data_last_24h.filter(temperature=lowest_temperature).first().timestamp
            peak_humidity_time = sensor_data_last_24h.filter(humidity=peak_humidity).first().timestamp
            lowest_humidity_time = sensor_data_last_24h.filter(humidity=lowest_humidity).first().timestamp

            sensor_data_list.append({
                'room_id': room.id,
                'peak_temperature': peak_temperature,
                'peak_temperature_time': peak_temperature_time,
                'lowest_temperature': lowest_temperature,
                'lowest_temperature_time': lowest_temperature_time,
                'peak_humidity': peak_humidity,
                'peak_humidity_time': peak_humidity_time,
                'lowest_humidity': lowest_humidity,
                'lowest_humidity_time': lowest_humidity_time,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)


@login_required
def get_sensor_dataa(request):
    rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    for room in rooms:
        latest_data = room.sensor_data.order_by('-timestamp').first()
        if latest_data:
            sensor_data_list.append({
                'room_id': room.id,
                'temperature_exceeds': latest_data.temperature > room.temperature_threshold if latest_data.temperature is not None else False,
                'humidity_exceeds': latest_data.humidity > room.humidity_threshold if latest_data.humidity is not None else False,
                'flood_detected': latest_data.floodState,
                'gas_detected': latest_data.gasState,
                'motion_detected': latest_data.pirState,
                'door_opened': latest_data.doorState,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)




@login_required
def get_sensor_dataaa(request):
    rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    for room in rooms:
        latest_data = room.sensor_data.order_by('-timestamp').first()
        if latest_data:
            temperature_status = 'white'
            humidity_status = 'white'
            flood_status = 'white'
            gas_status = 'white'
            motion_status = 'white'
            door_status = 'white'

            

            if latest_data.temperature is not None and latest_data.temperature > room.temperature_threshold:
                temperature_status = 'red'
            elif latest_data.temperature is not None:
                temperature_status = 'green'

            if latest_data.humidity is not None and latest_data.humidity > room.humidity_threshold:
                humidity_status = 'red'
            elif latest_data.humidity is not None:
                humidity_status = 'green'

            if room.door_state_threshold == "enabled" and latest_data.doorState:
                door_status = 'red'
            elif room.door_state_threshold == "enabled":
                door_status = 'green'

            if room.flood_state_threshold == "enabled" and latest_data.floodState:
                flood_status = 'red'
            elif room.flood_state_threshold == "enabled":
                flood_status = 'green'

            if room.pir_state_threshold == "enabled" and latest_data.pirState:
                motion_status = 'red'
            elif room.pir_state_threshold == "enabled":
                motion_status = 'green'

            if room.gas_state_threshold == "enabled" and latest_data.gasState:
                gas_status = 'red'
            elif room.gas_state_threshold == "enabled":
                gas_status = 'green'



            sensor_data_list.append({
                'room_id': room.id,
                'temperature_status': temperature_status,
                'humidity_status': humidity_status,
                'flood_status': flood_status,
                'gas_status': gas_status,
                'motion_status': motion_status,
                'door_status': door_status,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)




























# @login_required
# def mark_all_alerts_as_viewed(request, building_id):
#     try:
#         building = Building.objects.get(id=building_id)
#         rooms = building.rooms.all()

#         # Mark all alerts in the building's rooms as viewed
#         Alert.objects.filter(room__in=rooms).update(viewed=True)

#         # Send "0" to all MQTT devices
#         mqtt_devices = MqttDevice.objects.all()
#         for device in mqtt_devices:
#             mqtt_client.publish(device.topic_name, "0")

#         return JsonResponse({'status': 'success'})
#     except Building.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Building not found'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


# @login_required
# def mark_all_alerts_as_viewed(request, building_id):
#     try:
#         building = Building.objects.get(id=building_id)
#         rooms = building.rooms.all()

#         # Mark all alerts in the building's rooms as viewed and save the user info
#         main_admin = MainAdmin.objects.get(user=request.user)
#         Alert.objects.filter(room__in=rooms).update(viewed=True, marked_by=main_admin.user.username, marked_by_type='MainAdmin')

#         # Send "0" to all MQTT devices
#         mqtt_devices = MqttDevice.objects.all()
#         for device in mqtt_devices:
#             mqtt_client.publish(device.topic_name, "0")

#         return JsonResponse({'status': 'success'})
#     except Building.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Building not found'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})

@login_required
def mark_all_alerts_as_viewed(request, building_id):
    try:
        building = Building.objects.get(id=building_id)
        rooms = building.rooms.all()

        # Fetch alerts that are not yet viewed
        alerts_to_update = Alert.objects.filter(room__in=rooms, viewed=False)

        # Update only those alerts that haven't been viewed yet
        alerts_to_update.update(
            viewed=True,
            viewed_by=request.user.username,  # Store the name of the user who marks the alert
            viewed_at=timezone.now()  # Store the current time
        )

        # Send "0" to all MQTT devices
        mqtt_devices = MqttDevice.objects.all()
        for device in mqtt_devices:
            mqtt_client.publish(device.topic_name, "0")

        return JsonResponse({'status': 'success'})
    except Building.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Building not found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})























def room_list(request):
    rooms = Room.objects.all().values('id', 'name')
    return JsonResponse(list(rooms), safe=False)


########################
########################


#### graph



##############################
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

def all_rooms_alerts(request):
    now = timezone.now()
    
    # Get the time filter from the request, defaulting to the last 24 hours
    time_filter = request.GET.get('time_filter', '24h')
    time_deltas = {
        '30min': timedelta(minutes=30),
        '1h': timedelta(hours=1),
        '2h': timedelta(hours=2),
        '5h': timedelta(hours=5),
        '8h': timedelta(hours=8),
        '12h': timedelta(hours=12),
        '24h': timedelta(hours=24),
        '2d': timedelta(days=2),
        '3d': timedelta(days=3),
        '5d': timedelta(days=5),
        '10d': timedelta(days=10),
        '15d': timedelta(days=15),
        '20d': timedelta(days=20),
        '30d': timedelta(days=30),
        '60d': timedelta(days=60),
        '90d': timedelta(days=90),
    }

    # Get the delta for the selected time filter
    delta = time_deltas.get(time_filter, time_deltas['24h'])
    time_threshold = now - delta

    rooms_data = []

    for room in Room.objects.all():
        # Filter sensor data for the specified time range for the specific room
        sensor_data_qs = SensorData.objects.filter(
            rooms=room,
            timestamp__gte=time_threshold
        )

        # Initialize alert counts
        temperature_exceeds = sensor_data_qs.filter(
            Q(temperature__gt=room.temperature_threshold)
        ).count()

        humidity_exceeds = sensor_data_qs.filter(
            Q(humidity__gt=room.humidity_threshold)
        ).count()

        door_exceeds = 0
        if room.door_state_threshold == "enabled":
            door_exceeds = sensor_data_qs.filter(
                ~Q(doorState=(room.door_state_threshold == 'closed'))
            ).count()

        flood_exceeds = 0
        if room.flood_state_threshold == "enabled":
            flood_exceeds = sensor_data_qs.filter(
                ~Q(floodState=(room.flood_state_threshold == 'no_flood'))
            ).count()

        pir_exceeds = 0
        if room.pir_state_threshold == "enabled":
            pir_exceeds = sensor_data_qs.filter(
                ~Q(pirState=(room.pir_state_threshold == 'no_motion'))
            ).count()

        gas_exceeds = 0
        if room.gas_state_threshold == "enabled":
            gas_exceeds = sensor_data_qs.filter(
                ~Q(gasState=(room.gas_state_threshold == 'no_gas'))
            ).count()

        rooms_data.append({
            'name': room.name,
            'temperature_alerts': temperature_exceeds,
            'humidity_alerts': humidity_exceeds,
            'door_alerts': door_exceeds,
            'flood_alerts': flood_exceeds,
            'pir_alerts': pir_exceeds,
            'gas_alerts': gas_exceeds,
        })

    return JsonResponse(rooms_data, safe=False)




from django.utils import timezone
from django.http import JsonResponse
from .models import Room, SensorData
from datetime import timedelta

# def fetch_room_data_tem(request):
#     # Get current time and 1 hour before
#     current_time = timezone.now()
#     one_hour_ago = current_time - timedelta(hours=1)
    
#     # Get all rooms and their sensor data in the last hour
#     room_data = []
#     rooms = Room.objects.all()
    
#     for room in rooms:
#         sensor_data = room.sensor_data.filter(timestamp__gte=one_hour_ago).order_by('timestamp')
#         room_temperature = [data.temperature for data in sensor_data]
#         room_humidity = [data.humidity for data in sensor_data]
#         timestamps = [data.timestamp.strftime('%H:%M') for data in sensor_data]
        

#         room_data.append({
#             'room_name': room.name,
#             'temperature': room_temperature,
#             'humidity': room_humidity,
#             'timestamps': timestamps
#         })

#     return JsonResponse({'room_data': room_data})



from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

def fetch_room_data_tem(request):
    # Get current time in the server's timezone
    current_time = timezone.now()
    # Calculate the time range (last one hour)
    one_hour_ago = current_time - timedelta(hours=1)
    
    # List to store the room data
    room_data = []
    
    # Fetch all rooms
    rooms = Room.objects.all()
    
    # Iterate through each room to fetch relevant sensor data
    for room in rooms:
        # Filter sensor data for the last one hour
        sensor_data = room.sensor_data.filter(timestamp__gte=one_hour_ago).order_by('timestamp')
        
        # Extract temperature, humidity, and timestamps from the sensor data
        room_temperature = [data.temperature for data in sensor_data]
        room_humidity = [data.humidity for data in sensor_data]
        
        # Localize timestamps to the user's timezone (assuming the server uses UTC)
        timestamps = [timezone.localtime(data.timestamp).strftime('%H:%M') for data in sensor_data]
        
        # Append the data to the room_data list
        room_data.append({
            'room_name': room.name,
            'temperature': room_temperature,
            'humidity': room_humidity,
            'timestamps': timestamps
        })
    
    # Return the data as a JSON response
    return JsonResponse({'room_data': room_data})



########################
########################



from django.db.models import Q

def room_details(request, room_id):
    try:
        # Get the room object
        room = Room.objects.get(id=room_id)
        
        # Get the current time
        now = timezone.now()
        
        # Calculate 24 hours ago
        twenty_four_hours_ago = now - timedelta(hours=24)
        
        # Filter sensor data for the last 24 hours for the specific room
        sensor_data_qs = SensorData.objects.filter(
            rooms=room,
            timestamp__gte=twenty_four_hours_ago
        )

        # Initialize alert counts
        temperature_exceeds = sensor_data_qs.filter(
            Q(temperature__gt=room.temperature_threshold)
        ).count()

        humidity_exceeds = sensor_data_qs.filter(
            Q(humidity__gt=room.humidity_threshold)
        ).count()

        door_exceeds = 0
        if room.door_state_threshold == "enabled":
            door_exceeds = sensor_data_qs.filter(
                ~Q(doorState=(room.door_state_threshold == 'closed'))
            ).count()

        flood_exceeds = 0
        if room.flood_state_threshold == "enabled":
            flood_exceeds = sensor_data_qs.filter(
                ~Q(floodState=(room.flood_state_threshold == 'no_flood'))
            ).count()

        pir_exceeds = 0
        if room.pir_state_threshold == "enabled":
            pir_exceeds = sensor_data_qs.filter(
                ~Q(pirState=(room.pir_state_threshold == 'no_motion'))
            ).count()

        gas_exceeds = 0
        if room.gas_state_threshold == "enabled":
            gas_exceeds = sensor_data_qs.filter(
                ~Q(gasState=(room.gas_state_threshold == 'no_gas'))
            ).count()

        # Prepare the response data
        alert_data = {
            'temperature_exceeds': temperature_exceeds,
            'humidity_exceeds': humidity_exceeds,
            'door_exceeds': door_exceeds,
            'flood_exceeds': flood_exceeds,
            'pir_exceeds': pir_exceeds,
            'gas_exceeds': gas_exceeds,
        }
        
        room_data = {
            'name': room.name,
            'ip_address': room.ip_address,
            'temperature_threshold': room.temperature_threshold,
            'humidity_threshold': room.humidity_threshold,
            'alerts': alert_data,
            'current_time': timezone.localtime(now).strftime('%Y-%m-%d %H:%M:%S %Z'),
        }
        
        return JsonResponse(room_data)
    
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)



@login_required
def alert_counts(request):
    total_alerts = Alert.objects.count()
    resolved_alerts = Alert.objects.filter(viewed=True).count()
    pending_alerts = Alert.objects.filter(viewed=False).count()
    active_alerts = total_alerts - resolved_alerts

    data = {
        'total': total_alerts,
        'active': active_alerts,
        'resolved': resolved_alerts,
        'pending': pending_alerts,
    }
    return JsonResponse(data)










@login_required
def get_details(request, detail_type, detail_id):
    if detail_type == 'users':
        users = list(SubAdmin.objects.filter(approved=True).values('username', 'suspended'))  # Include 'suspended'
        return JsonResponse(users, safe=False)
    elif detail_type == 'buildings':
        buildings = list(Building.objects.values('id', 'name'))
        return JsonResponse(buildings, safe=False)
    elif detail_type == 'rooms':
        rooms = list(Room.objects.filter(buildings__id=detail_id).values('name'))
        return JsonResponse(rooms, safe=False)
    else:
        return JsonResponse([], safe=False)

##############################################################################################################################################################################################
###############################################################################################################################################################################################













################################################################################################################
################################################################################################################
################################################################################################################



def alerts_page(request):
    rooms = Room.objects.all()

    room_count = Room.objects.count()

    
    # Fetch all alerts and filter based on query parameters
    alert_list = Alert.objects.order_by('-id')[:10000] 
    room_id = request.GET.get('room')
    sensor = request.GET.get('sensor')
    date_range = request.GET.get('date_range')



    # Paginate the alerts
    paginator = Paginator(alert_list, 10)
    page = request.GET.get('page')

    try:
        alerts = paginator.page(page)
    except PageNotAnInteger:
        alerts = paginator.page(1)
    except EmptyPage:
        alerts = paginator.page(paginator.num_pages)

    # Separate queries for viewed and unviewed alerts
    viewed_alerts = Alert.objects.filter(viewed=True).order_by('-id')[:100] 
    unviewed_alerts = Alert.objects.filter(viewed=False).order_by('-id')[:100] 
    sub_admin_requests = SubAdmin.objects.filter(approved=False)


    context = {
        'alerts': alerts,
        'rooms': rooms,
        'room_count': room_count,
        'viewed_alerts': viewed_alerts,
        'unviewed_alerts': unviewed_alerts,
        'sub_admin_requests': sub_admin_requests,
    }
    return render(request, 'alerts/alerts-index.html', context)



def get_alerts(request):
    alerts = Alert.objects.order_by('-id')[:10]  
    alert_list = []
    for alert in alerts:
        building_names = ', '.join(building.name for building in alert.room.buildings.all())
        sub_admin_names = ', '.join(
            ', '.join(sub_admin.username for sub_admin in building.sub_admins.all())
            for building in alert.room.buildings.all()
        )
        alert_list.append({
            'id': alert.id,
            'message': alert.message,
            'alert_type': alert.type,
            'room_name': alert.room.name,
            'building_names': building_names,
            'sub_admin_names': sub_admin_names,
            'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            'viewed': alert.viewed,
            'viewed_by': alert.viewed_by if alert.viewed_by else "No one viewed",
            'viewed_at': localtime(alert.viewed_at).strftime('%Y-%m-%d %H:%M:%S') if alert.viewed_at else None,
        })
    return JsonResponse({'alerts': alert_list})




@login_required
def update_alerts(request):
    if request.method == 'POST':
        alert_ids = request.POST.getlist('alert_ids')
        if alert_ids:
            # Update each alert with the viewed status, current user, and current time
            Alert.objects.filter(id__in=alert_ids).update(
                viewed=True,
                viewed_by=request.user.username,
                viewed_at=timezone.now()  # Set the current time
            )
    return redirect('alerts_page')



def get_alert_details(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    building_names = ', '.join(building.name for building in alert.room.buildings.all())
    sub_admin_names = ', '.join(
        ', '.join(sub_admin.username for sub_admin in building.sub_admins.all())
        for building in alert.room.buildings.all()
    )
    return JsonResponse({
        'message': alert.message,
        'room_name': alert.room.name,
        'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        'sub_admin_names': sub_admin_names,
    })



@csrf_exempt
def reset_alert(request):
    if request.method == 'POST':
        try:
            mqtt_devices = MqttDevice.objects.all()
            for device in mqtt_devices:
                mqtt_client.publish(device.topic_name, "0")
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"})



def download_data(request):
    room_id = request.GET.get('room_id')
    start_datetime_str = request.GET.get('start_datetime')
    end_datetime_str = request.GET.get('end_datetime')

    # Validate date-time inputs
    try:
        start_datetime = parse_datetime(start_datetime_str)
        end_datetime = parse_datetime(end_datetime_str)
        if start_datetime is None or end_datetime is None:
            raise ValueError("Invalid date-time format.")
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

    if start_datetime >= end_datetime:
        return JsonResponse({'error': "Start date-time must be before end date-time."}, status=400)

    # Convert to timezone-aware datetimes
    start_datetime = timezone.make_aware(start_datetime)
    end_datetime = timezone.make_aware(end_datetime)

    room = get_object_or_404(Room, id=room_id)

    alerts = Alert.objects.filter(
        room=room,
        timestamp__range=[start_datetime, end_datetime]
    )

    if not alerts.exists():
        return JsonResponse({'error': "No data found for the specified criteria."}, status=404)

    data = []
    for alert in alerts:
        timestamp_naive = alert.timestamp.astimezone(None) if alert.timestamp else None
        timestamp_str = timestamp_naive.strftime('%Y-%m-%d %H:%M:%S') if timestamp_naive else None
        data.append({
            'Type': alert.type,
            'Message': alert.message,
            'Timestamp': timestamp_str,
            'Viewed': alert.viewed,
        })

    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={room.name}_alerts_{start_datetime_str}_to_{end_datetime_str}.xlsx'

    df.to_excel(response, index=False)
    return response


################################################################################################################
################################################################################################################
################################################################################################################









def lives(request):
    # Fetch all rooms
    rooms = Room.objects.all()
    sub_admin_requests = SubAdmin.objects.filter(approved=False)

    # Prepare context for rendering
    template_name = 'lives/lives-index.html'
    context = {
        'rooms': rooms,
        'sub_admin_requests': sub_admin_requests,
    }
    return render(request, template_name, context)














def get_live_sensor_data(request):
    room_id = request.GET.get('room')
    date_range = request.GET.get('date_range')
    
    rooms = Room.objects.all()
    if room_id:
        rooms = rooms.filter(pk=room_id)

    sensor_data_list = []

    for room in rooms:
        sensor_data_qs = SensorData.objects.filter(rooms=room)
        
        if date_range:
            try:
                start_date_str, end_date_str = date_range.split(' to ')
                start_date = parse_datetime(start_date_str)
                end_date = parse_datetime(end_date_str)
                sensor_data_qs = sensor_data_qs.filter(timestamp__range=[start_date, end_date])
            except ValueError:
                pass

        latest_data = sensor_data_qs.order_by('-timestamp').first()
        if latest_data:
            # Fetch sub-admins related to each building
            building_subadmins = {}
            for building in room.buildings.all():
                sub_admins = building.sub_admins.all()
                building_subadmins[building.name] = [sub_admin.username for sub_admin in sub_admins]

            sensor_data_list.append({
                'room_name': room.name,
                'building_names': [building.name for building in room.buildings.all()],
                'building_subadmins': building_subadmins,
                'temperature': latest_data.temperature,
                'humidity': latest_data.humidity,
                'door_state': latest_data.doorState,
                'flood_state': latest_data.floodState,
                'pir_state': latest_data.pirState,
                'gas_state': latest_data.gasState,
                'timestamp': localtime(latest_data.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                'temperature_exceeds': latest_data.temperature > room.temperature_threshold if latest_data.temperature is not None else False,
                'humidity_exceeds': latest_data.humidity > room.humidity_threshold if latest_data.humidity is not None else False,
                'door_opened': latest_data.doorState > 0,
                'flood_detected': latest_data.floodState > 0,
                'motion_detected': latest_data.pirState > 0,
                'gas_detected': latest_data.gasState > 0,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)













##############################################################################################################################################################################################
###############################################################################################################################################################################################





@require_GET
def fetch_data(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    sort_by = request.GET.get('sort_by', 'room_name')  # Default sort by room name
    sort_order = request.GET.get('sort_order', 'asc')  # Default sort order ascending

    # Parse start_date and end_date to datetime objects
    start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d')

    # Fetch alerts for each room for the specified date range
    room_alerts_data = []
    for room in Room.objects.all():
        room_alerts = room.alerts.filter(timestamp__range=(start_date, end_date))
        alert_counts = room_alerts.values('type').annotate(count=Count('type'))
        room_alerts_data.append({
            'room_name': room.name,
            'alert_counts': list(alert_counts),  # Convert QuerySet to list for JSON serialization
        })

    # Sort room_alerts_data based on sort_by and sort_order
    room_alerts_data.sort(key=lambda x: x[sort_by], reverse=(sort_order == 'desc'))

    return JsonResponse(room_alerts_data, safe=False)




def custom_logout(request):
    logout(request)
    return redirect('admin_login')





@csrf_exempt
def delete_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        try:
            room = Room.objects.get(id=room_id)
            room.delete()
            return JsonResponse({'message': 'Room deleted successfully'})
        except Room.DoesNotExist:
            return JsonResponse({'error': 'Room not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@login_required
@require_POST
def approve_sub_admin(request, sub_admin_id):
    sub_admin = get_object_or_404(SubAdmin, id=sub_admin_id)
    sub_admin.approved = True
    sub_admin.save()
    return redirect('main_admin_dashboard')

@login_required
@require_POST
def reject_sub_admin(request, sub_admin_id):
    sub_admin = get_object_or_404(SubAdmin, id=sub_admin_id)
    sub_admin.delete()
    return redirect('main_admin_dashboard')






from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import SubAdmin, Room, Alert

@login_required
def sub_admin_dashboard(request):
    template_name = 'dashboard/subadmindashboard.html'
    
    # Get the SubAdmin object for the logged-in user
    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
    except SubAdmin.DoesNotExist:
        # Handle the case where the current user is not a SubAdmin
        return HttpResponse("You are not authorized to access this page.")
    
    # Fetch all rooms associated with the current sub-admin's buildings
    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()


    sub_admin_count = SubAdmin.objects.count()
    building_count = Building.objects.count()
    room_count = Room.objects.count()

    

    context = {

        'buildings': buildings,
        'rooms': rooms,
        'sub_admin_count': sub_admin_count,
        'building_count': building_count,
        'room_count': room_count,
    }

    return render(request, template_name, context)



##################

# @login_required
# def alert_countss(request):
#     try:
#         sub_admin = SubAdmin.objects.get(user=request.user)
#     except SubAdmin.DoesNotExist:
#         # Handle the case where the current user is not a SubAdmin
#         return HttpResponse("You are not authorized to access this page.")
#     buildings = sub_admin.building.all()
#     rooms = Room.objects.filter(buildings__in=buildings).distinct()
#     # total_alerts = Alert.objects.count()
#     # resolved_alerts = Alert.objects.filter(viewed=True).count()
#     # pending_alerts = Alert.objects.filter(viewed=False).count()
#     # active_alerts = total_alerts - resolved_alerts
#     total_alerts_count = Alert.objects.filter(room__in=rooms).count()
#     active_alerts_count = Alert.objects.filter(room__in=rooms, viewed=False).count()
#     resolved_alerts_count = Alert.objects.filter(room__in=rooms, viewed=True).count()
#     pending_alerts_count = Alert.objects.filter(room__in=rooms, viewed=False).count()

#     data = {
#         'total': total_alerts_count,
#         'active': active_alerts_count,
#         'resolved': resolved_alerts_count,
#         'pending': pending_alerts_count,
#     }
#     return JsonResponse(data)


@login_required
def alert_countss(request):
    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
    except SubAdmin.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")

    # Get buildings and rooms related to the current sub-admin
    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()

    # Get alert counts specific to the sub-admin's rooms
    total_alerts_count = Alert.objects.filter(room__in=rooms).count()
    active_alerts_count = Alert.objects.filter(room__in=rooms, viewed=False).count()
    resolved_alerts_count = Alert.objects.filter(room__in=rooms, viewed=True).count()
    pending_alerts_count = Alert.objects.filter(room__in=rooms, viewed=False).count()

    data = {
        'total': total_alerts_count,
        'active': active_alerts_count,
        'resolved': resolved_alerts_count,
        'pending': pending_alerts_count,
    }

    return JsonResponse(data)


####################


@login_required
def get_sensor_dataaaa(request):

    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
    except SubAdmin.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")

    # Get buildings and rooms related to the current sub-admin
    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()

    
    # rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    for room in rooms:
        latest_data = room.sensor_data.order_by('-timestamp').first()
        if latest_data:
            sensor_data_list.append({
                'room_id': room.id,
                'temperature_exceeds': latest_data.temperature > room.temperature_threshold if latest_data.temperature is not None else False,
                'humidity_exceeds': latest_data.humidity > room.humidity_threshold if latest_data.humidity is not None else False,
                'flood_detected': latest_data.floodState,
                'gas_detected': latest_data.gasState,
                'motion_detected': latest_data.pirState,
                'door_opened': latest_data.doorState,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)




@login_required
def get_sensor_dataaaaa(request):


    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
    except SubAdmin.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")

    # Get buildings and rooms related to the current sub-admin
    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()


    # rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    for room in rooms:
        latest_data = room.sensor_data.order_by('-timestamp').first()
        if latest_data:
            temperature_status = 'white'
            humidity_status = 'white'
            flood_status = 'white'
            gas_status = 'white'
            motion_status = 'white'
            door_status = 'white'

            if latest_data.temperature is not None and latest_data.temperature > room.temperature_threshold:
                temperature_status = 'red'
            elif latest_data.temperature is not None:
                temperature_status = 'green'

            if latest_data.humidity is not None and latest_data.humidity > room.humidity_threshold:
                humidity_status = 'red'
            elif latest_data.humidity is not None:
                humidity_status = 'green'

            if room.door_state_threshold == "enabled" and latest_data.doorState:
                door_status = 'red'
            elif room.door_state_threshold == "enabled":
                door_status = 'green'

            if room.flood_state_threshold == "enabled" and latest_data.floodState:
                flood_status = 'red'
            elif room.flood_state_threshold == "enabled":
                flood_status = 'green'

            if room.pir_state_threshold == "enabled" and latest_data.pirState:
                motion_status = 'red'
            elif room.pir_state_threshold == "enabled":
                motion_status = 'green'

            if room.gas_state_threshold == "enabled" and latest_data.gasState:
                gas_status = 'red'
            elif room.gas_state_threshold == "enabled":
                gas_status = 'green'

            sensor_data_list.append({
                'room_id': room.id,
                'temperature_status': temperature_status,
                'humidity_status': humidity_status,
                'flood_status': flood_status,
                'gas_status': gas_status,
                'motion_status': motion_status,
                'door_status': door_status,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)




@login_required
def get_power_dataaa(request):
    buildings = Building.objects.prefetch_related('power_modules').all()

    power_data_list = []

    for building in buildings:
        for power_module in building.power_modules.all():
            latest_power_data = PowerData.objects.filter(power_module=power_module).order_by('-timestamp').first()
            if latest_power_data:
                power_data_list.append({
                    'module_id': power_module.id,
                    'module_name': power_module.name,
                    'building_ids': [b.id for b in power_module.buildings.all()],  # Get all associated building IDs
                    'ct1': latest_power_data.ct1,
                    'ct2': latest_power_data.ct2,
                    'ct3': latest_power_data.ct3,
                    'ct4': latest_power_data.ct4,
                    'ct1_name': power_module.ct1correspondingname,
                    'ct2_name': power_module.ct2correspondingname,
                    'ct3_name': power_module.ct3correspondingname,
                    'ct4_name': power_module.ct4correspondingname,
                })

    return JsonResponse({'power_data': power_data_list})






from django.utils import timezone
from django.http import JsonResponse
from .models import Room, SensorData
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min

@login_required
def get_peaksensor_dataaa(request):
    rooms = Room.objects.all()  # Adjust this as needed to filter relevant rooms
    sensor_data_list = []

    # Get the current time and 24 hours ago
    now = timezone.now()
    past_24_hours = now - timezone.timedelta(hours=24)

    for room in rooms:
        # Filter sensor data for the last 24 hours for each room
        sensor_data_last_24h = room.sensor_data.filter(timestamp__gte=past_24_hours)

        if sensor_data_last_24h.exists():
            # Get peak and lowest values for temperature and humidity
            peak_temperature = sensor_data_last_24h.aggregate(Max('temperature'))['temperature__max']
            lowest_temperature = sensor_data_last_24h.aggregate(Min('temperature'))['temperature__min']
            peak_humidity = sensor_data_last_24h.aggregate(Max('humidity'))['humidity__max']
            lowest_humidity = sensor_data_last_24h.aggregate(Min('humidity'))['humidity__min']

            # Get timestamps of these peak/lowest values
            peak_temperature_time = sensor_data_last_24h.filter(temperature=peak_temperature).first().timestamp
            lowest_temperature_time = sensor_data_last_24h.filter(temperature=lowest_temperature).first().timestamp
            peak_humidity_time = sensor_data_last_24h.filter(humidity=peak_humidity).first().timestamp
            lowest_humidity_time = sensor_data_last_24h.filter(humidity=lowest_humidity).first().timestamp

            sensor_data_list.append({
                'room_id': room.id,
                'peak_temperature': peak_temperature,
                'peak_temperature_time': peak_temperature_time,
                'lowest_temperature': lowest_temperature,
                'lowest_temperature_time': lowest_temperature_time,
                'peak_humidity': peak_humidity,
                'peak_humidity_time': peak_humidity_time,
                'lowest_humidity': lowest_humidity,
                'lowest_humidity_time': lowest_humidity_time,
            })

    response_data = {
        'sensor_data': sensor_data_list
    }

    return JsonResponse(response_data)



# @login_required
# def mark_all_alerts_as_viewedsub(request, building_id):
#     try:
#         building = Building.objects.get(id=building_id)
#         rooms = building.rooms.all()

#         # Mark all alerts in the building's rooms as viewed
#         Alert.objects.filter(room__in=rooms).update(viewed=True)

#         # Send "0" to all MQTT devices
#         mqtt_devices = MqttDevice.objects.all()
#         for device in mqtt_devices:
#             mqtt_client.publish(device.topic_name, "0")

#         return JsonResponse({'status': 'success'})
#     except Building.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Building not found'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


# @login_required
# def mark_all_alerts_as_viewedsub(request, building_id):
#     try:
#         building = Building.objects.get(id=building_id)
#         rooms = building.rooms.all()

#         # Mark all alerts in the building's rooms as viewed and save the user info
#         sub_admin = SubAdmin.objects.get(user=request.user)
#         Alert.objects.filter(room__in=rooms).update(viewed=True, marked_by=sub_admin.user.username, marked_by_type='SubAdmin')

#         # Send "0" to all MQTT devices
#         mqtt_devices = MqttDevice.objects.all()
#         for device in mqtt_devices:
#             mqtt_client.publish(device.topic_name, "0")

#         return JsonResponse({'status': 'success'})
#     except Building.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Building not found'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


@login_required
def mark_all_alerts_as_viewedsub(request, building_id):
    try:
        building = Building.objects.get(id=building_id)
        rooms = building.rooms.all()

        # Fetch alerts that are not yet viewed
        alerts_to_update = Alert.objects.filter(room__in=rooms, viewed=False)

        # Update only those alerts that haven't been viewed yet
        alerts_to_update.update(
            viewed=True,
            viewed_by=request.user.username,  # Store the name of the sub-admin who marks the alert
            viewed_at=timezone.now()  # Store the current time
        )

        # Send "0" to all MQTT devices
        mqtt_devices = MqttDevice.objects.all()
        for device in mqtt_devices:
            mqtt_client.publish(device.topic_name, "0")

        return JsonResponse({'status': 'success'})
    except Building.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Building not found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})







# # for the graph in sub admin or user profile 


from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import SubAdmin, Room, SensorData

@login_required
def all_rooms_alertssub(request):
    now = timezone.now()
    
    # Get the time filter from the request, defaulting to the last 24 hours
    time_filter = request.GET.get('time_filter', '24h')
    time_deltas = {
        '30min': timedelta(minutes=30),
        '1h': timedelta(hours=1),
        '2h': timedelta(hours=2),
        '5h': timedelta(hours=5),
        '8h': timedelta(hours=8),
        '12h': timedelta(hours=12),
        '24h': timedelta(hours=24),
        '2d': timedelta(days=2),
        '3d': timedelta(days=3),
        '5d': timedelta(days=5),
        '10d': timedelta(days=10),
        '15d': timedelta(days=15),
        '20d': timedelta(days=20),
        '30d': timedelta(days=30),
        '60d': timedelta(days=60),
        '90d': timedelta(days=90),
    }
    
    delta = time_deltas.get(time_filter, time_deltas['24h'])
    time_threshold = now - delta

    # Get the logged-in sub-admin's associated rooms
    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
    except SubAdmin.DoesNotExist:
        return JsonResponse({"error": "You are not authorized to access this data."}, status=403)

    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()

    rooms_data = []

    for room in rooms:
        sensor_data_qs = SensorData.objects.filter(
            rooms=room,
            timestamp__gte=time_threshold
        )

        # Initialize alert counts for each room
        temperature_exceeds = sensor_data_qs.filter(
            Q(temperature__gt=room.temperature_threshold)
        ).count()

        humidity_exceeds = sensor_data_qs.filter(
            Q(humidity__gt=room.humidity_threshold)
        ).count()

        door_exceeds = 0
        if room.door_state_threshold == "enabled":
            door_exceeds = sensor_data_qs.filter(
                ~Q(doorState=(room.door_state_threshold == 'closed'))
            ).count()

        flood_exceeds = 0
        if room.flood_state_threshold == "enabled":
            flood_exceeds = sensor_data_qs.filter(
                ~Q(floodState=(room.flood_state_threshold == 'no_flood'))
            ).count()

        pir_exceeds = 0
        if room.pir_state_threshold == "enabled":
            pir_exceeds = sensor_data_qs.filter(
                ~Q(pirState=(room.pir_state_threshold == 'no_motion'))
            ).count()

        gas_exceeds = 0
        if room.gas_state_threshold == "enabled":
            gas_exceeds = sensor_data_qs.filter(
                ~Q(gasState=(room.gas_state_threshold == 'no_gas'))
            ).count()

        rooms_data.append({
            'name': room.name,
            'temperature_alerts': temperature_exceeds,
            'humidity_alerts': humidity_exceeds,
            'door_alerts': door_exceeds,
            'flood_alerts': flood_exceeds,
            'pir_alerts': pir_exceeds,
            'gas_alerts': gas_exceeds,
        })

    return JsonResponse(rooms_data, safe=False)














################################################################################################################
################################################################################################################
################################################################################################################








# def alerts_pagesub(request):
#     template_name = 'alerts/alerts-indexsub.html'
    
#     try:
#         sub_admin = SubAdmin.objects.get(user=request.user)
#         buildings = sub_admin.building.all()
#         rooms = Room.objects.filter(buildings__in=buildings).distinct()
#         alerts_list = Alert.objects.filter(room__in=rooms).order_by('-id')
        
#         # Create a paginator with 10 items per page
#         paginator = Paginator(alerts_list, 10)
#         page_number = request.GET.get('page', 1)
        
#         try:
#             alerts = paginator.page(page_number)
#         except PageNotAnInteger:
#             alerts = paginator.page(1)
#         except EmptyPage:
#             alerts = paginator.page(paginator.num_pages)
        
#     except SubAdmin.DoesNotExist:
#         return render(request, template_name, {'error_message': "You are not authorized to access this page."})
    
#     context = {
#         'alerts': alerts,
#         'rooms': rooms,
#         'request': request,  # Pass the request to the template to handle pagination links
#     }
    
#     return render(request, template_name, context)


# def get_alerts_data(request):
#     try:
#         sub_admin = SubAdmin.objects.get(user=request.user)
#         buildings = sub_admin.building.all()
#         rooms = Room.objects.filter(buildings__in=buildings).distinct()
#         alerts_list = Alert.objects.filter(room__in=rooms).order_by('-id')
        
#         # Create a paginator with 10 items per page
#         paginator = Paginator(alerts_list, 10)
#         page_number = request.GET.get('page', 1)
        
#         try:
#             alerts = paginator.page(page_number)
#         except PageNotAnInteger:
#             alerts = paginator.page(1)
#         except EmptyPage:
#             alerts = paginator.page(paginator.num_pages)

#         alert_list = [{
#             'message': alert.message,
#             'alert_type': alert.type,
#             'room_name': alert.room.name,
#             'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
#             'viewed': alert.viewed,
#         } for alert in alerts]

#         return JsonResponse({'alerts': alert_list})

#     except SubAdmin.DoesNotExist:
#         return JsonResponse({'alerts': []})








# @csrf_exempt
# def update_alert_view_status(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         alert_id = data.get('alert_id')
#         viewed_status = data.get('viewed', False)

#         try:
#             alert = Alert.objects.get(id=alert_id)
#             alert.viewed = viewed_status
#             alert.save()
#             return JsonResponse({'success': True})
#         except Alert.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Alert not found.'})

#     return JsonResponse({'success': False, 'error': 'Invalid request method.'})





# def alerts_pagesub(request):
#     template_name = 'alerts/alerts-indexsub.html'
    
  
    
#     return render(request, template_name)

# def get_alertssub(request):
  
#     return JsonResponse()


# @login_required
# def update_alertssub(request):
   
#     return redirect()



# def get_alert_detailssub(request):

#     return JsonResponse()



# @csrf_exempt
# def reset_alertsub(request):
    
#     return JsonResponse()




@login_required
def alerts_pagesub(request):
    # Get the sub-admin's assigned buildings and rooms
    sub_admin = request.user.subadmin
    buildings = sub_admin.building.all()
    rooms = Room.objects.filter(buildings__in=buildings).distinct()

    # Fetch alerts only for rooms in the sub-admin's buildings
    alert_list = Alert.objects.filter(room__in=rooms).order_by('-id')[:10000]
    
    # Paginate the alerts
    paginator = Paginator(alert_list, 10)
    page = request.GET.get('page')

    try:
        alerts = paginator.page(page)
    except PageNotAnInteger:
        alerts = paginator.page(1)
    except EmptyPage:
        alerts = paginator.page(paginator.num_pages)

    # Separate viewed and unviewed alerts
    viewed_alerts = Alert.objects.filter(room__in=rooms, viewed=True).order_by('-id')[:100]
    unviewed_alerts = Alert.objects.filter(room__in=rooms, viewed=False).order_by('-id')[:100]

    context = {
        'alerts': alerts,
        'rooms': rooms,
        'viewed_alerts': viewed_alerts,
        'unviewed_alerts': unviewed_alerts,
    }
    return render(request, 'alerts/alerts-indexsub.html', context)


def get_alertssub(request):
    # Fetch only alerts related to the sub-admin's buildings
    sub_admin = request.user.subadmin
    rooms = Room.objects.filter(buildings__in=sub_admin.building.all()).distinct()
    alerts = Alert.objects.filter(room__in=rooms).order_by('-id')[:10]

    alert_list = []
    for alert in alerts:
        building_names = ', '.join(building.name for building in alert.room.buildings.all())
        alert_list.append({
            'id': alert.id,
            'message': alert.message,
            'alert_type': alert.type,
            'room_name': alert.room.name,
            'building_names': building_names,
            'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            'viewed': alert.viewed,
            'viewed_by': alert.viewed_by if alert.viewed_by else "No one viewed",
            'viewed_at': localtime(alert.viewed_at).strftime('%Y-%m-%d %H:%M:%S') if alert.viewed_at else None,
        })

    return JsonResponse({'alerts': alert_list})


@login_required
def update_alertssub(request):
    if request.method == 'POST':
        sub_admin = request.user.subadmin
        rooms = Room.objects.filter(buildings__in=sub_admin.building.all()).distinct()
        alert_ids = request.POST.getlist('alert_ids')

        # Ensure the alerts being updated are only in the sub-admin's buildings
        if alert_ids:
            Alert.objects.filter(id__in=alert_ids, room__in=rooms).update(
                viewed=True,
                viewed_by=request.user.username,
                viewed_at=timezone.now()  # Set the current time
            )
    return redirect('alerts_pagesub')


def get_alert_detailssub(request, alert_id):
    sub_admin = request.user.subadmin
    rooms = Room.objects.filter(buildings__in=sub_admin.building.all()).distinct()

    # Fetch the alert only if it's in one of the sub-admin's rooms
    alert = get_object_or_404(Alert, id=alert_id, room__in=rooms)
    building_names = ', '.join(building.name for building in alert.room.buildings.all())

    return JsonResponse({
        'message': alert.message,
        'room_name': alert.room.name,
        'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        'building_names': building_names,
    })


@csrf_exempt
def reset_alertsub(request):
    if request.method == 'POST':
        try:
            sub_admin = request.user.subadmin
            rooms = Room.objects.filter(buildings__in=sub_admin.building.all()).distinct()

            # Get MQTT devices related to rooms in the sub-admin's buildings
            mqtt_devices = MqttDevice.objects.filter(room__in=rooms).distinct()

            for device in mqtt_devices:
                mqtt_client.publish(device.topic_name, "0")

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"})






################################################################################################################
################################################################################################################
################################################################################################################






def livessub(request):
    template_name = 'lives/lives-indexsub.html'
    
    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
        buildings = sub_admin.building.all()
        rooms = Room.objects.filter(buildings__in=buildings).distinct()
    except SubAdmin.DoesNotExist:
        return render(request, template_name, {'error_message': "You are not authorized to access this page."})
    
    context = {
        'rooms': rooms,
    }
    
    return render(request, template_name, context)

def get_live_sensor_datasub(request):
    try:
        sub_admin = SubAdmin.objects.get(user=request.user)
        buildings = sub_admin.building.all()
        rooms = Room.objects.filter(buildings__in=buildings).distinct()
        sensor_data_list = []
        
        for room in rooms:
            latest_data = SensorData.objects.filter(rooms=room).order_by('-timestamp').first()
            if latest_data:
                sensor_data_list.append({
                    'room_name': room.name,
                    'temperature': latest_data.temperature,
                    'humidity': latest_data.humidity,
                    'door_state': latest_data.doorState,
                    'flood_state': latest_data.floodState,
                    'pir_state': latest_data.pirState,
                    'gas_state': latest_data.gasState,
                    'timestamp': localtime(latest_data.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                    'temperature_exceeds': latest_data.temperature > room.temperature_threshold if latest_data.temperature is not None else False,
                    'humidity_exceeds': latest_data.humidity > room.humidity_threshold if latest_data.humidity is not None else False,
                    'door_opened': latest_data.doorState,
                    'flood_detected': latest_data.floodState,
                    'motion_detected': latest_data.pirState,
                    'gas_detected': latest_data.gasState,
                })
    except SubAdmin.DoesNotExist:
        return JsonResponse({'sensor_data': []})
    
    return JsonResponse({'sensor_data': sensor_data_list})






def customm_logout(request):
    logout(request)
    return redirect('admin_login')







def rsub_admin_signup_view(request):
    template_name = 'authentification/signup_sub_admin.html'
    if request.method == 'POST':
        uname = request.POST['username']
        pasd = request.POST['password']
        cpasd = request.POST['cpassword']
        
        if pasd == cpasd:
            if User.objects.filter(username=uname).exists():
                context = {'msg': 'User already exists'}
            else:
                user = User.objects.create_user(username=uname, password=pasd)
                SubAdmin.objects.create(user=user, username=uname, approved=False)
                context = {'msg': 'Signup successful. Your request has been sent for approval. Please log in again after approval by the admin.'}
        else:
            context = {'msg': 'Passwords do not match'}
        return render(request, template_name, context)
    
    return render(request, template_name)




def get_sub_admin_rooms(request, sub_admin_id):
    try:
        sub_admin = SubAdmin.objects.get(id=sub_admin_id)
        rooms = sub_admin.rooms.all()
        room_names = [room.name for room in rooms]
        return JsonResponse({'rooms': room_names})
    except SubAdmin.DoesNotExist:
        return JsonResponse({'error': 'Sub admin not found'}, status=404)





def roomsub(request):


    return render(request, 'Room/room-indexsub.html')



##############################################################################################################################################################################################
###############################################################################################################################################################################################





#################

# new code for not get the application down by Start the MQTT client in a separate thread


# MQTT configuration

# MQTT_SERVER = "192.168.99.138"
# MQTT_SERVER = "192.168.0.111"

MQTT_SERVER = "192.168.29.184"
MQTT_PORT = 1883
MQTT_USERNAME = "iva"
MQTT_PASSWORD = "iva"

MQTT_KEEP_ALIVE = 60   ##################################



mqtt_client = None ####################################
######################################################################################################################################################################

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT broker yahooooooooooooo")
#         rooms = Room.objects.all()  # Get all rooms
#         for room in rooms:
#             client.subscribe(room.topic_name)  # Subscribe to each room's topic
#     else:
#         print("Failed to connect to MQTT broker. Error code:", rc)
#         # Here you can implement retry logic if needed



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to topics for Rooms and Power Modules
        rooms = Room.objects.all()
        for room in rooms:
            client.subscribe(room.topic_name)  # Subscribe to room topics

        power_modules = PowerModule.objects.all()
        for module in power_modules:
            client.subscribe(module.topic_name)  # Subscribe to power module topics
    else:
        print("Failed to connect to MQTT broker. Error code:", rc)


################################################################################################################################################################################################################################################################################################################################




######################################  bottom is continuesly send 5 in regular inteval from starting of app     #################################33



# Dictionary to store timers for each room
interval_timers = {}

def reset_timer(room):
    if room.id in interval_timers:
        interval_timers[room.id].cancel()
    
    # Fetch the latest interval from the database
    room.refresh_from_db()
    interval = room.interval  # Assuming `interval` is the field storing the interval in seconds

    # Set a new timer with the updated interval
    interval_timers[room.id] = Timer(interval, send_periodic_five, args=[room])
    interval_timers[room.id].start()

def send_periodic_five(room):
    mqtt_client.publish(room.topic_name, "5")
    reset_timer(room)

def start_timer_for_all_rooms():
    rooms = Room.objects.all()
    for room in rooms:
        reset_timer(room)

# Call this function to start the timers after the server starts or when intervals are updated
start_timer_for_all_rooms()





# def on_message(client, userdata, msg):
#     try:
#         topic = msg.topic
#         payload = msg.payload.decode()
#         print(f"Received message on topic {topic}: {payload}")



#         room = Room.objects.get(topic_name=topic)

#         building = room.buildings.first()  # Assuming a room belongs to at most one building   ###### this is for room
#         building_name = building.name if building else "Unknown Building"                          ###### this is for room

        

#         data = json.loads(payload)

#         sensor_data = SensorData.objects.create(
#             temperature=data.get('temperature'),
#             humidity=data.get('humidity'),
#             doorState=data.get('doorState'),
#             floodState=data.get('floodState'),
#             pirState=data.get('pirState'),
#             gasState=data.get('gasState')
#         )
#         room.sensor_data.add(sensor_data)
#         room.save()

#         alerts = check_thresholds_and_create_alert(room, sensor_data)

 

#         mqtt_devices = MqttDevice.objects.all()                                            ###### this is for room
#         for device in mqtt_devices:
#             for index, (alert_msg, alert_numbers) in enumerate(alerts, start=1):
#                 for alert in alert_numbers:
#                     alert_with_building_room = f"{building_name} {room.name}:{alert_msg}:{alert}\n\n"
#                     mqtt_client.publish(device.topic_name, alert_with_building_room)            

#         gsm_modules = GsmModule.objects.all()
#         if room.gsm_alert == 'enabled':
#             selected_numbers = room.gsm_numbers.split(',')
#             for alert_msg, alert_numbers in alerts:
#                 # Construct the alert message once per alert
#                 for module in gsm_modules:
#                     alert_messages = []
#                     for number in selected_numbers:
#                         alert_with_number = f"{number}:{room.name}:{alert_msg}\n"
#                         alert_messages.append(alert_with_number)
#                         # Optionally, you can break out of the loop here if you only want to send one message per alert
#                         break  # Remove this line if you want to send to all selected_numbers
#                     mqtt_client.publish(module.topic_name, ''.join(alert_messages))
#                     # Optionally, you can break out of the loop here if you only want to send one message per alert
#                     break  # Remove this line if you want to send to all gsm_modules


#         # Reset the timer since new data has been saved
#         reset_timer(room)

#     except Exception as e:
#         print("Error processing MQTT message:", str(e))





def on_message(client, userdata, msg):
    try:
        topic = msg.topic
        payload = msg.payload.decode()
        print(f"Received message on topic {topic}: {payload}")

        # Determine if the message is for Power Module or Room
        if 'CT1' in payload:  # Check if the message is for a Power Module
            data = json.loads(payload)
            power_module = PowerModule.objects.get(topic_name=topic)

            # Save the incoming data
            PowerData.objects.create(
                power_module=power_module,
                ct1=data.get('CT1'),
                ct2=data.get('CT2'),
                ct3=data.get('CT3'),
                ct4=data.get('CT4')
            )
        else:  # Handle Room data
            data = json.loads(payload)
            room = Room.objects.get(topic_name=topic)
            building = room.buildings.first()  # Assuming a room belongs to at most one building
            building_name = building.name if building else "Unknown Building"

            sensor_data = SensorData.objects.create(
                temperature=data.get('temperature'),
                humidity=data.get('humidity'),
                doorState=data.get('doorState'),
                floodState=data.get('floodState'),
                pirState=data.get('pirState'),
                gasState=data.get('gasState')
            )
            room.sensor_data.add(sensor_data)
            room.save()



            # alerts = check_thresholds_and_create_alert(room, sensor_data)

            # mqtt_devices = MqttDevice.objects.all()
            # for device in mqtt_devices:
            #     for index, (alert_msg, alert_numbers) in enumerate(alerts, start=1):
            #         for alert in alert_numbers:
            #             alert_with_building_room = f"{building_name} {room.name}:{alert_msg}:{alert}\n\n"
            #             mqtt_client.publish(device.topic_name, alert_with_building_room)
  
         ## changed for selecting alert device 
            room = Room.objects.get(topic_name=topic)
            alerts = check_thresholds_and_create_alert(room, sensor_data)

            for device in room.alert_mqtt_device.all():
                for index, (alert_msg, alert_numbers) in enumerate(alerts, start=1):
                    for alert in alert_numbers:
                        alert_with_building_room = f"{room.name}:{alert_msg}:{alert}\n\n"
                        mqtt_client.publish(device.topic_name, alert_with_building_room)

            # gsm_modules = GsmModule.objects.all()
            # if room.gsm_alert == 'enabled':
            #     selected_numbers = room.gsm_numbers
            #     for alert_msg, alert_numbers in alerts:
            #         alert_messages = []
            #         for number in selected_numbers:
            #             alert_with_number = f"{number}:{room.name}:{alert_msg}\n"
            #             alert_messages.append(alert_with_number)
            #         # Publish to each GSM module
            #         for module in gsm_modules:
            #             mqtt_client.publish(module.topic_name, ''.join(alert_messages))


            
            # gsm_modules = GsmModule.objects.all()
            # if room.gsm_alert == 'enabled':
            #     selected_numbers = room.gsm_numbers.split(',')
            #     for alert_msg, alert_numbers in alerts:
            #         # Construct the alert message once per alert
            #         for module in gsm_modules:
            #             alert_messages = []
            #             for number in selected_numbers:
            #                 alert_with_number = f"{number}:{room.name}:{alert_msg}\n"
            #                 alert_messages.append(alert_with_number)
            #                 # Optionally, you can break out of the loop here if you only want to send one message per alert
            #                 break  # Remove this line if you want to send to all selected_numbers
            #             mqtt_client.publish(module.topic_name, ''.join(alert_messages))
            #             # Optionally, you can break out of the loop here if you only want to send one message per alert
            #             break  # Remove this line if you want to send to all gsm_modules

            gsm_modules = GsmModule.objects.all()
            if room.gsm_alert == 'enabled':
                selected_numbers = room.gsm_numbers.split(',')  # Splitting the comma-separated numbers
                for alert_msg, alert_numbers in alerts:
                    # Construct the alert message once per alert
                    for module in gsm_modules:
                        alert_messages = []
                        # Join all selected numbers into a single comma-separated string
                        numbers_string = ','.join(selected_numbers)
                        # Create the alert message including all selected numbers
                        alert_with_numbers = f"{numbers_string}:{room.name}:{alert_msg}\n"
                        alert_messages.append(alert_with_numbers)

                        # Publish the message to the MQTT topic
                        mqtt_client.publish(module.topic_name, ''.join(alert_messages))
                        
                        # # Optionally, break out of the loop here if you only want to send one message per alert
                        # break  # Remove this line if you want to send to all gsm_modules


            # Reset the timer since new data has been saved
            reset_timer(room)

    except Exception as e:
        print("Error processing MQTT message:", str(e))









###################################################################################################################################################################
###################################################################################################################################################################




def check_thresholds_and_create_alert(room, sensor_data):
    alerts = []



    def publish_alert(alert_type, topic):
        alert_number = int(alert_type)
        # mqtt_client.publish(topic, str(alert_number))
        mqtt_client.publish(topic)    

    if sensor_data.temperature and sensor_data.temperature > room.temperature_threshold:
        alert_msg = f"Temp.{sensor_data.temperature}>{room.temperature_threshold}"
        alerts.append((alert_msg, room.temperature_alerts.split(',')))
        Alert.objects.create(room=room, type="Temperature Exceeded", message=alert_msg)
        for alert in room.temperature_alerts.split(','):
            publish_alert(alert, room.topic_name)

    if sensor_data.humidity and sensor_data.humidity > room.humidity_threshold:
        alert_msg = f"Hum.{sensor_data.humidity}>{room.humidity_threshold}"
        alerts.append((alert_msg, room.humidity_alerts.split(',')))
        Alert.objects.create(room=room, type="Humidity Exceeded", message=alert_msg)
        for alert in room.humidity_alerts.split(','):
            publish_alert(alert, room.topic_name)

    if room.door_state_threshold == "enabled" and sensor_data.doorState:
        alert_msg = "Door opened"
        alerts.append((alert_msg, room.door_alerts.split(',')))
        Alert.objects.create(room=room, type="Door Alert", message=alert_msg)
        for alert in room.door_alerts.split(','):
            publish_alert(alert, room.topic_name)

    if room.flood_state_threshold == "enabled" and sensor_data.floodState:
        alert_msg = "Flood detected"
        alerts.append((alert_msg, room.flood_alerts.split(',')))
        Alert.objects.create(room=room, type="Flood Alert", message=alert_msg)
        for alert in room.flood_alerts.split(','):
            publish_alert(alert, room.topic_name)

    if room.pir_state_threshold == "enabled" and sensor_data.pirState:
        alert_msg = "Motion detected"
        alerts.append((alert_msg, room.pir_alerts.split(',')))
        Alert.objects.create(room=room, type="Motion Alert", message=alert_msg)
        for alert in room.pir_alerts.split(','):
            publish_alert(alert, room.topic_name)

    if room.gas_state_threshold == "enabled" and sensor_data.gasState:
        alert_msg = "Gas detected"
        alerts.append((alert_msg, room.gas_alerts.split(',')))
        Alert.objects.create(room=room, type="Gas Alert", message=alert_msg)
        for alert in room.gas_alerts.split(','):
            publish_alert(alert, room.topic_name)        

    return alerts



######################################################################################################################################################################################################################################################################################################################################################################################################################################################







# def latest_alerts_api(request):
#     # Retrieve the latest alerts from the database
#     latest_alerts = Alert.objects.order_by('-timestamp')[:50]

#     # Convert the alerts data to JSON format
#     alerts_data = [{
#         'id': alert.id,
#         'room': alert.room.name,
#         'type': alert.type,
#         'message': alert.message,
#         'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
#         'viewed': alert.viewed,
#     } for alert in latest_alerts]

#     # Return the JSON response
#     return JsonResponse({'alerts': alerts_data})


# @login_required
# def latest_alertss_api(request):
#     if request.user.is_authenticated:
#         try:
#             sub_admin = SubAdmin.objects.get(user=request.user)
#             rooms = sub_admin.rooms.all()
#             latest_alerts = Alert.objects.filter(room__in=rooms).order_by('-timestamp')[:50]
#         except SubAdmin.DoesNotExist:
#             return JsonResponse({'alerts': []})
#     else:
#         return JsonResponse({'alerts': []})

#     alerts_data = [{
#         'id': alert.id,
#         'room': alert.room.name,
#         'type': alert.type,
#         'message': alert.message,
#         'timestamp': localtime(alert.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
#         'viewed': alert.viewed,
#     } for alert in latest_alerts]

#     return JsonResponse({'alerts': alerts_data})



# @require_POST
# @login_required
# def mark_alerts_viewed(request):
#     viewed_alert_ids = request.POST.getlist('viewed_alerts')
#     Alert.objects.filter(id__in=viewed_alert_ids).update(viewed=True)
#     return redirect('main_admin_dashboard')


# @require_POST
# def mark_alertss_viewed(request):
#     viewed_alert_ids = request.POST.getlist('viewed_alertss')
#     Alert.objects.filter(id__in=viewed_alert_ids).update(viewed=True)
#     return redirect('sub_admin_dashboard')

############################################################################################################################################################333


### below code must be uncomment 


# def connect_mqtt():
#     global mqtt_client
#     mqtt_client = mqtt.Client()
#     mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
#     mqtt_client.on_connect = on_connect
#     mqtt_client.on_message = on_message

#     while True:
#         try:
#             mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEP_ALIVE)
#             mqtt_client.loop_forever()
#             break
#         except Exception as e:
#             print("Error connecting to MQTT broker:", str(e))
#             time.sleep(5)
#######################################################################################################################

# DUMMY    # USE KAXINJU ITHU FULL KALANJITT MUKALIL ULLA FUNCTION UNCOMMENT CHEYYANAM 

def connect_mqtt():
    global mqtt_client
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    while True:
        try:
            mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEP_ALIVE)
            mqtt_client.loop_forever()
            break
        except Exception as e:
            print("Error connecting to MQTT broker:", str(e))
            time.sleep(5)

        # # # # Start sending dummy messages
        send_dummy_messages()

# def send_dummy_messages():
#     topics = ["device1","device2","device3","device4","device5","device6","device7","device8","device9","device10","device11"]
#     # topics = ["device11"]
#     # topics = ["bibin_final_test"]
#     while True:
#         try:
#             dummy_message = generate_dummy_message()
#             for topic in topics:
#                 mqtt_client.publish(topic, json.dumps(dummy_message))
#         except Exception as e:
#             print("Error sending dummy message:", str(e))
#         time.sleep(1)  # Add a small sleep interval to prevent high CPU usage

# def generate_dummy_message():
#     temperature = round(random.uniform(0, 100), 2)
#     humidity = round(random.uniform(0, 100), 2)
#     doorState = random.randint(0, 1)
#     floodState = random.randint(0, 1)
#     pirState = random.randint(0, 1)
#     gasState = random.randint(0, 1)

#     return {
#         "temperature": temperature,
#         "humidity": humidity,
#         "doorState": doorState,
#         "floodState": floodState,
#         "pirState": pirState,
#         "gasState": gasState
#     }

def send_dummy_messages():
    topics = ["device1","device2","device3","device4","device5","device6","device7","device8","device9","device10"]
    
    while True:
        try:
            # Generate the dummy message
            dummy_message = generate_dummy_message()
            
            # Select a random topic
            topic = random.choice(topics)
            
            # Publish the message to the selected topic
            mqtt_client.publish(topic, json.dumps(dummy_message))
            
            # Wait for 10 seconds before sending the next message
            time.sleep(20)
            
        except Exception as e:
            print("Error sending dummy message:", str(e))

def generate_dummy_message():
    temperature = round(random.uniform(0, 100), 2)
    humidity = round(random.uniform(0, 100), 2)
    doorState = random.randint(0, 1)
    floodState = random.randint(0, 1)
    pirState = random.randint(0, 1)
    gasState = random.randint(0, 1)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "doorState": doorState,
        "floodState": floodState,
        "pirState": pirState,
        "gasState": gasState
    }

#################################################################

mqtt_thread = threading.Thread(target=connect_mqtt)
mqtt_thread.daemon = True
mqtt_thread.start()


def start_mqtt_client():  #############################################################
    connect_mqtt()
    mqtt_client.loop_forever()
     


# Start the MQTT client in a separate thread
mqtt_thread = threading.Thread(target=start_mqtt_client)
mqtt_thread.daemon = True  # Daemonize the thread so it will exit when the main thread exits
mqtt_thread.start()



def mqtt_thread():
    while True:
        try:
            mqtt_client.connect(MQTT_SERVER, MQTT_PORT, 60)
            mqtt_client.loop_forever()
        except Exception as e:
            print("Error connecting to MQTT broker:", str(e))
            # Attempt to reconnect after a delay
            time.sleep(0)

# Start the MQTT client thread
mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.daemon = True
mqtt_thread.start()


##code for fetching the data from all topics and save in db

###################################################################################################

 # code for getting the value in the alarmcontent also 
def get_rooms(request):
    rooms = Room.objects.all()
    room_data = [{'id': room.id, 'name': room.name} for room in rooms]
    return JsonResponse({'rooms': room_data})

def get_room_sensor_data(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
        # Assuming you want the latest sensor data for the room
        latest_sensor_data = room.sensor_data.latest('timestamp')
        data = {
            'temperature': latest_sensor_data.temperature,
            'humidity': latest_sensor_data.humidity,
            'doorState': latest_sensor_data.doorState,
            'floodState': latest_sensor_data.floodState,
            'pirState': latest_sensor_data.pirState,
            'gasState':latest_sensor_data.gasState,
            'humidity_threshold':room.humidity_threshold,
            'temperature_threshold':room.temperature_threshold,
            'timePeriod':room.interval
        }
        return JsonResponse(data)
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)
    except SensorData.DoesNotExist:
        return JsonResponse({'error': 'No sensor data found for this room'}, status=404)
    


######################################


#################################################
    

##########################################################################################################################



##########################################################################################################################
 #threshold setting part 

def thresholdFormsubmit(request):
    if request.method == 'POST':
        romid = int(request.POST['romid'])
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        doorState = request.POST['doorState']
        floodState = request.POST['floodState']
        pirState = request.POST['pirState']
        gasState = request.POST['gasState']
        timePeriod = request.POST['timePeriod']
        

        temperature_alerts = request.POST.getlist('temalert')
        humidity_alerts = request.POST.getlist('humalert')
        door_alerts = request.POST.getlist('dooralert')
        flood_alerts = request.POST.getlist('floodalert')
        pir_alerts = request.POST.getlist('piralert')
        gas_alerts = request.POST.getlist('gasalert')
        gsm_alert = request.POST['gsmalert']
        gsm_numbers = request.POST.getlist('gsmnumbers')

        data = Room.objects.get(id=romid)
        data.temperature_threshold = temperature
        data.humidity_threshold = humidity
        data.door_state_threshold = doorState
        data.flood_state_threshold = floodState
        data.pir_state_threshold = pirState
        data.gas_state_threshold = gasState
        data.interval = timePeriod

        data.temperature_alerts = ','.join(temperature_alerts)
        data.humidity_alerts = ','.join(humidity_alerts)
        data.door_alerts = ','.join(door_alerts)
        data.flood_alerts = ','.join(flood_alerts)
        data.pir_alerts = ','.join(pir_alerts)
        data.gas_alerts = ','.join(gas_alerts)
        data.gsm_alert = gsm_alert
        data.gsm_numbers = ','.join(gsm_numbers)

        data.save()
        return redirect('main_admin_dashboard')
    






@login_required
@require_POST
def temperatureFormsubmit(request):
    romid = int(request.POST['romid'])
    temperature = request.POST['temperature']
    temperature_alerts = request.POST.getlist('temalert')

    data = Room.objects.get(id=romid)
    data.temperature_threshold = temperature
    data.temperature_alerts = ','.join(temperature_alerts)
    data.save()
    return JsonResponse({'message': 'Temperature threshold set successfully'})



@login_required
@require_POST
def humidityFormsubmit(request):
    romid = int(request.POST['romid'])
    humidity = request.POST['humidity']
    humidity_alerts = request.POST.getlist('humalert')

    data = Room.objects.get(id=romid)
    data.humidity_threshold = humidity
    data.humidity_alerts = ','.join(humidity_alerts)
    data.save()
    # return redirect('main_admin_dashboard')
    return JsonResponse({'message': 'Humidity threshold set successfully'})

@login_required
@require_POST
def doorFormsubmit(request):
    romid = int(request.POST['romid'])
    doorState = request.POST['doorState']
    door_alerts = request.POST.getlist('dooralert')

    data = Room.objects.get(id=romid)
    data.door_state_threshold = doorState
    data.door_alerts = ','.join(door_alerts)
    data.save()
    # return redirect('main_admin_dashboard')
    return JsonResponse({'message': 'Door threshold set successfully'})

@login_required
@require_POST
def floodFormsubmit(request):
    romid = int(request.POST['romid'])
    floodState = request.POST['floodState']
    flood_alerts = request.POST.getlist('floodalert')

    data = Room.objects.get(id=romid)
    data.flood_state_threshold = floodState
    data.flood_alerts = ','.join(flood_alerts)
    data.save()
    # return redirect('main_admin_dashboard')
    return JsonResponse({'message': 'Flood threshold set successfully'})

@login_required
@require_POST
def motionFormsubmit(request):
    romid = int(request.POST['romid'])
    pirState = request.POST['pirState']
    pir_alerts = request.POST.getlist('piralert')

    data = Room.objects.get(id=romid)
    data.pir_state_threshold = pirState
    data.pir_alerts = ','.join(pir_alerts)
    data.save()
    # return redirect('main_admin_dashboard')
    return JsonResponse({'message': 'Motion threshold set successfully'})

@login_required
@require_POST
def gasFormsubmit(request):
    romid = int(request.POST['romid'])
    gasState = request.POST['gasState']
    gas_alerts = request.POST.getlist('gasalert')

    data = Room.objects.get(id=romid)
    data.gas_state_threshold = gasState
    data.gas_alerts = ','.join(gas_alerts)
    data.save()
    # return redirect('main_admin_dashboard')
    return JsonResponse({'message': 'Gas threshold set successfully'})


@csrf_exempt
@login_required
@require_POST
def gsmFormsubmit(request):
    romid = int(request.POST['romid'])
    gsm_alert = request.POST['gsmalert']
    gsm_numbers = request.POST.getlist('gsmnumbers') if gsm_alert == 'enabled' else []

    data = Room.objects.get(id=romid)
    data.gsm_alert = gsm_alert
    data.gsm_numbers = ','.join(gsm_numbers)
    data.save()
    return JsonResponse({'message': 'GSM Number set successfully'})

@csrf_exempt
@login_required
@require_POST
def intervalFormsubmit(request):
    romid = int(request.POST['romid'])
    time_period = request.POST['timePeriod']

    data = Room.objects.get(id=romid)
    data.interval = time_period
    data.save()
    return JsonResponse({'message': 'Interval set successfully'})









def get_sensor_data(request, room_id):
    room = Room.objects.get(id=room_id)
    latest_sensor_data = room.sensor_data.order_by('-timestamp').first()

    if latest_sensor_data:
        data = {
            'temperature': latest_sensor_data.temperature,
            'humidity': latest_sensor_data.humidity,
            'doorState': latest_sensor_data.doorState,
            'floodState': latest_sensor_data.floodState,
            'pirState': latest_sensor_data.pirState,
            'gasState': latest_sensor_data.gasState,
        }
    else:
        data = {
            'temperature': None,
            'humidity': None,
            'doorState': None,
            'floodState': None,
            'pirState': None,
            'gasState': None,
        }

    return JsonResponse(data)





