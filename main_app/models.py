from django.db import models
from django.urls import reverse
from datetime import date
import datetime

#? CONSTANT variables assigned to salaires dropdown/CharField in Role Model.
SALARIES = (
    ('$45,000-60,000', 'Jr. Entry Level'),
    ('$60,000-70,000', 'Entry Level'),
    ('$70,000-80,000', 'Intermediate'),
    ('$80,000-95,000', 'Mid-level'),
    ('$95,000-110,000', 'Experienced'),
    ('$110,000 +', 'Senior')
)
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.CharField(
        choices=SALARIES,
        default=SALARIES[0][0]
        )
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    pub_date = models.DateField('date added') #? Default set to day
    #M:M will go below this line.
    #follow_ups = models.ManyToManyField(FollowUp)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('role_detail', kwargs={"pk": self.id})
        # Lets an individual OBJECT tell the app "my detail page is 'this'"
    
