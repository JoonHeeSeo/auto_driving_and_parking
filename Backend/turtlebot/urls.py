from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view),
    path('custom_parking', views.test_view),

]