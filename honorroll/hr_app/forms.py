from django import forms
from django.forms import ModelForm
from hr_app.models import Organization, Honoree, Honor

class UploadForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file  = forms.FileField()

class HonoreeForm(ModelForm):
	class Meta:
		model = Honoree
		exclude = ['parent']

class HonorForm(ModelForm):
	class Meta:
		model = Honor
		exclude = ['parent']