# django-cybersecurity-blog
<h1>Cybersecurity Blog Application</h1>
<h3>Overview</h3>
<p>This project is a blog application designed for a cybersecurity company. It allows users to register, log in, and manage their posts, while also enabling anonymous feedback submission. Additionally, users can apply for job openings, and superusers have access to manage all posts and applications.</p>
<h3>Features</h3>
User Authentication: Users can register and log in to access their personal posts.
CRUD Operations:
    Users can create, read, update, and delete their own posts.
    Superusers can manage all posts in the system.

Feedback System:
    Anonymous users can submit feedback.
    Only superusers can view feedback comments.

Job Application:
    Users can apply for job openings.
    Superusers can view and manage job applications.

<h3>Test GIFs</h3>
Here are some test demonstrations showing how the main functions of the application work.
    Feedback Test:
    Post Test:
    Apply Test (Anonymous):
    Editing Post in Admin Panel:
    Related Post Functionality:
    Broken Access Control Test:
      An unprivileged user (Anas) can delete a post created by another user (Barbarossa) by manipulating the URL.
    Fixed Broken Access Control:
      This issue was fixed using UserPassesTestMixin and a custom test_func to check if the user is the post owner or a superuser.
<h3>Technology Stack</h3>
Backend Framework: Django
Database: SQLite3 (default)
Frontend: HTML, CSS
<h3>Installation</h3>
1. Clone the repository: git clone <repository-url>
2. Navigate to the project directory: cd blogging
3. Create a superuser to access the admin panel: python manage.py createsuperuser
4. Run the development server: python manage.py runserver
5. Open your browser and navigate to http://127.0.0.1:8000/
