from django.db import models

class message(models.Model):
	body_message=models.CharField(max_length=80)

	def _unicode_(self):
        	return (self.body_message)

