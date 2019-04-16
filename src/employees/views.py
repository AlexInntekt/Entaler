"""
employees/views
"""
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Employee


class EmployeesListView(ListView):
	model = Employee
	template_name = "employees.html"

