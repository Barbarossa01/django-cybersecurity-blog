<h1>Django Cybersecurity Blog</h1>

<h2>Overview</h2>
<p>This project is a blog application designed for a cybersecurity company. It allows users to register, log in, and manage their own posts, while also enabling anonymous feedback submissions. Additionally, users can apply for job openings, and superusers can manage all posts, feedback, and applications.</p>

<h2>Features</h2>
<ul>
  <li><strong>User Authentication</strong>:  
    <ul>
      <li>Users can register and log in to access and manage their personal posts.</li>
    </ul>
  </li>

  <li><strong>CRUD Operations</strong>:
    <ul>
      <li>Users can create, read, update, and delete their own posts.</li>
      <li>Superusers have full control over all posts in the system.</li>
    </ul>
  </li>

  <li><strong>Feedback System</strong>:
    <ul>
      <li>Anonymous users can submit feedback.</li>
      <li>Only superusers can view feedback comments in the admin panel.</li>
    </ul>
  </li>

  <li><strong>Job Application</strong>:
    <ul>
      <li>Users can apply for available job openings.</li>
      <li>Superusers can view and manage job applications.</li>
    </ul>
  </li>
</ul>

<h2>Test GIFs</h2>
<p>Below are demonstrations of the main functions of the application:</p>

<ul>
  <li><strong>Feedback Test</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/Feedback.gif" alt="Feedback Test">
  </li>

  <li><strong>Post Test</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/Post.gif" alt="Post Test">
  </li>

  <li><strong>Apply Test (Anonymous)</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/applyToJob.gif" alt="Apply Test">
  </li>

  <li><strong>Editing Post in Admin Panel</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/EditPost.gif" alt="Editing Post">
  </li>

  <li><strong>Related Post Functionality</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/RelatedPost.gif" alt="Related Post">
  </li>

  <li><strong>Broken Access Control Test</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/BrokenAccessControl.gif" alt="Broken Access Control">
    <p>An unprivileged user (Anas) can delete a post created by another user (Barbarossa) by manipulating the URL.</p>
  </li>

  <li><strong>Fixed Broken Access Control</strong>:
    <br><img src="https://github.com/Barbarossa01/django-cybersecurity-blog/blob/main/tests/FixedBrokenAccessControl.gif" alt="Fixed Broken Access Control">
    <p>This issue was fixed using <code>UserPassesTestMixin</code> and a custom <code>test_func</code> to check if the user is the post owner or a superuser.</p>
  </li>
</ul>

<h2>Technology Stack</h2>
<ul>
  <li><strong>Backend Framework</strong>: Django</li>
  <li><strong>Database</strong>: SQLite3 (default)</li>
  <li><strong>Frontend</strong>: HTML, CSS</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Clone the repository: <code>git clone &lt;repository-url&gt;</code></li>
  <li>Navigate to the project directory: <code>cd blogging</code></li>
  <li>Create a superuser to access the admin panel: <code>python manage.py createsuperuser</code></li>
  <li>Run the development server: <code>python manage.py runserver</code></li>
  <li>Open your browser and navigate to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></li>
</ol>
