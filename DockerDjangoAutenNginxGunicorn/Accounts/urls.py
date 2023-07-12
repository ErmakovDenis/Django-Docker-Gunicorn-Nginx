from django.urls import path, include

from DockerDjangoAutenNginxGunicorn.Accounts.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
]