from django.forms import ModelForm
from message.models import message

class messageform(ModelForm):
	class Meta:
		model=message
