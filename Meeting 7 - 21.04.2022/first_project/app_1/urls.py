from django.urls import include, path
from app_1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='locations_list'),
    path('add/', views.CreateLocationView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_location, name='delete'),
    path('<int:pk>/activate/', views.activate_location, name='activate'),
]
