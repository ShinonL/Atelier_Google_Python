from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from app_1.models import Locations

# Create your views here.


class LocationsView(LoginRequiredMixin, ListView):
    model = Locations
    template_name = 'app_1/locations_index.html'


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Locations
    fields = ['city', 'country']
    template_name = 'app_1/locations_form.html'

    def get_success_url(self) -> str:
        return reverse('locations:locations_list')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Locations
    fields = ['city', 'country']
    template_name = 'app_1/locations_form.html'

    def get_success_url(self) -> str:
        return reverse('locations:locations_list')


@login_required
def delete_location(request, pk):
    Locations.objects.filter(id=pk).update(active=0)
    return redirect('locations:locations_list')


@login_required
def activate_location(request, pk):
    Locations.objects.filter(id=pk).update(active=1)
    return redirect('locations:locations_list')
