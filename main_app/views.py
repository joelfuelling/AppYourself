from django.shortcuts import render
from .models import Role
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Cats has the above line broken up #! FYI --------
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView



def home(request):
    return render (request, 'home.html')
# Create your views here.

def about(request):
    return render(request, 'about.html')

def roles_detail(request, pk):
    role = Role.objects.get(id=pk)
    return render(request, 'main_app/role_detail.html',
    {'role': role }
    )

#class based views.
class RoleList(ListView):
    model = Role

class RoleCreate(CreateView):
    model = Role
    fields = '__all__'
    #? Using Django, we only need a single URL-based route because a CreateView CBV will automatically:
        #? Create a Django ModelForm used to automatically create the form's inputs for the Model.
        #? Handle the Request:
            #? GET request ===> Render and display a template (html). On that template, we'll include a <form>, it will display our Form.
            #? POST request ===> Use the posted form's contents to (automatically and transparently) create data and perform a redirect (usually to our index page)

class RoleUpdate(UpdateView):
    model = Role
    fields = '__all__'

class RoleDelete(DeleteView):
    model = Role
    success_url = '/role'

class RoleDetail(DetailView):
    model = Role