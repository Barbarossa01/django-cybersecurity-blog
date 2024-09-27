from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from django.shortcuts import reverse 
from .models import Article, JobApplication
from Articles.models import Article
from .forms import ArticleForm, RegisterForm, JobApplicationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView , FormView
from django.shortcuts import redirect 
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404
from sapp.views import feedback_view
from sapp.models import Feedback

class MyLoginView(LoginView):
    
    redirect_authenticated_user = True  # the authenticated user gonna be redirected out of login page

    def get_success_url(self):
        messages.success(self.request,"Login successful" )
        return reverse_lazy("post:list")    
    
    def form_invalid(self, form):
        messages.error(self.request,"Error in username or password" )
        return self.render_to_response(self.get_context_data(form=form)) # to make the user stay at the same page (form)    
    
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is already authenticated and logged in
        if self.request.user.is_authenticated:
            return redirect('post:list')  # Redirect to profile if logged in
        return super().dispatch(request, *args, **kwargs)
    

def my_logout_view(request):
      logout(request)  # Log out the user
      return redirect(reverse_lazy('post:login'))  # Redirect to login page

class RegisterView(FormView):
    
    redirect_authenticated_user = True  # the authenticated user gonna be redirected out of login page
    template_name='registration/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('post:login')

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is already authenticated and logged in
        if self.request.user.is_authenticated:
            return redirect('post:profile')  # Redirect to profile if logged in
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
      user = form.save()
      if user:
        login(self.request,user)
      return super(RegisterForm,self).form_valid(form)




class Create(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('post:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # save the user to the current user 
        form.instance.is_approved = False  # Set is_approved to False by default
        messages.success(self.request, 'Your post has been successfully uploaded!')  # Add the success message
        return super().form_valid(form)  # Call the parent class's form_valid method


class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #restrict the updating of posts to superusers only while allowing normal users to manage only their own posts
    model = Article
    template_name='update.html'
    form_class=ArticleForm
    success_url= reverse_lazy('post:list')

    def form_valid(self, form):
        return super().form_valid(form)  
    
    def test_func(self):
        article = self.get_object()
        return self.request.user.is_superuser or article.user == self.request.user


class Delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#This mixin allows you to implement custom permission logic.
    model = Article
    template_name='delete.html'
    success_url= reverse_lazy('post:list')

    def test_func(self): # checks if the user is a superuser or if the article belongs to the user
        article = self.get_object()
        return self.request.user.is_superuser or article.user == self.request.user
    

class List(LoginRequiredMixin,ListView):
    model = Article
    template_name='articles.html'
    context_object_name='articles'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()  # Admin sees all articles
        return Article.objects.filter(user=self.request.user)  # Editor sees only their articles
    
    
class ProfileView(LoginRequiredMixin,TemplateView):
    def get_template_names(self):
        return ['users/profile.html']

class Detail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Article
    template_name= 'detail.html'
    context_object_name = 'articles'
    
    def test_func(self):
        article = self.get_object()
        return self.request.user.is_superuser or article.user == self.request.user



def apply_for_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the application data
            messages.success(request, 'Application submitted successfully!')
            return redirect('post:success')  # Redirect to the success page
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def list_applications(request):
    applications = JobApplication.objects.all()  # Retrieve all applications
    return render(request, 'jobs/list_applications.html', {'applications': applications})

def success_view(request):
    return render(request, 'jobs/success.html')  # Make sure this path is correct



@user_passes_test(lambda u: u.is_superuser)
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, id=pk)
    application.delete()
    return redirect('post:list_applications')  # Correct name used here


