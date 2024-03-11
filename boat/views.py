from django.shortcuts import render
from django.views.generic import *
from boat.models import *

class BoatListView(ListView):
    model = Boat

class BoatDetailView(DetailView):
    model = Boat
    