from django import forms
from django.forms import ModelForm
from .models import Honor, Honoree, Organization

class HonoreeForm(ModelForm):

#	honor = forms.ModelMultipleChoiceField(queryset=Honor.objects.all())

	class Meta:
		model = Honoree
		fields = ['affiliation','first_name','middle_name','last_name','email']#,'honor']
