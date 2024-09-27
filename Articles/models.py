from django.db import models
from django.contrib.auth.models import User  # Import User model
from PIL import Image 

# Create your models here.
# ----------------------------------------- Done -----------------------------
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User
    date = models.DateTimeField(auto_now_add=True)
    photo_user = models.ImageField(upload_to='image', blank=True, default='images/no-image-article.jpg')
    photo_article = models.ImageField(upload_to='image', blank=True, default='images/no-photo-user.jpg')
    is_approved = models.BooleanField(default=False)  # Ensure this is defined correctly
    def __str__(self):
        return f"article {self.title} by {self.user} on {self.date}, {self.photo_article}"     # translate the object to string
    class Meta:
        ordering = ['-date']  



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  avatar= models.ImageField(
    default='images/no-photo-user.jpg',upload_to='profile_avatar'
  )
  def __str__(self):
    return f'{self.user.username} profile'
    
  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first
        
        # Open the image
        img = Image.open(self.avatar.path)
        
        # Convert the image to RGB if it's in a mode that JPEG doesn't support
        if img.mode in ("P", "RGBA"):
            img = img.convert("RGB")
        
        # Resize the image if it's larger than the desired size
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        
        # Save the image back to the original path
        img.save(self.avatar.path, format='JPEG')



class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    portfolio_link = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)
    about = models.TextField()
    def __str__(self):
        return self.name