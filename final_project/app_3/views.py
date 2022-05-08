from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from app_3.models import Jobs

# Create your views here.


class JobsView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'app_3/jobs_index.html'
    paginate_by = 5


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'app_3/jobs_form.html'

    def get_success_url(self) -> str:
        return reverse('jobs:jobs_list')


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'app_3/jobs_form.html'

    def get_success_url(self) -> str:
        return reverse('jobs:jobs_list')


@login_required
def delete_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:jobs_list')


@login_required
def activate_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect('jobs:jobs_list')
