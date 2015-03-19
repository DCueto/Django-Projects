# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# Model fields

class Musician(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	instrument = models.CharField(max_length=100)

class Album(models.Model):
	artist = models.ForeignKey(Musician)
	name = models.CharField(max_length=100)
	release_date = models.DateField()
	num_stars = models.IntegerField()

# Choices

class Person(models.Model):
	SHIRT_SIZES = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

# Primary key field

class Fruit(models.Model):
	name = models.CharField(max_length=100, primary_key=True)

# Verbose field names

class VerboseFields(models.Model):
	first_name = models.CharField("person's first name", max_length=30)
	fruit = models.ForeignKey(Fruit, verbose_name="the related fruit")
	albums = models.ManyToManyField(Album, verbose_name="list of albums")
	musician = models.OneToOneField(Musician, verbose_name="related musician")


# Many_to_one relationships

class Manufacturer(models.Model):
	# ...
	name = models.CharField(max_length=64)

class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	# ...

# Many_to_many relationships

class Topping(models.Model):
	# ...
	name = models.CharField(max_length=64)

class Pizza(models.Model):
	# ...
	toppings = models.ManyToManyField(Topping)


# Extra fields on many-to-many relationships

class PersonTwo(models.Model):
	name = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(PersonTwo, through="Membership")

	def __unicode__(self):
		return self.name

class Membership(models.Model):
	person = models.ForeignKey(PersonTwo)
	group = models.ForeignKey(Group)
	date_joined = models.DateField()
	invite_reason = models.CharField(max_length=64)


# Models across files

	# from geography.models import ZipCode

	# class Restaurant(models.Model):
		# zip_code = models.ForeignKey(ZipCode)


# Meta options

class Ox(models.Model):
	horn_length = models.IntegerField()

	class Meta:
		verbose_name_plural = "oxen"
		ordering = ['horn_length']

# Model methods

class CustomPerson(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_date = models.DateField()

	def baby_boomer_status(self):
		"Returns the person's baby-boomer status."
		import datetime
		if self.birth_date < datetime.date(1945,8,1):
			return "Pre-boomer"
		elif self.birth_date < datetime.date(1965, 1, 1):
			return "Baby boomer"
		else:
			return "Post-boomer"

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.first_name, self.last_name)

	full_name = property(_get_full_name)


# Overriding predefined model methods

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def save(self, *args, **kwargs):
		if self.name == "Yoko Ono's blog":
			return #Yoko shall never have her own blog!
		else:
			super(Blog, self).save(*args, **kwargs) #Call the "real" save() method.

	