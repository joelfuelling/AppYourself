from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


#? CONSTANT variables assigned to salaires dropdown/CharField in Role Model.
SALARIES = (
    ('$45,000-60,000', 'Jr. Entry Level'),
    ('$60,000-70,000', 'Entry Level'),
    ('$70,000-80,000', 'Intermediate'),
    ('$80,000-95,000', 'Mid-level'),
    ('$95,000-110,000', 'Experienced'),
    ('$110,000 +', 'Senior')
)

class Tag(models.Model): #? This needs placed here so Role can call Tag.
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tags_detail', kwargs={'pk': self.id})


class Role(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.CharField(
        choices=SALARIES,
        default=SALARIES[0][0]
        )
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    pub_date = models.DateField('date added') #* Default set to today in status JS file.
    tags = models.ManyToManyField(Tag)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
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

