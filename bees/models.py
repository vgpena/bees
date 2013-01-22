from django.db import models
from daguerre.models import Image

class Category(models.Model):
	"""
	Describes type of Event.
	
	"""
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	
	class Meta:
		verbose_name_plural = 'categories'
	
	
	def __unicode__(self):
		return (self.name)

class Event(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=200)
	category = models.ForeignKey('Category', blank=True, null=True)
	link = models.URLField(blank=True)
	location = models.CharField(max_length=250)
	date = models.DateTimeField()
	summary = models.TextField(blank=True)
	preview_image = models.ForeignKey('daguerre.Image', blank=True, null=True)
	media_gallery = models.ForeignKey('Gallery', blank=True, null=True)
	
	def __unicode__(self):
		return (self.title)

class Gallery(models.Model):
	"""
	I want to put videos here eventually, but photos will do fine for now.
	Might want to use https://github.com/andrewebdev/django-video for that?
	Also needs (as an optional field) a FK to an Event from another yet-to-be-made app.

	"""
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100)
	index = models.PositiveIntegerField(help_text="This can be used to determine the order in which the galleries are displayed.")

	class Meta:
		verbose_name_plural = 'galleries'

	def __unicode__(self):
		return (self.title)


class Photo(models.Model):
	"""
	For use in galleries, or alone.
	
	"""
	image = models.ForeignKey('daguerre.image')
	credit = models.CharField(max_length=200, blank=True)
	caption = models.CharField(max_length=300, blank=True)
	gallery = models.ForeignKey('Gallery', related_name="photos")
	slug = models.SlugField(max_length=200)

	def __unicode__(self):
		return(self.slug)
				

"""
Options for Member: gender (until collegiate fencing becomes more progressive) and weapon.

"""
GENDER_CHOICES = (
	('Women\'s', 'Female'),
	('Men\'s', 'Male'),
)

WEAPON_CHOICES = (
	('Epee', 'Epee'),
	('Foil', 'Foil'),
	('Sabre', 'Sabre'),
)


class Member(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=40)
	slug = models.SlugField(max_length=40)
	current_member = models.BooleanField()
	grad_year = models.IntegerField(max_length=4, blank=True, null=True)
	titles = models.CharField(max_length=250, blank=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	weapon = models.CharField(max_length=10, choices=WEAPON_CHOICES)
	photo = models.ForeignKey('daguerre.Image', blank=True, null=True)
	bio = models.TextField()

	def __unicode__(self):
		return (self.slug)