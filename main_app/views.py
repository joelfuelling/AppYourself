from django.shortcuts import render
from django.http import HttpResponse

jobs = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]


def home(request):
    return render (request, 'home.html')
# Create your views here.

def about(request):
    return render(request, 'about.html')

def jobs_index(request):
    return render(request, 'jobs/index.html', {
        'jobs': jobs
    })
