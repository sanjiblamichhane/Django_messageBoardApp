from django.db import models

# Create your models here.
class Post(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text[:50]
	#note that we just created a new database model called Post which has the database field text.
	# We have also specified the type of content it will hold, TextField()
