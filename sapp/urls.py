from django.contrib import admin
from django.urls import path, include
from .views import Home, About, Contact, Team, Faq, Error , Blogs, Careers, PrivacyPolicy, ComingSoon, SingleBlog,feedback_view,feedback_success,submit_feedback

app_name = 'sapp'
urlpatterns = [
    path('', Home, name='index'),
    path('about/', About, name='about'),
    path('team/', Team, name='team'),
    path('contact/', Contact, name='contact'),
    path('faq/', Faq, name='faq'),
    path('error/', Error, name='error'),
    path('blogs/', Blogs, name='blogs'),
    path('careers/', Careers, name='careers'),
    path('privacy/', PrivacyPolicy, name='privacy'),
    path('comingsoon/', ComingSoon, name='comingsoon'),
    path('single-blog/<int:pk>/', SingleBlog, name='single-blog'),
    path('feedback/', feedback_view , name='feedback'),
    path('feedback/success/', feedback_success, name='feedback_success'),
    path('feedback_form/', submit_feedback, name='feedback_form'),
]
