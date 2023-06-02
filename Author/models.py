from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

news = 'Новости'
article = 'Статьи'

POSITTIONS = [
	(news, 'Новости'),
	(article, 'Статьи')
]

# Create your models here.
# Модель автор
class Author(models.Model):
	id_user = models.OneToOneField(User, on_delete= models.CASCADE)
	rating = models.IntegerField(default= 0)

	def update_rating(self):
		all_posts = Post.objects.all().filter(id_user)
		return all_posts


# Модель категория
class Category(models.Model):
	name_category = models.CharField(max_length= 50, unique= True)

# Модель пост
class Post(models.Model):
	id_author = models.ForeignKey(Author, on_delete= models.CASCADE)
	field_news_or_article = models.CharField(max_length= 20,
											choices= POSITTIONS)
	date_post = models.DateTimeField(auto_now_add= True)
	id_category = models.ManyToManyField(Category, through= 'PostCategory')
	article_title = models.CharField(max_length= 100)
	text_article = models.TextField()
	rating = models.IntegerField(default= 0)

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		if self.rating > 0:
			self.rating -= 1
			self.save()
		else:
			self.rating = 0
			self.save()

	def preview(self):
		return self.text_article[:124] + '...'

# Модель пост-категория
class PostCategory(models.Model):
	id_post = models.ForeignKey(Post, on_delete= models.CASCADE)
	id_category = models.ForeignKey(Category, on_delete= models.CASCADE)

# Модель Comment
class Comment(models.Model):
	id_post = models.ForeignKey(Post, on_delete= models.CASCADE)
	id_user = models.ForeignKey(User, on_delete= models.CASCADE)
	text_comment = models.TextField()
	date_time_post = models.DateTimeField(auto_now_add= True)
	rating = models.IntegerField(default= 0)

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		if self.rating > 0:
			self.rating -= 1
			self.save()
		else:
			self.rating = 0
			self.save()
