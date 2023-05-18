from django.shortcuts import render, redirect
from .models import Role, Tag
from .forms import FollowUpForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
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
    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    #! This is how to create a 'user' form object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#class based views.


class RoleList(LoginRequiredMixin, ListView):
    model = Role
    
    #? Translated from objects.get.all() from index_view function version.
    def get_queryset(self):
       queryset = super().get_queryset()
       print(queryset)
       return queryset.filter(user=self.request.user)

class RoleCreate(LoginRequiredMixin, CreateView):
    model = Role
    fields = ['name', 'company_name', 'salary', 'location', 'description', 'pub_date']
    #? Using Django, we only need a single URL-based route because a CreateView CBV will automatically:
        #? Create a Django ModelForm used to automatically create the form's inputs for the Model.
        #? Handle the Request:
            #? GET request ===> Render and display a template (html). On that template, we'll include a <form>, it will display our Form.
            #? POST request ===> Use the posted form's contents to (automatically and transparently) create data and perform a redirect (usually to our index page)
    # This inherited method is called when a valid cat form is being submitted
    def form_valid(self, form):
      #* We're overriding the CreateView's form_valid method to assign the logged in user, self.request.user.
      form.instance.user = self.request.user
      #* In Python, methods inherited by the superclass can be invoked by prefacing the method name with super().
      return super().form_valid(form)
      #* Accordingly, after updating the form to include the user, we're calling super().form_valid(form) to let the CreateView do its usual job of creating the model in the database and redirecting.
      #* Yes, the logged in user will automatically be assigned to the request object similar to what Passport did in Express!
    
class RoleUpdate(LoginRequiredMixin, UpdateView):
    model = Role
    fields = ['name', 'salary', 'location', 'description']
    

class RoleDelete(LoginRequiredMixin, DeleteView):
    model = Role
    success_url = '/tags'

class RoleDetail(LoginRequiredMixin, DetailView):
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
    
class TagList(LoginRequiredMixin, ListView):
  model = Tag

class TagDetail(LoginRequiredMixin, DetailView):
  model = Tag

class TagCreate(LoginRequiredMixin, CreateView):
  model = Tag
  fields = ['name']

class TagUpdate(LoginRequiredMixin, UpdateView):
  model = Tag
  fields = ['name']
  success_url = '/tags'

class TagDelete(LoginRequiredMixin, DeleteView):
  model = Tag
  success_url = '/tags'

@login_required
def assoc_tag(request, role_id, tag_id):
  Role.objects.get(id=role_id).tags.add(tag_id)
  return redirect('role_detail', pk=role_id)

@login_required
def unassoc_tag(request, role_id, tag_id):
  Role.objects.get(id=role_id).tags.remove(tag_id)
  return redirect('role_detail', pk=role_id)