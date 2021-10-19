from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.html import conditional_escape
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PostManager(models.Manager):

    def published(self):
        now = timezone.now()
        return self.filter(Q(publish_date__lte=now) | Q(publish_date=None)).order_by("-publish_date")


class ItemManager(models.Manager):

    def available(self):
        return self.all()


class Tag(models.Model):

    name = models.SlugField(
        max_length=32,
        db_index=True,
        unique=True,
        help_text='Tag name'
    )

    def __str__(self):
        return self.name


class Project(models.Model):

    name = models.SlugField(
        max_length=32,
        db_index=True,
        unique=True,
        help_text='Project internal name'
    )
    title = models.CharField(
        max_length=255,
        help_text='Project title'
    )
    description = models.TextField(
        help_text='Project description'
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
    preview_upload = models.ImageField(
        help_text='Preview image',
        blank=True,
    )
    preview_image = models.CharField(
        max_length=255,
        help_text='URL of the preview image (internal)',
        blank=True,
    )
    preview_image_external = models.CharField(
        max_length=255,
        help_text='URL of the preview image (external sites)',
        blank=True,
    )
    preview_text = models.TextField(
        help_text='Short preview text',
    )
    content = RichTextUploadingField(
        help_text='Content of the post'
    )
    tags = models.ManyToManyField(
        Tag,
        help_text='Tags'
    )

    def __str__(self):
        return self.title


class Item(models.Model):

    objects = ItemManager()

    title = models.CharField(
        max_length=255,
        help_text='Name of the item'
    )
    sku = models.CharField(
        max_length=255,
        unique=True,
        help_text='SKU of the item'
    )
    slug = models.SlugField(
        help_text='Slug of the item',
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
    preview_docs = models.TextField(
		blank=True,
        help_text='Preview datasheet link',
    )
    description = RichTextUploadingField(
        help_text='Long item description'
    )
    specifications = RichTextUploadingField(
        help_text='Technical specifications (specifications tab)'
    )
    docs = RichTextUploadingField(
        blank=True,
        help_text='Links to datasheets and stuff (docs tab)'
    )
    info = RichTextUploadingField(
        blank=True,
        help_text='Additional information about item (info tab)'
    )
    project = models.ManyToManyField(
        Project,
        help_text='Project'
    )

    def __str__(self):
        return self.title



class Feedback(models.Model):
    name = models.CharField(
        max_length=255,
        help_text='User name'
    )
    code = models.CharField(
        max_length=255,
		blank=True,
        help_text='Internal code'
	)
    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Date feedback was submitted'
    )
    email = models.CharField(
        max_length=255,
        help_text='User email'
    )
    text = models.TextField(
        help_text='Feedback text'
    )

    def __str__(self):
        return 'Feedback from ' + self.email