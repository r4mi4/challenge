from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('test/', views.ExternalAPIView.as_view(), name='view'),
]