from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from app_2.models import Companies

# Create your views here.


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'app_2/companies_index.html'
    paginate_by = 5


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    template_name = 'app_2/companies_form.html'

    def get_success_url(self) -> str:
        return reverse('companies:companies_list')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    template_name = 'app_2/companies_form.html'

    def get_success_url(self) -> str:
        return reverse('companies:companies_list')


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:companies_list')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:companies_list')
