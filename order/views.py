from django.shortcuts import render , get_object_or_404
from order.models import Order
from django.views.generic import *
from boat.models import Boat
from django.urls import reverse


class OrderCreateView(CreateView):
    model = Order
    fields = ('boat','name','email','message',)

    def get_success_url(self):
        return reverse('boat:boat_view',args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['boat'] = get_object_or_404(Boat,pk=self.kwargs.get('pk'))

        return context_data

