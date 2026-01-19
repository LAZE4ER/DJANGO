
from django.urls import path

from .views import visit_counter_view, visit_reset

urlpatterns = [
    path('visit-counter/', visit_counter_view, name='visit_counter'),
    path('reset-visit-counter/', visit_reset, name='reset_visit_counter'),
]