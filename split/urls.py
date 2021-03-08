from django.urls import path

from .views import view_employee
from .views import view_department


urlpatterns = [
    path('emp/', view_employee.emp),
    path('dept/', view_department.dept),
]
