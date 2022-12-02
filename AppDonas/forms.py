from django import forms

class FormDonareg(forms.Form):
    sabor=forms.CharField(max_length=50)
    precio=forms.IntegerField()

class FormDonaprem(forms.Form):
    sabor= forms.CharField(max_length=50)
    precio= forms.IntegerField()

class FormMalteadas(forms.Form):
    sabor= forms.CharField(max_length=50)
    precio= forms.IntegerField()