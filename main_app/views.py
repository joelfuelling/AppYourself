from django.shortcuts import render, redirect
from .models import Role, Tag
from .forms import FollowUpForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

def home(request):
    return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_followup(request, pk):
    #? The model 'form' can be passed in the data from the submission (request.POST, in this case). Then, we validate to avoid sending/receiving unwanted/orphan data.
    form = FollowUpForm(request.POST)
    if form.is_valid():
        # "staging" the new_followup, but not committing to the Db yet.
        #? Why can't we save it yet? Because the followup model is only setup for 'name', 'contact', and 'date, not id.
        new_followup = form.save(commit=False)
        # Below, add the role_id and assign the primary key. 
        # #! Database Relationship is always stord in 'modelname_id'
        new_followup.role_id = pk
        #? now, we can commit to the db.
        new_followup.save()
    #? Return to the page, where the current pk=pk, or the "same page"
    return redirect('role_detail', pk=pk)
    
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
    fields = ['name', 'salary', 'location', 'description']
    

class RoleDelete(DeleteView):
    model = Role
    success_url = '/tags'

class RoleDetail(DetailView):
    model = Role
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        followup_form = FollowUpForm()
        #?
        role = self.get_object() #? role is 'this' object now, so below we can use 'it' to create the id_list
        id_list = role.tags.all().values_list('id', flat=True)
        tags_role_doesnt_have = Tag.objects.exclude(id__in=id_list) #? One line that relies on built in methods, the Django way. Instead of writing out the whole "if not in loop, create list, add to list" nonsense.
        context['tags_role_doesnt_have'] = tags_role_doesnt_have
        #?
        context['followup_form'] = followup_form
        return context
    
class TagList(ListView):
  model = Tag

class TagDetail(DetailView):
  model = Tag

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
  model = Tag
  fields = ['name']
  success_url = '/tags'

class TagDelete(DeleteView):
  model = Tag
  success_url = '/tags'

def assoc_tag(request, role_id, tag_id):
  Role.objects.get(id=role_id).tags.add(tag_id)
  return redirect('role_detail', pk=role_id)

def unassoc_tag(request, role_id, tag_id):
  Role.objects.get(id=role_id).tags.remove(tag_id)
  return redirect('role_detail', pk=role_id)