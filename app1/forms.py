from django import forms
from .models import Topic, Entry
class TitleForm (forms.ModelForm):#1st form

	class Meta:
		model = Topic#built the form from topic model
		fields = ['text']#include in form only fields
		labels = {'text': ''}#not generate label for text fields

class ContentForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Your Content:'}
		widgets = {'text': forms.Textarea(attrs = {'cols': 80})}


		