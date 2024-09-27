# Generated by Django 5.1.1 on 2024-09-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_article_is_approved_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('portfolio_link', models.URLField()),
                ('github_link', models.URLField()),
                ('about', models.TextField()),
            ],
        ),
    ]
