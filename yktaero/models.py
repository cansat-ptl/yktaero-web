from django.db import models
from django.db.models import Q
from django.utils import timezone


class PostManager(models.Manager):

	def published(self):
		now = timezone.now()
		return self.filter(Q(publish_date__lte=now) | Q(publish_date=None)).order_by("-created")

class Tag(models.Model):

	name = models.SlugField(
		max_length=32,
		db_index=True,
		unique=True,
		help_text='Tag name'
	)
	
	def __str__(self):
		return self.name


class Post(models.Model):

	objects = PostManager()

	created = models.DateTimeField(
		auto_now_add=True,
		help_text='Date and time the post was created'
	)
	updated = models.DateTimeField(
		auto_now=True,
		help_text='Date and time the post was last updated',
	)
	publish_date = models.DateTimeField(
		blank=True,
		null=True,
		help_text='(optional) If set, when to publish the post'
	)
	title = models.CharField(
		max_length=255,
		help_text='Title of the post'
	)
	slug = models.SlugField(
		help_text='Slug of the post',
		db_index=True,
		unique=True,
		null=True,
		blank=True,
	)
	preview_image = models.TextField(
		help_text='URL of the preview image',
		blank=True,
	)
	preview_image_external = models.TextField(
		help_text='URL of the preview image (external sites)',
		blank=True,
	)
	preview_text = models.TextField(
		help_text='Short preview text',
	)
	content = models.TextField(
		help_text='Content of the post'
	)
	tags = models.ManyToManyField(
		Tag,
		help_text='Tags'
	)

	def __str__(self):
		return self.title
