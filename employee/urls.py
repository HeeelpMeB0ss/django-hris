from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views

app_name = 'employee'
urlpatterns = [
     path('index/', views.EmployeeListView.as_view(), name='index'),
     path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
     path('create/', views.CreateEmployee.as_view(), name='create'),
     path('<int:pk>/update/', views.UpdateEmployee.as_view(), name='update'),
     path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete'),
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path("leave/", views.CreateEmployeeLeave.as_view(), name="leave"),
     path('', TemplateView.as_view(template_name='base.html'), name='base'),
]
