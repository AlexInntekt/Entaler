from django.urls import path

from .views import EmployeesListView

urlpatterns = [
	path('', EmployeesListView.as_view()),
]