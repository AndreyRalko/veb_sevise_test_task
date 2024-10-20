from django.urls import path
from .views import MergeAPI

urlpatterns = [
    path('', MergeAPI.as_view() )
]