from django.urls import path
from app_2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='companies_list'),
    path('add/', views.CreateCompanyView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateCompanyView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_company, name='delete'),
    path('<int:pk>/activate/', views.activate_company, name='activate'),
]
