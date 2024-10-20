from django.urls import path
from .views import MultipleAPI

urlpatterns = [
    path('', MultipleAPI.as_view() )
]