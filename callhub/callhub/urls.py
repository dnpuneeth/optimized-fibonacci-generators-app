"""callhub URL Configuration"""

from django.urls import include, path


urlpatterns = [
    path('', include('fibonacci.urls'))
]
