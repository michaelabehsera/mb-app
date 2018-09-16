from django.db import models

# Create your models here.

'''
Note that we've created a new database model called Post
which has the database field text. We've also specified
the type of content it will hold, TextField(). Django
provides many model fields supporting common types of
content such as characters, dates, integers, emails and so on
'''

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
