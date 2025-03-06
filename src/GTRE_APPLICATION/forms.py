# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room,Building
from django.core.exceptions import ValidationError

from django import forms
from .models import Room
from .models import Cluster
from .models import Building,SubAdmin,MainAdmin

from .models import PowerModule





class AddRoomForm(forms.Form):
    name = forms.CharField(max_length=100)
    ip_address = forms.GenericIPAddressField()
    topic_name = forms.CharField(max_length=255)



class EditThresholdForm(forms.ModelForm):
    room_id = forms.IntegerField(widget=forms.HiddenInput())
    threshold_type = forms.CharField(widget=forms.HiddenInput())
    threshold_value = forms.FloatField()

    class Meta:
        model = Room
        fields = ['room_id', 'threshold_type', 'threshold_value']





class AddBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'rooms']

    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)






class EditBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'rooms']

    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


  
# class AddClusterForm(forms.ModelForm):
#     class Meta:
#         model = Cluster
#         fields = ['name', 'description', 'rooms']
#     rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

class AddClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['name', 'description', 'rooms', 'buildings', 'power_modules', 'main_admins', 'sub_admins']
    
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    buildings = forms.ModelMultipleChoiceField(queryset=Building.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    power_modules = forms.ModelMultipleChoiceField(queryset=PowerModule.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    main_admins = forms.ModelMultipleChoiceField(queryset=MainAdmin.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    sub_admins = forms.ModelMultipleChoiceField(queryset=SubAdmin.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


class EditClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['name', 'description', 'rooms']
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)





class SelectBuildingsForm(forms.Form):
    sub_admin_id = forms.IntegerField(widget=forms.HiddenInput())
    buildings = forms.ModelMultipleChoiceField(
        queryset=Building.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    





# class PowerModuleForm(forms.ModelForm):
#     class Meta:
#         model = PowerModule
#         fields = ['name', 'topic_name', 'ip_address', 'buildings']  # Include buildings field
#         widgets = {
#             'buildings': forms.CheckboxSelectMultiple(),  # Optional: use checkboxes for multi-select
#         }

class PowerModuleForm(forms.ModelForm):
    class Meta:
        model = PowerModule
        fields = ['name', 'topic_name', 'ip_address', 'ct1correspondingname', 'ct2correspondingname', 'ct3correspondingname', 'ct4correspondingname', 'buildings']
        widgets = {
            'buildings': forms.CheckboxSelectMultiple(),  # Optional: use checkboxes for multi-select
        }


###############################################################################
