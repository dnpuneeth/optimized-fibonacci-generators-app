"""callhub URL Configuration"""

from django.urls import include, path


urlpatterns = [
    path('fibonacci/', include('fibonacci.urls'))
]
