from django.db import models

# Create your models here.

# Abstract base classes - related_name

class OtherModel(models.Model):
	pass

class Base(models.Model):
	m2m = models.ManyToManyField(OtherModel, related_name="%(app_label)s%(class)s_related")

	class Meta:
		abstract = True

class ChildA(Base):
	pass

class ChildB(Base):
	pass