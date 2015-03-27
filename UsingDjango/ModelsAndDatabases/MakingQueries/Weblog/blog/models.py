from django.db import models

# Create your models here.

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

# Custom reverse manager

class EntryManager(models.Manager):
	pass

class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()

	objects = models.Manager()
	entries = EntryManager()

	def __unicode__(self):
		return self.headline

class EntryDetail(models.Model):
	entry = models.OneToOneField(Entry)
	details = models.TextField()