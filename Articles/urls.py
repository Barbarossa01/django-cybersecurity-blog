
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    List,
    Create,
    Update,
    Delete,
    Detail,
    MyLoginView,
    ProfileView,
    RegisterView,
    apply_for_job,
    list_applications,
    success_view,
    delete_application,
    my_logout_view,
    feedback_view,
)

app_name = 'post'

urlpatterns = [
    path('', List.as_view(), name='list'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('post/<int:pk>/', Detail.as_view(), name='detail'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', my_logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('apply/', apply_for_job, name='apply_for_job'),
    path('applications/', list_applications, name='list_applications'),
    path('success/', success_view, name='success'),
    path('applications/delete/<int:pk>/', delete_application, name='delete_application'),  # Correctly defined here
    path('feedback/', feedback_view, name='feedback'),
]

