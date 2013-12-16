from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Requirement(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # relationships
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created_on']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Requirement, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/requirement/%i/' % self.id


class Case(models.Model):
    type_choice = (
        ('BUG', 'Bug'),
        ('FEATURE_REQUEST', 'Feature Request'),
    )
    #data fields
    type = models.CharField(max_length=155, choices=type_choice)
    title = models.CharField(max_length=55)
    detail = models.TextField()
    closed = models.BooleanField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User)
    requirement = models.ForeignKey(Requirement, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Case, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/cases/%i/' % self.id