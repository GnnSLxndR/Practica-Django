#encoding:utf-8
from django.forms import ModelForm, DateField, CharField
from django import forms
from polls.models import Choice, Poll

class PollForm(ModelForm):
	question = CharField(max_length=34 ,widget=forms.TextInput(attrs={'class':'special'}))
	pub_date = DateField(label='fecha de Publicacion')
	class Meta:
		model = Poll
		
class ChoiceForm(ModelForm):
	class Meta:
		model = Choice

class ChoiceForm2(ModelForm):
	
	class Meta:
		model = Choice
		exclude = ('poll',)
