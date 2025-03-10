# Generated by Django 4.2.7 on 2024-09-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("GTRE_APPLICATION", "0002_room_alert_mqtt_device"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="alert_mqtt_device",
            field=models.ManyToManyField(
                blank=True,
                related_name="alert_mqtt_devices",
                to="GTRE_APPLICATION.mqttdevice",
            ),
        ),
    ]
