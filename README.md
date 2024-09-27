# django-cybersecurity-blog
<h1>Cybersecurity Blog Application</h1>
<h3>Overview</h3>
<p>This project is a blog application designed for a cybersecurity company. It allows users to register, log in, and manage their posts, while also enabling anonymous feedback submission. Additionally, users can apply for job openings, and superusers have access to manage all posts and applications.</p>
<h3>Features</h3>
User Authentication: Users can register and log in to access their personal posts.<br>
CRUD Operations:
<br>    Users can create, read, update, and delete their own posts.
<br>   Superusers can manage all posts in the system.
<br>
<br>Feedback System:
 <br>   Anonymous users can submit feedback.
 <br>   Only superusers can view feedback comments.

<br>Job Application:
    <br>Users can apply for job openings.
    <br>Superusers can view and manage job applications.

<br><h3>Test GIFs</h3>
<br>Here are some test demonstrations showing how the main functions of the application work.
    <br>Feedback Test:
    ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/Feedback.gif)

    <br>
   Post Test:
   ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/Post.gif)

<br>    Apply Test (Anonymous):    
![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/applyToJob.gif)

   <br> Editing Post in Admin Panel:
    ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/EditPost.gif)

   <br> Related Post Functionality:
    ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/RelatedPost.gif)

   <br> Broken Access Control Test:
    ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/BrokenAccessControl.gif)

    <br>  
   An unprivileged user (Anas) can delete a post created by another user (Barbarossa) by manipulating the URL.
    <br> Fixed Broken Access Control:
        ![Alt text](https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/FixedBrokenAccessControl.gif)
     <br> This issue was fixed using UserPassesTestMixin and a custom test_func to check if the user is the post owner or a superuser.
<br> <h3>Technology Stack</h3>
<br>Backend Framework: Django
<br>Database: SQLite3 (default)
<br>Frontend: HTML, CSS
<br><h3>Installation</h3>
<br>1. Clone the repository: git clone <repository-url>
<br>2. Navigate to the project directory: cd blogging
<br>3. Create a superuser to access the admin panel: python manage.py createsuperuser
<br>4. Run the development server: python manage.py runserver
<br>5. Open your browser and navigate to http://127.0.0.1:8000/
