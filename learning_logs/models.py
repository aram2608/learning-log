from django.db import models # A model tells Django how to work with the day that will be stored in the app

class Topic(models.Model):
    """A topic the user is learning about.""" # Model Field Reference https://docs.djangoproject.com/en/4.1/ref/models/fields
    text = models.CharField(max_length=200) # max character length for storing topic titles in our database
    date_added = models.DateTimeField(auto_now_add=True) # Django sets the date and time at the time of a post

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ForeignKey is a database term, connects each entry to a specific topic
    text = models.TextField() #another textField, no limit here  CASCADE stands for cascading delete, if a topic is deleted all entries should be too
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: # tells Django to use entries as a plural term for Entry
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text