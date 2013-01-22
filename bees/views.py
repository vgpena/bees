from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.db import models
import datetime
from datetime import date, datetime
from bees.models import *

def index(TemplateView):
	template_name = "index.html"
	
def roster(request):
	past = Member.objects.exclude(current_member=True).order_by("weapon", "gender")
	current = Member.objects.filter(current_member=True).order_by("weapon", "gender")
	return render_to_response("roster.html", {"current": current, "past": past})
	
def events(request):
	categories = Category.objects.all()
	past_events = Event.objects.exclude(date__gte=datetime.now()).order_by("category")
	upcoming_events = Event.objects.filter(date__gte=datetime.now()).order_by("category")
	
	return render_to_response("events.html", {"categories": categories, "past": past_events, "upcoming": upcoming_events})
	
def gallery(request):
	galleries = Gallery.objects.order_by("index")
	
	return render_to_response("gallery.html", {"galleries": galleries})