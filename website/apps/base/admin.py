# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from base.models import Podcast

# Register your models here.


class PodcastAdmin(admin.ModelAdmin):
    model = Podcast
    fields = ('title', 'text', 'is_displayed', 'priority', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Podcast, PodcastAdmin)