from django import forms
from my_work.models import UserGarbageBin,Complaint, UserArea


class UserGarbageBinForm(forms.ModelForm):
    class Meta:
        model = UserGarbageBin
        fields = [ 'bin']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['issue']


class AddLocation(forms.ModelForm):
    class Meta:
        model=UserArea
        fields=['area','street','buildingno']


