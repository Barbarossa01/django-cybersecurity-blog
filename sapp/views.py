from django.shortcuts import render, get_object_or_404, redirect
from Articles.models import Article
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def Home(request):
    return render(request,'index.html')


def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Team(request):
    return render(request,'team.html')

def Faq(request):
    return render(request,'faq.html')
    


def Error(request):
    return render(request,'404.html')

def Blogs(request):
    articles = Article.objects.all().order_by('-date')
    context = {
        'all_articles': articles
    }
    return render(request, 'blogs.html', context)

def Careers(request):
    return render(request,'careers.html')


def PrivacyPolicy(request):
    return render(request,'privacy-policy.html')


def ComingSoon(request):
    return render(request,'coming-soon.html')


def SingleBlog(request, pk):
    # Fetch the single article based on ID
    article = get_object_or_404(Article, pk=pk)
    
    # Fetch the latest three articles excluding the current one
    related_articles = Article.objects.exclude(pk=pk).order_by('-date')[:3]
    
    context = {
        'article': article,
        'last_three_articles': related_articles,
    }
    return render(request, 'single-blog.html', context)

def blog_list(request):
    articles = Article.objects.filter(is_approved=True)  # Only show approved articles
    return render(request, 'blog/blog_list.html', {'articles': articles})




def feedback_success(request):
    return render(request, 'feedback_success.html')  # A simple success 


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def feedback_view(request):
    feedbacks = Feedback.objects.all()  # Get all feedback entries
    return render(request, 'feedback.html', {'feedbacks': feedbacks})


def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the feedback directly
            return redirect('sapp:feedback_success')  # Redirect to feedback listing page
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})