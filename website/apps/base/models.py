# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DisplayManager(models.Manager):
    def get_queryset(self):
        return super(DisplayManager, self).get_queryset().filter(is_displayed=True)


class DisplayModel(models.Model):
    is_displayed = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)

    objects = models.Manager()  # The default manager.
    displayed_objects = DisplayManager()

    class Meta:
        abstract = True
        ordering = ('priority',)


class Podcast(DisplayModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title
