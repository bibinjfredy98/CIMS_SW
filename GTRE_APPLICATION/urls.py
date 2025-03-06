#GTRE_APPLICATION/urls.py

from django.urls import path
from . import views
# from .views import sub_admin_signup_view
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import custom_logout
from .views import delete_room
from .views import get_rooms
from .views import get_room_sensor_data
# from .views import push_button
from .views import add_mqtt_device, add_gsm_module
from .views import (
    temperatureFormsubmit, humidityFormsubmit, doorFormsubmit,
    floodFormsubmit, motionFormsubmit, intervalFormsubmit,gasFormsubmit, gsmFormsubmit
)
# from .views import add_powermqtt_device, configure_power_sources, get_active_power_source

from .views import admin_login


# from .views import base
from .views import *
from .views import edit_room, delete_rooom
from .views import edit_threshold, toggle_sensor









urlpatterns = [
    # path('home', views.home, name='home'),
    # path('main-admin/login/', views.main_admin_login, name='main_admin_login'),
    # path('main-admin/dashboard/', views.main_admin_dashboard, name='main_admin_dashboard'),

    # path('main-admin/dashboard/', main_admin_dashboard, name='main-admin/dashboard'),
    
    # path('dashboard/alert_counts/', alert_counts, name='alert_counts'),
    path('dashboard/rooms/', room_list, name='room_list'),



    path('dashboard/room/<int:room_id>/', room_details, name='room_details'),

#################
    path('sub-admin/dashboard/', views.sub_admin_dashboard, name='sub_admin_dashboard'),
    path('sub-admin/dashboard/', sub_admin_dashboard, name='sub-admin/dashboard'),

        # path('sub-admin/login/', views.sub_admin_login, name='sub_admin_login'),
    path('sub-admin/dashboard/', views.sub_admin_dashboard, name='sub_admin_dashboard'),

    path('subadmindashboard/', views.sub_admin_dashboard, name='sub_admin_dashboard'),


    

    path('roomsub/', roomsub, name='roomsub'),
    path('alertssub/', views.alerts_pagesub, name='alertssub'),
    # path('alerts-indexsub/', views.alerts_pagesub, name='alerts-indexsub'),
    path('alertssub/', views.alerts_pagesub, name='alerts_pagesub'),

    

    path('lives-indexsub/', livessub, name='lives-indexsub'),


    # path('get_alerts_data/', views.get_alerts_data, name='get_alerts_data'),

    path('get_live_sensor_datasub/', get_live_sensor_datasub, name='get_live_sensor_datasub'),



    

    






###########################


    # path('room/', views.room, name='room'),
    path('rsignup-sub-admin/', views.rsub_admin_signup_view, name='rsignup_sub_admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('main-admin/logout/', views.custom_logout, name='custom_logout'),
    path('sub-admin/logout/', views.customm_logout, name='customm_logout'),
    path('delete-room/', views.delete_room, name='delete_room'),
    path('get-sub-admin-rooms/<int:sub_admin_id>/', views.get_sub_admin_rooms, name='get_sub_admin_rooms'),
    path('get-room-sensor-data/<int:room_id>/', views.get_room_sensor_data, name='get_room_sensor_data'),
    path('api/rooms/', get_rooms, name='get_rooms'),
    path('api/get-room-sensor-data/<int:room_id>/', get_room_sensor_data, name='get_room_sensor_data'),
    path('thresholdFormsubmit', views.thresholdFormsubmit, name='thresholdFormsubmit'),
    # path('api/latest_alerts/', views.latest_alerts_api, name='latest_alerts_api'),
    # path('mark-alerts-viewed/', views.mark_alerts_viewed, name='mark_alerts_viewed'),
    path('fetch-data/', views.fetch_data, name='fetch_data'),

    # path('api/latest_alertss/', views.latest_alertss_api, name='latest_alertss_api'),

    # path('push-button', push_button, name='push_button'),
    # path('mark-alertss-viewed/', views.mark_alertss_viewed, name='mark_alertss_viewed'),



    path('add_mqtt_device/', add_mqtt_device, name='add_mqtt_device'),
    # path('list_mqtt_devices/', list_mqtt_devices, name='list_mqtt_devices'),



    path('add_gsm_module/', add_gsm_module, name='add_gsm_module'),
    # path('list_gsm_modules/', list_gsm_modules, name='list_gsm_modules'),


    path('delete_mqtt_device/', views.delete_mqtt_device, name='delete_mqtt_device'),
    path('delete_gsm_module/', views.delete_gsm_module, name='delete_gsm_module'),

    path('temperatureFormsubmit/', temperatureFormsubmit, name='temperatureFormsubmit'),
    path('humidityFormsubmit/', humidityFormsubmit, name='humidityFormsubmit'),
    path('doorFormsubmit/', doorFormsubmit, name='doorFormsubmit'),
    path('floodFormsubmit/', floodFormsubmit, name='floodFormsubmit'),
    path('motionFormsubmit/', motionFormsubmit, name='motionFormsubmit'),
    path('intervalFormsubmit/', intervalFormsubmit, name='intervalFormsubmit'),
    path('gasFormsubmit/', gasFormsubmit, name='gasFormsubmit'),
    path('gsmFormsubmit/', gsmFormsubmit, name='gsmFormsubmit'),



    path('api/get_sensor_data/<int:room_id>/', views.get_sensor_data, name='get_sensor_data'),


    # path('add_powermqtt_device/', add_powermqtt_device, name='add_powermqtt_device'),
    # path('configure_power_sources/', configure_power_sources, name='configure_power_sources'),
    # path('get_active_power_source/', get_active_power_source, name='get_active_power_source'),



    path('admin-login/', admin_login, name='admin_login'),
    

    # path('signup-sub-admin/', sub_admin_signup_view, name='signup_sub_admin'),




    # path('base/', base, name='base'),



    # path('index/', index, name='index'),
    path('room/', room, name='room'),


    # path('rooms/edit/<int:pk>/', edit_room, name='edit_room'),
    # path('rooms/delete/<int:pk>/', delete_room, name='delete_room'),

    path('rooms/edit/<int:room_id>/', edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', delete_rooom, name='delete_rooom'),
   
    path('add-room/', add_room, name='add_room'),


    path('device/', device, name='device'),

    # path('device/', views.device, name='device'),
    path('add-mqtt-device/', views.add_mqtt_device, name='add_mqtt_device'),
    path('edit-mqtt-device/<int:device_id>/', views.edit_mqtt_device, name='edit_mqtt_device'),
    path('delete-mqtt-device/', views.delete_mqtt_device, name='delete_mqtt_device'),
    path('get-mqtt-device/<int:device_id>/', views.get_mqtt_device, name='get_mqtt_device'),
    path('add-gsm-module/', views.add_gsm_module, name='add_gsm_module'),
    path('edit-gsm-module/<int:module_id>/', views.edit_gsm_module, name='edit_gsm_module'),
    path('delete-gsm-module/', views.delete_gsm_module, name='delete_gsm_module'),
    path('get-gsm-module/<int:module_id>/', views.get_gsm_module, name='get_gsm_module'),


    path('edit_threshold/', edit_threshold, name='edit_threshold'),
    path('toggle_sensor/', toggle_sensor, name='toggle_sensor'),
    path('update_alert/', views.update_alert, name='update_alert'),








    
    path('alerts/', views.alerts_page, name='alerts'),

    



# ##

    # path('dashboard/details/<str:detail_type>/<int:detail_id>/', get_details, name='get_details'),



    path('get_alerts/', views.get_alerts, name='get_alerts'),

    




    # path('building/add/', add_building, name='add_building'),
    # path('building/config/', building_config, name='building_config'),
    # path('building/edit/<int:pk>/', edit_building, name='edit_building'),
    # path('building/delete/<int:pk>/', delete_building, name='delete_building'),

    path('building-config/', building_config, name='building_config'),
    path('add-building/', add_building, name='add_building'),
    path('edit-building/<int:pk>/', edit_building, name='edit_building'),
    path('delete-building/<int:pk>/', delete_building, name='delete_building'),

    path('add_cluster/', views.add_cluster, name='add_cluster'),
    path('clusters/add/', views.add_cluster, name='add_cluster'),
    path('clusters/edit/<int:cluster_id>/', views.edit_cluster, name='edit_cluster'),
    path('clusters/delete/<int:cluster_id>/', views.delete_cluster, name='delete_cluster'),


    path('reset_alert/', views.reset_alert, name='reset_alert'),

    path('alerts/', views.alerts_page, name='alerts_page'),
    path('update-alerts/', views.update_alerts, name='update_alerts'),

    path('get_alert_details/<int:alert_id>/', views.get_alert_details, name='get_alert_details'),

    path('lives-index/', lives, name='lives-index'),


    path('get_live_sensor_data/', get_live_sensor_data, name='get_live_sensor_data'),




    path('approve_sub_admin/<int:sub_admin_id>/', approve_sub_admin, name='approve_sub_admin'),
    path('reject_sub_admin/<int:sub_admin_id>/', reject_sub_admin, name='reject_sub_admin'),
    path('rsub_admin_signup_view/', rsub_admin_signup_view, name='rsub_admin_signup_view'),

    
    path('assign-buildings/', assign_buildings, name='assign_buildings'),
    path('assign-buildings/', views.assign_buildings, name='assign-buildings'),

    


    path('download-data/', download_data, name='download_data'),
    
    # path('fetch-alert-data/', fetch_alert_data, name='fetch_alert_data'),

    # path('all_rooms_alerts/', all_rooms_alerts, name='all_rooms_alerts'),
    

    path('get-active-inactive-rooms/', get_active_inactive_rooms, name='get_active_inactive_rooms'),

    path('get-active-inactive-rooms-dash1/', get_active_inactive_rooms_dash1, name='get_active_inactive_rooms_dash1'),


    path('all_rooms_alertssub/', all_rooms_alertssub, name='all_rooms_alertssub'),

    # path('fetch_room_data_tem/', fetch_room_data_tem, name='fetch_room_data_tem'),


    #  #############  
    #  # # filteration graphs of tem and hum in the live page 
     
    # path('fetch_room_data_test/', fetch_room_data_test, name='fetch_room_data_test'),

    
    

    
    




    # path('update_alert_view_status/', update_alert_view_status, name='update_alert_view_status'),



    path('delete-sub-admin/<int:sub_admin_id>/', delete_sub_admin, name='delete_sub_admin'),
    path('toggle-suspend-sub-admin/<int:sub_admin_id>/', toggle_suspend_sub_admin, name='toggle_suspend_sub_admin'),

    path('add_power_module/', views.add_power_module, name='add_power_module'),
    path('api/power-data/', power_data_api, name='power_data_api'),




    # path('power-module/<int:id>/', power_module_detail, name='power_module_detail'),
    # path('power-module/<int:id>/update/', power_module_update, name='power_module_update'),
    # path('power-module/<int:id>/delete/', power_module_delete, name='power_module_delete'),



    


    

    path('view-power-module/<int:pk>/', views.view_power_module, name='view_power_module'),
    path('edit-power-module/', views.edit_power_module, name='edit_power_module'),
    path('delete-power-module/', views.delete_power_module, name='delete_power_module'),




    

    path('mark_all_alerts_as_viewed/<int:building_id>/', mark_all_alerts_as_viewed, name='mark_all_alerts_as_viewed'),


    path('select-mqtt-device/', views.select_mqtt_device, name='select_mqtt_device'),
    




    # path('api/sensor-dataa/', get_sensor_dataa, name='get_sensor_dataa'),
    # path('api/sensor-dataaa/', get_sensor_dataaa, name='get_sensor_dataaa'),





    path('api/sensor-dataaaa/', get_sensor_dataaaa, name='get_sensor_dataaaa'),
    path('api/sensor-dataaaaa/', get_sensor_dataaaaa, name='get_sensor_dataaaaa'),

    path('dashboard/alert_countss/', alert_countss, name='alert_countss'),
    
    # path('api/peaksensor-dataa/', get_peaksensor_dataa, name='get_peaksensor_dataa'),

    # path('api/power-dataa/', get_power_data, name='get_power_data'),




    path('api/peaksensor-dataaa/', get_peaksensor_dataaa, name='get_peaksensor_dataaa'),

    path('api/power-dataaa/', get_power_dataaa, name='get_power_dataaa'),

    path('mark_all_alerts_as_viewedsub/<int:building_id>/', mark_all_alerts_as_viewedsub, name='mark_all_alerts_as_viewedsub'),
    


    
    


  


    
    path('get_alertssub/', views.get_alertssub, name='get_alertssub'),
    path('update-alertssub/', views.update_alertssub, name='update_alertssub'),
    path('get_alert_detailssub/<int:alert_id>/', views.get_alert_detailssub, name='get_alert_detailssub'),
    path('reset_alertsub/', views.reset_alertsub, name='reset_alertsub'),



    path('overview/', views.Overview, name='overview'),



    path('api/alert-stats/', views.alert_stats, name='alert_stats'),



















    path('maindashboard1/', views.main_admin_dashboard1, name='main_admin_dashboard1'),
    # path('maindashboard2/', views.main_admin_dashboard2, name='main_admin_dashboard2'),
    # path('maindashboard3/', views.main_admin_dashboard3, name='main_admin_dashboard3'),
    # path('maindashboard4/', views.main_admin_dashboard4, name='main_admin_dashboard4'),

  
    path('fetch_alert_status/', views.fetch_alert_status, name='fetch_alert_status'),

    # path('get_live_sensor_data_dash3/', get_live_sensor_data_dash3, name='get_live_sensor_data_dash3'),
    # path('get_live_sensor_data_beehive/', get_live_sensor_data_beehive, name='get_live_sensor_data_beehive'),
    path('get-temperature-data/', views.get_temperature_data, name='get_temperature_data'), 
    path('get-humidity-data/', views.get_humidity_data, name='get_humidity_data'),   

    

    
    path('get_combined_sensor_data/', views.get_combined_sensor_data, name='get_combined_sensor_data'),


    path('get_power_sensor_data/', views.get_power_sensor_data, name='get_power_sensor_data'),


    path('get_alert_history/', get_alert_history, name='get_alert_history'),


    path('api/get_buildings/', views.get_buildings, name='get_buildings'),

    path('fetch_live_sensor_data_temhum/', views.fetch_live_sensor_data_temhum, name='fetch_live_sensor_data_temhum'),
    path('fetch_rooms_temhum/', views.fetch_rooms_temhum, name='fetch_rooms_temhum'),




    



    



    






    





    
    





    



    






    



    


    




]





    


