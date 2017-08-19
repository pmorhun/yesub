# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from base.models import Podcast


class HomeView(TemplateView):
    template_name = 'home.html'
    model = Podcast

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['podcasts'] = Podcast.objects.all()
        return context


class ListenView(TemplateView):
    template_name = 'listen.html'
    model = Podcast

    def get_context_data(self, **kwargs):
        context = super(ListenView, self).get_context_data(**kwargs)
        context['podcast'] = Podcast.objects.filter(id=int(kwargs['pk'])).first()
        return context

