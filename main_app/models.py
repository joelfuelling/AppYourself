from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Tag(models.Model): #? This needs placed here so Role can call Tag.
  name = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE)  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tags_detail', kwargs={'pk': self.id})


class Role(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.CharField(default='$', max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(default='(include a link!)', max_length=3000)
    pub_date = models.DateField('date added') #* Default set to today in static JS file.
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #? AUTO CREATED Django stuff
    #? followup_set = [FollowUp]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('role_detail', kwargs={"pk": self.id})
        # Lets an individual OBJECT tell the app "my detail page is 'this'"
    
class FollowUp(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField('contact info', max_length=30)
    date = models.DateField('date contacted')
    # reply = models.BooleanField()
    #* Below is the line creating the 1:M relationship.
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name} via {self.contact} was contacted on {self.date} about {self.role} role'
    
    class Meta:
        ordering = ['-date']






# After adding #!"user = models.ForeignKey(User, on_delete=models.CASCADE)"#!...
# In the RoleModel above, perform the actions below:
#*>>> python3 manage.py makemigrations
# Which then presents us with this message:

#*>>> You are trying to add a non-nullable field 'user' to cat without a default;
#*>>> we can't do that (the database needs something to populate existing rows).
#*>>> Please select a fix:
#*>>>  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
#*>>>  2) Quit, and let me add a default in models.py
#*>>> Select an option:

#$ Option 1) is our best option because it will allow us to enter the id of a user, which we created earlier this week (the superuser).
# Go ahead and press 1 and [enter], which will then prompt us to enter the value:

#*>>> Please enter the default value now, as valid Python
#*>>> The datetime and django.utils.timezone modules are available,
#*>>> so you can do e.g. timezone.now
#*>>> Type 'exit' to exit this prompt
#*>>> >>> 1 [press enter]

#Our superuser's id should be 1, so type 1 and press [enter].
# The migration file will then be created. Let's migrate the changes:
# python3 manage.py migrate"
